import logging

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from app.Config import Config
from app.CommandRouter import CommandRouter


class CocksizeBot:
    def __init__(self):
        self.__config = Config()
        self.init_logging()
        self.bot = Bot(token=self.__config.telegram_token)
        self.storage = MemoryStorage()
        self.dispatcher = Dispatcher(bot=self.bot, storage=self.storage)
        self.router = CommandRouter(self.dispatcher)
        self.router.register_commands()
        self.router.register_inline_commands()

    async def on_startup(self, dispatcher: Dispatcher):
        await self.router.register_commands_names()

    def init_logging(self):
        if self.__config.debug:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    bot = CocksizeBot()
    executor.start_polling(bot.dispatcher, on_startup=bot.on_startup)
