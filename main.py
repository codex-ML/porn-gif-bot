import telebot
import requests
from telebot import types

# Initialize your bot token
bot_token = '6472433409:AAH3IKMVV__PTJvG4CfNoNvUvvlEYcsmWFA'
bot = telebot.TeleBot(bot_token, parse_mode=None)


# Define the function to handle button clicks
@bot.message_handler(commands=["gif"])
def send_gif(message):
  # Request a random GIF from the API
  api_url = 'https://gifapi-xx7w.onrender.com/random'
  response = requests.get(api_url)
  if response.status_code == 200:
    gif_data = response.json()
    gif_url = gif_data['img_src']
    # Send the GIF to the user
    bot.send_animation(message.chat.id, gif_url)
  else:
    bot.send_message(message.chat.id,
                     "Failed to fetch GIF. Please try again later.")


# Define the handler for the /start command
@bot.message_handler(commands=['start'])
def start_handler(message):
  # Send a message with the command to receive a random GIF
  markup = types.ReplyKeyboardMarkup(row_width=2)
  btn_gif = types.KeyboardButton('/gif')
  btn_dice = types.KeyboardButton('/dice')
  markup.add(btn_gif, btn_dice)
  bot.send_message(message.chat.id,
                   "Send the /gif command to receive a random GIF.",
                   reply_markup=markup)


@bot.message_handler(commands=['dice'])
def start_handler(message):
  bot.send_dice(message.chat.id)


# Start the bot
bot.polling()
