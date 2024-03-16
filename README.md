# weatherappv3
A telegram bot that can tell you the weather of any given location

Pre-requirements:
- Basic telegram bot api knowledge
- A bot token / api from botfather
- Weather api from https://www.weatherapi.com/WeatherAPI.com

How to use:

Local Dev:
1. Clone the repo
2. Create a file .env for environment variables using the template
3. Add your api keys for relevant features
4. Install the requirements
      ` pip install --no-cache-dir -r requirements.txt`
6. Run the app/main.py


Docker Container
1. Pull the image
   `docker pull dmjiwan/weatherappv3:latest`
   `docker pull dmjiwan/weatherappv3:arm64` for arm based systems ( Raspberry Pi )
   OR
    `github`
3. Run the image in a container while making sure to add the following environment variables and associated api keys
   `tele_logger_token`
   `tele_logger_chat_id`
   `weather_api_token`
   `tele_chat_bot_token`
4. The service is ready to use



Powered by https://www.weatherapi.com/ WeatherAPI.com
