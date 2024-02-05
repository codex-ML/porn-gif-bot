import os
import telebot
import requests
import random
from io import BytesIO

bot_token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(
      message,
    "Welcome to pron Gif bot \n"
    "This website may contain content of an adult nature. "
    "If you are easily offended or are under the age of 18, "
    "please exit now \n \n"
    "usage of bot :- \n"
    "/anal \n"
    "/doggystyle \n"
    "/threesome \n"
    "/erotic \n"
    "/cumshot \n"
    "/blowjob \n"
    "/masturbating \n"
    "/bdsm \n"
    "/cunnilingus \n"
    "/oral-sex \n"
    "/69 \n"
    "/bondage"
  )
  
# main function
@bot.message_handler(commands=['anal', 'doggystyle', 'threesome', 'cumshot', 'blowjob', 'masturbating', 'bdsm', 'cunnilingus', 'oral-sex', '69', 'bondage'])  # Add more commands as needed
def send_random_gif(message):
    command = message.text.split('/')[1]  # Extract the command from the message
    gif_data = get_random_gif_data(command)  # Get a random GIF data based on the command
    if gif_data:
        gif_url = gif_data['img_src']
        bot.send_animation(message.chat.id, gif_url)
    else:
        bot.reply_to(message, f"No GIFs found for the command /{command}.")

def get_random_gif_data(endpoint):
    response = requests.get(f"https://pron-api.onrender.com/{endpoint}")
    data = response.json()
    return random.choice(data) if data else None

bot.infinity_polling()

# 6161615496
# AAFtkF661taD-vRE3nAQ3UF5ggWMD68o2tg
# anal', 'doggystyle', 'threesome', 'erotic', 'cumshot',
# 'blowjob', 'masturbating', 'bdsm', 'cunnilingus', 'oral-sex',
# '69', 'bondage'
