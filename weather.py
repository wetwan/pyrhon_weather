from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_waether(city= 'osogbo'):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == '__main__':
    print('\n*** Get current weather***\n')
    
    city =input('\n Please enter your city: ')

    if not bool(city.strip()):
        city = 'osogbo'
        
    weather_data = get_waether(city)

    print('\n')
    pprint(weather_data)
    