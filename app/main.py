import logging
from telegram import Update
from telegram.ext import filters, CommandHandler, ApplicationBuilder, MessageHandler , ContextTypes
from weatherupdate import *


# logging for the telegram BOT - Different from app logging
logging.basicConfig(
    # handles telegram bot side logging and debug
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lfd(f'Service requested by user:{update.effective_user} chatid:{update.effective_chat.id} ')
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, Welcome to my Weather App!")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Enter the city you wish to get a weather update for!")

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter the city:")
    
async def get_weather(update: Update, context):
    task = update.message.text
    reply = printWeatherInfo(task)
    lfd(f'| TERMINATED | Service requested by user:{update.effective_user} chatid:{update.effective_chat.id} ')
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)

if __name__ == '__main__':
    basicTest()
    application = ApplicationBuilder().token(tele_api).build()
    
    start_handler = CommandHandler('start', start)
    weather_handler = CommandHandler('weather', weather)
    get_weather_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), callback=get_weather)
    
    application.add_handler(start_handler)
    application.add_handler(weather_handler)
    application.add_handler(get_weather_handler)
    lfi("Aplication Started")
    application.run_polling()
    endService()
'''
    TO DO     
         
    formatted messages
    
    telegram logger check async issue
    
    dockerize
    
    deploy
    

    
    humidity and what to do with the weather.
    
    website implementation
    
    subscribe to service
    
    
    
'''