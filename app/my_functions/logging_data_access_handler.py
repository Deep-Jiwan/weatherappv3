from dotenv import load_dotenv

#####################################################################
####################################################################
###         JSON_Handler
####################################################################

import json
# Assuming your JSON file is named data.json
file_path = "./config.json"

def read_json():
    with open(file_path, "r") as file:
        json_data = json.load(file)
    return json_data

def write_json(data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# Example usage:
#json_data = read_json(file_path)

#####################################################################
####################################################################
###         Logging_Handler
####################################################################

import logging
import asyncio
import telegram
import os

# Create logger for logging to file
f_logger = logging.getLogger('f_logger')
f_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/mylogs.log', mode='a')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
file_handler.setFormatter(file_formatter)
f_logger.addHandler(file_handler)

# Create logger for logging to console
c_logger = logging.getLogger('c_logger')
c_logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(file_formatter) # use the same string format
c_logger.addHandler(console_handler)

# Create logger for logging to telegram
t_logger = logging.getLogger('telegram_logger') 
        # Set up a handler to send messages to the Tele bot, custom
class TelegramHandler(logging.Handler):
    def __init__(self, bot_token, chat_id):
        super().__init__()
        self.bot_token = bot_token
        self.chat_id = chat_id

    def emit(self, record):
        log_entry = self.format(record)
        bot = telegram.Bot(token=self.bot_token)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        asyncio.run(self.send_telegram_message(bot, log_entry))
        
    async def send_telegram_message(self, bot, log_entry):
        await bot.send_message(chat_id=self.chat_id, text=log_entry)

# Initialize the bot and the handler
bot_token = os.getenv("tele_logger_token")
chat_id = os.getenv("tele_logger_chat_id")
telegram_handler = TelegramHandler(bot_token, chat_id)
t_logger.setLevel(logging.INFO)
telegram_handler.setFormatter(file_formatter)
t_logger.addHandler(telegram_handler)


def testlogger():
    '''
        This function will send a test message to all loggers to check functionality
    '''
    print("Testing the Logger")
    
    f_logger.debug('debug - file - working')
    f_logger.info('info - file - working')

    c_logger.debug('debug - console - working')
    c_logger.info('info - console - working')

    # These need to run with async.run
    #t_logger.debug('debug - telegram - working')
    #t_logger.info('info - telegram - working')

class log:
    class console:
        class message:
            def info(mes):
                c_logger.info(mes)
            def debug(mes):
                c_logger.debug(mes)
    class file:
        class message:
            def info(mes):
                f_logger.info(mes)
            def debug(mes):
                f_logger.debug(mes)
    class telegram:
        class message:
            def info(mes):
                t_logger.info(mes)
            def debug(mes):
                t_logger.debug(mes)
        
def lci(message):
    '''Log to log.console.message.info '''
    log.console.message.info(message)
    
def lcd(message):
    '''Log to log.console.message.debug '''
    log.console.message.debug(message)
    
def lfi(message):
    '''Log to log.file.message.info '''
    log.file.message.info(message)
    
def lfd(message):
    '''Log to log.file.message.debug '''
    log.file.message.debug(message)
    
def lti(message):
    '''Log to log.telegram.message.info '''
    log.telegram.message.info(message)

def ltd(message):
    '''Log to log.telegram.message.debug '''
    log.telegram.message.debug(message)
    
    
           
# Usage : log.console.message.debug("hi deep")
#         lcd("hi deep")


#####################################################################
####################################################################
###         Data_Access_Handler
####################################################################

def getData(cat,field):
    try:
        # get json data
        json_data = read_json()
        variable_value = json_data[cat][field]
        lfd(f"Json data accessed for {cat} -> {field}")
        return variable_value
    except KeyError:
        lfd("Variable was not found in JSON data.")
    except Exception as e:
        lfd(f'Error: {e}')

def getTelegramAPI():
    return getData("telegram","API")
def getWeatherAPI():
    return getData("weather","API")
def getWeatherRequestCount():
    return getData("weather","request_count")
def getWeatherTotalCount():
    return getData("weather","total_count")

def testHandler():
    print("JSON handler Test")
    print(getWeatherAPI())
    print(getWeatherRequestCount())
    print(getWeatherTotalCount())
    print(getTelegramAPI())
    
def setWeatherTotalCount(value):
    try: 
        data =read_json()
        data['weather']['total_count'] = value
        write_json(data)
    except Exception as e:
        lfd(f'Error: {e}')

def setAPIs():
    try: 
        data =read_json()
        data['weather']['API'] = os.getenv("weather_api_token")
        data['telegram']['API'] = os.getenv("tele_chat_bot_token")
        write_json(data)
    except Exception as e:
        lfd(f'Error: {e}')
        
def resetAPIs():
    # reset the environment variables
    os.environ['tele_logger_token'] = " "
    os.environ['tele_logger_chat_id'] = " "
    os.environ['weather_api_token'] = " "
    os.environ['tele_chat_bot_token'] = " "
    
def resetJSON():
    # reset the json variables
    data = read_json()
    data['weather']['API'] = "your-api-here"
    data['telegram']['API'] = "your-api-here"
    write_json(data)