import telepot
from googletrans import Translator
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

translator = Translator()
origine = "it"
dest = "en"

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        if msg['text'] == '/dt': #destination
            destinazione = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="English🇺🇸", callback_data="enDest")],[InlineKeyboardButton(text="Italiano🇮🇹", callback_data="itDest")], [InlineKeyboardButton(text="French🇫🇷", callback_data="frDest")]])

            bot.sendMessage(chat_id, "Scegli la lingua di destinazione", reply_markup=destinazione)
        elif msg['text'] == '/sr': #source
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='English🇺🇸', callback_data='en')],[InlineKeyboardButton(text="Italiano🇮🇹", callback_data="it",)], [InlineKeyboardButton(text="French🇫🇷", callback_data="fr")]])

            bot.sendMessage(chat_id, "Scegli la lingua di origine", reply_markup=keyboard)
        else:
            txt = msg["text"]
            print("Origine:",origine,"Destinazione:",dest)
            translations = translator.translate(txt, src=origine, dest=dest)
            bot.sendMessage(chat_id, translations.text)
            name = msg["from"]["first_name"]
            print(name, msg["text"], " -> ", translations.text)

def on_callback_query(msg):
    global origine
    global dest
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print("Query data impostato su : ", query_data)

    if len(query_data) > 2:
        dest = query_data[0:2]
        bot.answerCallbackQuery(query_id, text=query_data + "Impostato come lingua di destinazione")
    else:
        origine = query_data
        bot.answerCallbackQuery(query_id, text=query_data + "Impostato come lingua di origine")

#Creazione del BOT
TOKEN = "843667392:AAH3DNUEM5oPdcNW14OrAxvgX3k5duiZisc"
bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': on_chat_message, 'callback_query': on_callback_query})

import time
while 1:
    time.sleep(10)
