
import requests  
from loguru import logger

Town = 'Moscow'

def get_weather(town):
    '''
    получаем погоду с сайта openweather.org по 
    городам, указанным в TOWN_LIST
    '''
    logger.info(f'Starting get_weather for {town}')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={town}&appid=5e9e27c33f5ecafaf9083a17607da8f4'
    response = requests.get(url)
    if response.status_code == 200:  
        jsn = response.json()
        temp = jsn['main']['temp']
        pressure = jsn['main']['pressure']
        humidity = jsn['main']['humidity']
        logger.info(f'Stopping get_weather for {town}')
    else:
                print(f'Ошибка на стороне сервера --> {response.status_code }')  
    return [town, temp, pressure, humidity]           


if __name__ == "__main__":    

    results = (get_weather(Town))
    print(results)        
