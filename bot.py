#Data creazione 21/08/2018
# coding=utf-8

import telepot
import subprocess
import speech_recognition as sr
from pydub import AudioSegment

recognizer_instance = sr.Recognizer()

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'voice':
        name = msg["from"]["first_name"]
        lon = msg["voice"]["duration"]
        voiceName = msg["voice"]["file_id"]
        mimeType = msg["voice"]["mime_type"]
        bot.download_file(msg["voice"]["file_id"], './audio.ogg')
        subprocess.call(['ffmpeg', '-v', 'quiet', '-y', '-i', 'audio.ogg', 'audio.wav'])
        wav =  sr.AudioFile('audio.wav')
        with wav as source:
            recognizer_instance.pause_threshold = 3.0
            audio = recognizer_instance.listen(source)
            print('Elaborazione messaggio in corso...')

        try:
            text = recognizer_instance.recognize_google(audio, language="it-IT")
            print("Sono riuscito a comprendere: \n", text)
            bot.sendMessage(chat_id, "Messaggio: %s\n"%text)
        except Exception as e:
            print(e)

        bot.sendMessage(chat_id, "Il messaggio inviato è di tipo vocale")
        print('Utente: %s'%name)
        if lon > 1:
            print('Lunghezza audio: %d'%lon,'secondi')
        else:
            print('Lunghezza audio: %d'%lon,'secondo')

TOKEN = '573952513:AAHp0U1TP_zBo4b-I2EVk_Sgk4EUPp8cNaA'

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

print('Listening for inputs... ')

import time

while 1:
    time.sleep(10)


#DA RICORDARE

#bot.sendMessage(chat_id, 'ciao %s, sono un bot molto stupido!'%name)
#bot.sendMessage(chat_id, 'ho ricevuto questo : %s'%txt)
