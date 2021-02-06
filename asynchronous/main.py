import asyncio
import logging
from aiohttp import web
from getwearher import get_weather
from models import Weather
from tortoise.contrib.aiohttp import register_tortoise

logging.basicConfig(level=logging.DEBUG)

### здесь работает #######
weather_list = asyncio.run(get_weather())
print( weather_list )


async def list_all(request, weather_list):
    pass
    #weather_list = asyncio.run(get_weather())
    #print(weather_list)
    #return web.Response(text=weather_list)
   

async def add_user(request):
    pass

app = web.Application()
app.add_routes([web.get("/", list_all), web.post("/user", add_user)])
register_tortoise(
    app, db_url="sqlite://:memory:", modules={"models": ["models"]}, generate_schemas=True
)


if __name__ == "__main__":
    web.run_app(app, port=5000)
    
