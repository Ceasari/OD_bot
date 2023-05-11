Handwritten Digit Recognizer Telegram Bot
This is a Telegram bot that recognizes handwritten digits from an image sent to it and returns the original image with bounding boxes and labels around each detected digit.

Installation
To install the required dependencies, run the following command:

Copy code
pip install -r requirements.txt
You will also need to create a bot on Telegram and obtain the access token. Follow the instructions on the Telegram Bot API documentation to create a bot and obtain the access token.

Usage
To start the bot, run the following command:

css
Copy code
python bot.py --token YOUR_BOT_TOKEN
To use the bot, send an image of a handwritten digit to the bot in a chat and wait for the bot to recognize and label the digits in the image. The bot will then return the original image with bounding boxes and labels around each detected digit.

Example
Here is an example of the bot recognizing and labeling handwritten digits in an image:
