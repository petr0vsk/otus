import asyncio
import logging
from aiohttp import web
import jinja2
import aiohttp_jinja2
from getwearher import get_weather, TOWN_LIST
from models import Weather
from tortoise.contrib.aiohttp import register_tortoise

logging.basicConfig(level=logging.DEBUG)

async def add_weather():
    '''
    # добавляем последний запрос по городам в БД
    '''
    weather_list = await get_weather() 
    for weather in weather_list: 
        await Weather.create(name = weather[0], temp = weather[1], pressure = weather[2], humidity = weather[3] )


# погода во всех городах
async def show_all(request):
    '''
    показывает содержимое всей базы данных погоды
    '''
    await add_weather()
    weather_all = await Weather.all()
    return web.Response(body=str(weather_all)) # возвращаем значения погоды из БД

async def resume_town(request):
    '''
    выводит последние значения по всем городам из списка TOWN_LIST
    '''
    await add_weather()

    offset  = await Weather.all().count()
    weather_context = await Weather.all().offset(offset- 5)  #  5 --> len(TOWN_LIST) 
    return web.Response(body=str(weather_context)) # возвращаем значения погоды из БД
    
async def town_page(request):
    '''
    выводит всю погоду по конкретному городу
    '''
    url_town = request.match_info['url_town']
    if url_town == str('delete'):
        await Weather.all().delete()
    rsp = await Weather.exists(name=url_town)
    if rsp:
        town_weather = await Weather.filter(name = url_town)
        return web.Response(body=str(town_weather)) 
    else:
        return web.Response(body=str(f"Такого города нет в базе данных, выберите из {str(TOWN_LIST)}, наберите delete для обнуления БД "))       
  


app = web.Application()
#aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
app.add_routes([web.get("/", resume_town)])
app.add_routes([web.get("/all", show_all)])
app.add_routes([web.get("/{url_town}", town_page)])
#app.add_routes([web.static('/static', 'static')])
register_tortoise(
    app, db_url='sqlite://db.sqlite3', modules={"models": ["models"]}, generate_schemas=True
    
)

if __name__ == "__main__":
    web.run_app(app, port=8080)
    
