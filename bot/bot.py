from telegram.ext import Updater, Dispatcher
from config import TOKEN
from handlers import handlers

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    for handler in handlers:
        dp.add_handler(handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
