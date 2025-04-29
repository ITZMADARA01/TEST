from telegram.ext import CommandHandler, MessageHandler, Filters
from database import Database

db = Database()

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to the Slayer Assist Bot!')

def report(update, context):
    report_text = update.message.text.split('/report ')[1]
    db.add_report(update.effective_user.id, report_text)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Report submitted successfully!')

def get_reports(update, context):
    reports = db.get_reports()
    report_text = '\n'.join([f'User {report[1]}: {report[2]}' for report in reports])
    context.bot.send_message(chat_id=update.effective_chat.id, text=report_text)

handlers = [
    CommandHandler('start', start),
    CommandHandler('report', report),
    CommandHandler('get_reports', get_reports),
]
