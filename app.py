
import logging
from logging.handlers import RotatingFileHandler

from aiogram.utils import executor
from create_bot import dp


rfh = RotatingFileHandler(
    filename="bot_log.log",
    mode='a',
    maxBytes=5*1024*1024,
    backupCount=2,
    encoding=None
)

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
                    datefmt='%H:%M:%S',
                    handlers=[
                        rfh
                   ]
                   )

async def on_startup(_):
    print("START ONLINE BOT")

from handlers import main_meny, weather, currency_converter, random_pictures

weather.register_handler_weather(dp)
currency_converter.register_handler_currency_convertor(dp)
random_pictures.register_handler_random_picture(dp)
main_meny.register_handler_main_meny(dp)

if __name__ == '__main__':
    logging.info("start bot")
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
