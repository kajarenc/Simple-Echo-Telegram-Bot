SHEDULE = {
    '201': {
        'Monday': [
            "Discrete Mathematics",
            "Object Oriented Programming",
            "Data Structures and Algorithms",

        ],
        'Tuesday': [
            "Data Structures and Algorithms",
            "Object Oriented Programming",
            "Discrete Mathematics",
            "Writing the Essay",

        ],
        'Wednesday': [
            "Data Analysis",
            "Object Oriented Programming",
            "Discrete Mathematics",
            "Data Structures and Algorithms",
        ],
        'Thursday': [
            "Calculus II for Engineers ",
            "Object Oriented Programming",
            "Data Structures and Algorithms",

        ],
        'Friday': [
            "Data Structures and Algorithms",
            "Object Oriented Programming",
            "Computer Architecture and Organization",
            "Calculus II for Engineers ",

        ],
    },
    '202': {
        'Monday': [
            "Object Oriented Programming",
            "Calculus II for Engineers ",
            "Data Analysis",

        ],
        'Tuesday': [
            "Discrete Mathematics",
            "Writing the Essay",
            "Calculus II for Engineers ",

        ],
        'Wednesday': [
            "Data Analysis",
            "Discrete Mathematics",
            "Object Oriented Programming",
        ],
        'Thursday': [
            "Data Structures and Algorithms",
            "Object Oriented Programming",
            "Writing the Essay",
            "Data Analysis",

        ],
        'Friday': [
            "Discrete Mathematics",
            "Object Oriented Programming",
            "Data Structures and Algorithms",

        ],
    },
    '203': {
        'Monday': [
            "Writing the Essay",
            "Data Structures and Algorithms",
            "Object Oriented Programming",
            "Discrete Mathematics",

        ],
        'Tuesday': [
            "Data Analysis",
            "Data Structures and Algorithms",
            "Computer Architecture and Organization",
            "Object Oriented Programming",

        ],
        'Wednesday': [
            "Object Oriented Programming",
            "Discrete Mathematics",
            "Data Analysis",
        ],
        'Thursday': [
            "Computer Architecture and Organization",
            "Writing the Essay",
            "Data Analysis",
            "Object Oriented Programming",

        ],
        'Friday': [
            "Data Structures and Algorithms",
            "Discrete Mathematics",
            "Data Analysis",

        ],
    }
}

GROUPS = ['201', '202', '203']

NEW_USER = 'new_user'
REGISTERED_USER = 'registered_user'

# States are saved in a dict that maps chat_id -> state
state = dict()
# Sometimes you need to save data temporarily
context = dict()

values = dict()
from telegram import ReplyKeyboardMarkup, ReplyKeyboardHide

custom_keyboard = [["Monday", "Tuesday", "Wednesday"],
                   ["Thursday", "Friday", "LOL"]]
reply_markup = ReplyKeyboardMarkup(custom_keyboard)


def constract_pretty_shedule_response(chat_context, text):
    resp = ''
    for i, lesson in enumerate(SHEDULE[chat_context][text], start=1):
        resp += str(i) + '.' + lesson + '\n'
    return resp


def get_random_joke():
    return "random joke"


def handler(bot, update):
    chat_id = update.message.chat.id
    text = update.message.text.encode('utf-8')
    chat_state = state.get(chat_id, NEW_USER)
    chat_context = context.get(chat_id, None)

    if chat_state == NEW_USER and text[0] == '/' or text == '/start':
        state[chat_id] = NEW_USER  # set the state
        # context[chat_id] = user_id  # save the user id to context
        bot.sendMessage(chat_id,
                        text="Stranger, please enter your group number and I can tell your schedule for week!",
                        )
    elif chat_state == NEW_USER and text in GROUPS:
        state[chat_id] = REGISTERED_USER
        context[chat_id] = text
        bot.sendMessage(chat_id=chat_id, text="Dedication passed! Choose day, student", reply_markup=reply_markup)
    elif chat_state == NEW_USER and text not in GROUPS:
        bot.sendMessage(chat_id=chat_id,
                        text=" Hey, if you do not tell me your group number, how do I know your schedule? "
                             "Please, tell me your group number...", reply_markup=ReplyKeyboardHide())

    elif chat_state == REGISTERED_USER:
        if text in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] and chat_context in GROUPS:
            bot.sendMessage(chat_id=chat_id, text=constract_pretty_shedule_response(chat_context, text),
                            reply_markup=reply_markup)
        elif text == "LOL":
            bot.sendMessage(chat_id=chat_id, text=get_random_joke(), reply_markup=reply_markup)
        else:
            state[chat_id] = NEW_USER
            context[chat_id] = None
            bot.sendMessage(chat_id,
                            text="Something went wrong , please use /start command to restart our communication",
                            reply_markup=ReplyKeyboardHide())
