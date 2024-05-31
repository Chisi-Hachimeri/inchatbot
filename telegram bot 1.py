#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tinashe
#
# Created:     10/04/2023
# Copyright:   (c) Tinashe 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
from telegram.ext import Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, filters

def welcome(update, context):
    new_members = update.message.new_chat_members
    for new_member in new_members:
        if not new_member.is_bot:
            keyboard = [[InlineKeyboardButton("Пройдите бесплатный тест", callback_data='test')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text(f'Welcome to InChat English, {new_member.first_name}!', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    if query.data == 'test':
        query.edit_message_text(text="https://forms.gle/jDQkSixC1siZQfNX9")

updater = Updater('5878345073:AAEoJDs3NwTHtSkDAMSds6kRC1iFzpZAEyI', use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()
