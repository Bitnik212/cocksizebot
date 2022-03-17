from .Command import Command
from aiogram import types, Dispatcher


class HelloCommand(Command):
    def __init__(self, dispatcher: Dispatcher):
        super().__init__(dispatcher)
        self.names = [{'hello': "привет"}]

    @staticmethod
    async def handler(message: types.Message):
        await message.answer("Привет")
