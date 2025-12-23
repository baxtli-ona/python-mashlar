# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 11:07:43 2025

@author: acer
"""

from transliterate import to_cyrillic, to_latin
import telebot
TOKEN='8553370627:AAFCUdNX_DIWnD9-Db7dJR41r4JQoTXPST8'
bot=telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob="Assalomu alaykum.Xush kelibsiz. Matn kiriting"
    javob+="\nMatn kirrrrringggg: " 
    bot.reply_to(message, javob)
@bot.message_handler(func=lambda messege: True)
def echo_all(message):
    msg=message.text
    javob=lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    
    
    
    
    
    bot.reply_to(message, javob(msg))
            
bot.polling()
