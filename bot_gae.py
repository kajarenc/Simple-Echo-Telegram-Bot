#!/usr/bin/env python
import sys
import os

sys.path.append(os.path.join(os.path.abspath('.'), 'venv/lib/python2.7/site-packages/'))

from flask import Flask, request
import telegram
app = Flask(__name__)

global bot
bot = telegram.Bot(token='144611601:AAHH1laGr83dvBLzrEb-f1t0mdNRDRgtU8A')


@app.route('/144611601:AAHH1laGr83dvBLzrEb-f1t0mdNRDRgtU8A', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True))

        chat_id = update.message.chat.id

        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8')
        # repeat the same message back (echo)
        text = text + " hello Suren!"
        bot.sendMessage(chat_id=chat_id, text=text)

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