#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tinashe
#
# Created:     10/04/2023
# Copyright:   (c) Tinashe 2023
# Licence:     <your licence>

#Function Definition: The def keyword is used to define a function named main(). 
#However, in this case, the function body is empty (pass).
def main(): 
    pass
#If Statement: 
#The if statement checks if the __name__ attribute of the current module is equal to '__main__'.
if __name__ == '__main__':
    main() 
#Import Statements: 
#These lines import various classes and functions from the telegram.ext and telegram modules.   
from telegram.ext import Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, filters

def welcome(update, context):
    new_members = update.message.new_chat_members

    #For Loop: A for loop iterates over each new_member in the new_members list.
    for new_member in new_members:
        if not new_member.is_bot:
            keyboard = [[InlineKeyboardButton("Пройдите бесплатный тест", callback_data='test')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text(f'Welcome to InChat English, {new_member.first_name}!', reply_markup=reply_markup)

def button(update, context):
    #Attribute Access: The update.callback_query attribute is accessed and assigned to the query variable.
    query = update.callback_query
    if query.data == 'test':
        query.edit_message_text(text="https://forms.gle/jDQkSixC1siZQfNX9")

#Object Instantiation: An Updater object is created with the provided bot token and use_context=True argument.
updater = Updater('5878345073:AAEoJDs3NwTHtSkDAMSds6kRC1iFzpZAEyI', use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
#Method Call: The start_polling() method is called on the updater object to start the bot and begin receiving updates.
updater.start_polling()
#Method Call: The idle() method is called on the updater object to keep the bot running until interrupted (e.g., by pressing Ctrl+C).
updater.idle()
