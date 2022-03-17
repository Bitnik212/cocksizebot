from aiogram.utils import executor
from Bot import CocksizeBot


if __name__ == '__main__':
    bot = CocksizeBot()
    executor.start_polling(bot.dispatcher, on_startup=bot.on_startup)
