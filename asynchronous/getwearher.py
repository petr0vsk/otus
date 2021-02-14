import aiohttp
import asyncio
import json
from loguru import logger
import random as rnd


TOWN_LIST = ['London', 'Moscow', 'Kyiv', 'Berlin', 'Barcelona']

async def get_session(town):
    async with aiohttp.ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={town}&appid=5e9e27c33f5ecafaf9083a17607da8f4'
        async with session.get(url) as resp:
            if resp.status == 200:
                logger.info(f'Starting get_weather for {town}')
                jsn = await resp.json()
                rnd.random() #!!! усилим эффект ассинхронности, отлкючить в продакшн !!! 
                town = jsn['name']
                temp = jsn['main']['temp']
                pressure = jsn['main']['pressure']
                humidity = jsn['main']['humidity']
                logger.info(f'Stopping get_weather for {town}')
            else:
                print(f'Ошибка на стороне сервера --> {resp.status}')    
    return [town, temp, pressure, humidity]

async def get_weather():

    coros = (
        get_session(town)
        for town in TOWN_LIST
    )
    result = await asyncio.gather(*coros)
    print(f'f_get_weather: {result} ')
    return result

if __name__ == "__main__":    

    results = asyncio.run(get_weather())
    print(results)
