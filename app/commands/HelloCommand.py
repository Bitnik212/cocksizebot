from .Command import Command
from aiogram import types, Dispatcher


class HelloCommand(Command):

    def __init__(self, dispatcher: Dispatcher):
        super().__init__(dispatcher)
        self.name = "hello"
        self.description = "привет"

    async def handler(self, message: types.Message):
        await message.answer("Привет")
