import requests
from app_error_checking import *

API_KEY = getWeatherAPI()
total_count = getWeatherTotalCount() # retrive from config file
request_count = 0
tele_api = getTelegramAPI()

def getWeatherInfo(CITY):
    '''
        A function to get weather data json and return it. Pass city to search for \n
        Ctrl + Click to know more
    '''
    # basic url for accessing the API
    url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}'
    
    # retun and process the json file with the weather data
    response = requests.get(url)
    if checkResponse(response):
        global request_count
        request_count = request_count+1
        lfd(f'API request made # {request_count} ')
    weather_data = response.json()
    
    # return weather data in json format
    return weather_data

def printWeatherInfo(city):
    '''
        A function to directly print the weather data of a given city. \n
        It will also return the string that it prints \n
        Ctrl + Click to know more
    '''
    # get the weather data json
    weather_data = getWeatherInfo(city)
    
    # store the basic weather information.
    try:
        temperature_c = weather_data['current']['temp_c']
        # access the city using the json data so that which city data being shown is apparent.
        city = weather_data['location']['name']
        status = weather_data['current']['condition']['text']
        feellike_temp = weather_data['current']['feelslike_c']
        local_time = weather_data['location']['localtime']
        country = weather_data['location']['country']
        humidity = weather_data['current']['humidity']
        
        # Contstruct a string that give weather information and print it
        infop1 = f'Local Time: {local_time} Hrs\n\nIt is currently {status} in {city}, {country} with a temperature of {temperature_c}{chr(176)}C.'
        infop2 = f'\n\nTemperature feels like {feellike_temp}{chr(176)}C.'
        infop3 = f'\nHumidity is {humidity}%'
        info = infop1 + infop2 + infop3
        print(info)
        return info
    except Exception as e:
        print(f'Error: {e}')
        lfd(f'Error: {e}')
        error_code = weather_data['error']['code']
        error_message = weather_data['error']['message']
        if(error_code==1006):
            lfd(f'Error code: {error_code} -> ' + error_message )
            return "I dont think that location exists!"
        else:
            lfd(f'Error code: {error_code} -> ' + error_message )
            return "Service temporarily unavailable :("

def getWeather(city):
    '''
        A function that returns a dictionary with 3 basic weather infromation. \n
        Ctrl + Click to know more
    '''
    # this basically converts the json into a dictionary for simpler access.
    # add more info to the dictionary as needed.
    weather_data = getWeatherInfo(city) # this will handle api count
    temprature_c = weather_data['current']['temp_c']
    city = weather_data['location']['name']
    status = weather_data['current']['condition']['text']
    
    weather_info  = {
        "temp": temprature_c,
        "city": city,
        "status": status
    }# access using [], weather_info["temp"] returns temp
    
    # return the info as a python dictionary
    return weather_info
    
def isCondition(city,condition):
    '''
        A function to check the condition/Status of a city \n
        Returns True / False
    '''
    weather_info = getWeather(city) # will handle api count
    status = weather_info['status'].lower()
    
    if (status==condition.lower()):
        return True
    else:
        return False

def basicTest():
    lfd("API test initiated")
    print("----Testing the Service now----")
    printWeatherInfo('london')
    print('Testing the Loggers')
    testlogger()
    print('Testing the JSON handler')
    testHandler()
    print("----Test completed----")
    lfd("API test completed")

def endService():
    print("Terminating the service")
    lfi("Aplication Terminated")
    lfi(f"Total Requests this session #{request_count}")
    global total_count
    total_count = total_count + request_count
    setWeatherTotalCount(total_count)
    lfi(f"Total Requests since begining of time #{total_count}")
    # resetAPIs() - disabled since we dont need to reset env vars inside docker
    resetJSON() # diable if you are dont want to reload the apis every time
    lfi(f"Clearing the environment variables (API Keys) and in the json")

'''
basicTest()
print('Powered by https://www.weatherapi.com/ WeatherAPI.com')
'''