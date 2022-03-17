from random import Random

from aiogram import Dispatcher, types
from aiogram.types import InputMessageContent

from app.commands.Command import Command


class MyCockSizeCommand(Command):
    def __init__(self, dispatcher: Dispatcher):
        super().__init__(dispatcher)
        self.MAX_SIZE = 40
        self.MIN_SIZE = 4
        self.name = "mycocksize"
        self.title = "My cock size"
        self.description = "Share your cock size"
        self.inline_support = True

    async def handler(self, message: types.Message):
        await message.answer(self.my_cock_size)

    def inline_handler(self, query: types.InlineQuery) -> InputMessageContent:
        return InputMessageContent(message_text=self.my_cock_size)

    @property
    def my_cock_size(self) -> str:
        cock_size = str(Random().randint(self.MIN_SIZE, self.MAX_SIZE))
        return "My cock size is " + cock_size + " cm"
