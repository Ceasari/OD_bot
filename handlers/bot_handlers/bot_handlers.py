from main import dp, bot
from aiogram import types
from keyboards.keyboards import rate_kb
from aiogram.types import ContentType
import os.path
from config import ALLOWED_FORMATS, MODEL_PATH
import cv2
from ultralytics import YOLO
import random
import string
import glob

model = YOLO(MODEL_PATH)

os.makedirs("Temp", exist_ok=True)
os.makedirs("Processed", exist_ok=True)

def generate_random_idx(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choices(letters_and_digits, k=length))


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("I am bot bla bla bla, waiting for photo  .... bla bla bla ")


@dp.message_handler(content_types=[ContentType.PHOTO, ContentType.DOCUMENT])
async def handle_img_and_files(message: types.Message):
    # Handle photos
    if message.photo:
        # get the last photo from the message
        photo = message.photo[-1]
        photo_id = generate_random_idx()
        print(photo_id)
        # download the file to a local directory
        file_path = f"Temp/{photo_id}.jpg"
        output_file_path = f"Temp/"
        try:
            await photo.download(file_path)
            results = model.predict(source=file_path, conf=0.3, imgsz=640)
            res_plotted = results[0].plot()
            cv2.imwrite(output_file_path + f"/{photo_id}_done.jpg", res_plotted)
            with open(output_file_path + f"/{photo_id}_done.jpg", "rb") as photo_file:

                await message.answer_photo(photo_file)
            await message.answer("Please, rate the quality of detection", reply_markup=rate_kb(photo_id))
        except Exception as e:
            await message.answer(f"Error processing file: {e}")


    # Handle documents
    elif message.document and message.document.mime_type.split("/")[0] == "image" and \
            message.document.file_name.split(".")[-1] in ALLOWED_FORMATS:
        # get the last photo from the message
        photo = message.document
        photo_id = generate_random_idx()
        print(photo_id)
        # download the file to a local directory
        file_path = f"Temp/{photo_id}.jpg"
        output_file_path = f"Temp/"
        try:
            await photo.download(file_path)
            results = model.predict(source=file_path, conf=0.3, imgsz=640)
            res_plotted = results[0].plot()
            cv2.imwrite(output_file_path + f"/{photo_id}_done.jpg", res_plotted)
            with open(output_file_path + f"/{photo_id}_done.jpg", "rb") as photo_file:

                await message.answer_photo(photo_file)
            await message.answer("Please, rate the quality of detection", reply_markup=rate_kb(photo_id))
        except Exception as e:
            await message.answer(f"Error processing file: {e}")
    else:
        await message.answer("Sorry, only image files in JPEG, JPG, PNG, and GIF formats are allowed.")


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('rate_'))
async def handle_rate_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    photo_id = callback_query.data.split('|')[-1]
    rate = callback_query.data.split('_')[1]
    if rate == "40" or rate == "60":
        path = "Answer_gifs/Low_rate/"
        video_files = glob.glob(path + "*.mp4")
        random_video = random.choice(video_files)

        # move both the original and done file if quality is bad
        file_path = f"Temp/{photo_id}.jpg"
        output_file_path = f"Temp/{photo_id}_done.jpg"
        if os.path.exists(file_path) and os.path.exists(output_file_path):
            os.rename(file_path, f"Processed/{photo_id}.jpg")
            os.rename(output_file_path, f"Processed/{photo_id}_done.jpg")

    elif rate == "80" or rate == "100":
        path = "Answer_gifs/High_rate/"
        video_files = glob.glob(path + "*.mp4")
        random_video = random.choice(video_files)

        # delete both the original and done file if quality is good
        file_path = f"Temp/{photo_id}.jpg"
        output_file_path = f"Temp/{photo_id}_done.jpg"
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(output_file_path):
            os.remove(output_file_path)
    await bot.send_message(callback_query.message.chat.id, "Thanks for rating!")
    await bot.send_video(callback_query.message.chat.id, open(random_video, 'rb'))


@dp.message_handler(
    content_types=[ContentType.GAME, ContentType.STICKER, ContentType.VIDEO, ContentType.VIDEO_NOTE, ContentType.VOICE,
                   ContentType.CONTACT, ContentType.LOCATION, ContentType.AUDIO])
async def handle_other_types(message: types.Message):
    await message.answer("Sorry, only image files in JPEG, JPG, PNG, and GIF formats are allowed.")
