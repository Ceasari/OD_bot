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


# Handwritten Digits Recognition Telegram Bot

This Telegram bot can receive an image with handwritten digits and return the original image with bounding boxes and labels of each detected digit.

## Usage

1. Start a chat with the bot by searching for `@HandwrittenDigitsRecognitionBot`.
2. Send the bot a photo with handwritten digits.
3. Wait for the bot to process the image and return the original image with bounding boxes and labels of each detected digit.

## Example

![Example image with handwritten digits and corresponding output](example.png)

## Requirements

* Python 3.x
* `numpy`
* `opencv-python`
* `pytesseract`
* `python-telegram-bot`

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your-username/handwritten-digits-recognition-bot.git
    cd handwritten-digits-recognition-bot
    ```

2. Install the required libraries:

    ```
    pip install -r requirements.txt
    ```

3. Rename `config.py.example` to `config.py` and update the values:

    ```
    cp config.py.example config.py
    nano config.py
    ```

4. Start the bot:

    ```
    python bot.py
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
