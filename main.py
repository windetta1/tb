import telebot
import googletrans
from googletrans import Translator
bot = telebot.TeleBot('6312656723:AAFLJLdNOw19rZzEP7UwNP5CfvQMOzan6Ak')
translator = Translator()
src = 'en'
dest = 'ru'


ru_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
en_letters = 'abcdefghijklmnopqrstuvwxyz'
@bot.message_handler(commands=(['start']))
def main(message):
    bot.send_message(message.chat.id, 'ПРИВЕТ! Напиши в чат сообщение, а я его переведу😁')


@bot.message_handler(func=lambda m: True)
def translate_text(message):
    trnslt = translator.translate(message.text, src=src, dest=dest).text
    trnslt1 = translator.translate(message.text, src=dest, dest=src).text
    textmessage = message.text[0].lower()
    if textmessage in en_letters:
        bot.send_message(message.chat.id, trnslt)
    elif textmessage in ru_letters:
        bot.send_message(message.chat.id, trnslt1)






bot.infinity_polling()
