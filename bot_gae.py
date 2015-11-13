#!/usr/bin/env python
import sys
import os

sys.path.append(os.path.join(os.path.abspath('.'), 'venv/lib/python2.7/site-packages/'))

from flask import Flask, request
import telegram
from bot_logic import Result

app = Flask(__name__)

result = ''

global bot
bot = telegram.Bot(token='144611601:AAHH1laGr83dvBLzrEb-f1t0mdNRDRgtU8A')


@app.route('/144611601:AAHH1laGr83dvBLzrEb-f1t0mdNRDRgtU8A', methods=['POST'])
def webhook_handler():
    global result

    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True))

        chat_id = update.message.chat.id

        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8')
        bot_resp = ''
        if text == '/start':
            bot_resp = "Ok, let's play a game. You can start playing with /play command," \
                       " decrease your score by /increment command, and reset your score by /reset command" \
                       "your can know your score by /get_result command, and lastly you can finish playing " \
                       "with /finish command."
        elif text == "/play":
            local_result = Result()
            result = local_result
            bot_resp = "OK, we start the game!"
        elif text == '/increment':
            if isinstance(result, Result):
                result.increment_result()
                bot_resp = "Hi %s! You result just incremented and now your result is  %s" % (
                    update.message.from_user.first_name,
                    result.get_result())
            else:
                bot_resp = "Before /increment you must start playing with /play command"

        elif text == '/reset':
            if isinstance(result, Result):
                result.reset_result()
                bot_resp = "Hi %s! You result just reset and now your result is  %s" % (
                    update.message.from_user.first_name,
                    result.get_result())
            else:
                bot_resp = "Before /reset you must start playing with /play command"

        elif text == '/get_result':
            if isinstance(result, Result):
                bot_resp = "Hi %s! You result is  %s" % (
                    update.message.from_user.first_name,
                    result.get_result())
            else:
                bot_resp = "Before /get_result you must start playing with /play command"

        elif text == "/finish":
            if isinstance(result, Result):
                result = ''
                bot_resp = "OK, we can play again when you wont!"
            else:
                bot_resp = "Before /finish you must start playing with /play command. It's obvious :D"
        else:
            bot_resp = "Unknown command"

        # repeat the same message back (echo)
        bot.sendMessage(chat_id=chat_id, text=bot_resp)

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
