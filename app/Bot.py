from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

from Config import Config
from CommandRouter import CommandRouter


class CocksizeBot:
    def __init__(self):
        config = Config()
        self.bot = Bot(token=config.telegram_token)
        self.storage = MemoryStorage()
        self.dispatcher = Dispatcher(bot=self.bot, storage=self.storage)
        self.router = CommandRouter(self.dispatcher)
        self.router.register()

    async def on_startup(self, dispatcher: Dispatcher):
        await self.router.register_commands_names()

