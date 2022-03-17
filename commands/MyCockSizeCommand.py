from random import Random

from aiogram import Dispatcher, types

from .Command import Command


class MyCockSizeCommand(Command):
    def __init__(self, dispatcher: Dispatcher):
        super().__init__(dispatcher)
        self.names = [{'mycocksize': "My cock size"}]

    @staticmethod
    async def handler(message: types.Message):
        random = Random(10)
        await message.answer("My cock size is "+str(random.randint(1, 100)))


