#!/usr/bin/env python
import sys
import os

sys.path.append(os.path.join(os.path.abspath('.'), 'venv/lib/python2.7/site-packages/'))

from flask import Flask, request
import telegram

app = Flask(__name__)
from bot_logic import handler

bot = telegram.Bot(token='144611601:AAHH1laGr83dvBLzrEb-f1t0mdNRDRgtU8A')


def get_random_joke():
    return "random joke"


@app.route('/144611601:AAHH1laGr83dvBLzrEb-f1t0mdNRDRgtU8A', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True))

        chat_id = update.message.chat.id

        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8')
        # repeat the same message back (echo)

        # response_text = ''
        # if text=="Monday":
        #     response_text = "Monday shedule"
        # elif text=="Tuesday":
        #     response_text = "Tuesday shedule"
        # elif text == "Wednesday":
        #     response_text = "Wednesday shedule"
        # elif text == "Thursday":
        #     response_text = "Thursday shedule"
        # elif text == "Friday":
        #     response_text = "Friday shedule"
        # elif text == "LOL":
        #     response_text = get_random_joke()
        #
        # custom_keyboard = [["Monday", "Tuesday","Wednesday"],
        #                    ["Thursday", "Friday","LOL"]]
        # reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        # bot.sendMessage(chat_id=chat_id, text=response_text, reply_markup=reply_markup)
        # # bot.sendMessage(chat_id=chat_id, text=text)
        handler(bot, update)
    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('https://yerevantaxibot.appspot.com/144611601:AAHH1laGr83dvBLzrEb-f1t0mdNRDRgtU8A')
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return '.'
