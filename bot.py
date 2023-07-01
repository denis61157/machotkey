import pandas as pd
import time
import telebot
import requests
import os


TOKEN = '5863994706:AAGBKKYvKti107v27EJoBzexFq0biWdEdoo'
CHAT_ID = '-1001861124691'


def send_telegram_message(message, image_path):
    bot = telebot.TeleBot(TOKEN)
    with open(image_path, 'rb') as photo:
        bot.send_photo(chat_id=CHAT_ID, photo=photo, caption=message, parse_mode='Markdown')


df = pd.read_csv('data_for_HotKey_new.csv', delimiter=';')
while True:
    for index, row in df.iterrows():
        print(row['Action'])

        area = row['Area']
        action = row['Action']
        keystroke = row['Keystroke']
        image_url = row['Image']

        image_path = '/home/ubuntu/temp_image.jpg'
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(image_path, 'wb') as f:
                f.write(response.content)

        message = f"*{area}*  ---> *{keystroke}*" + "\n\n" + f"💻 `{action}`"

        send_telegram_message(message, image_path)

        os.remove(image_path)

        time.sleep(21600)
