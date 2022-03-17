from aiogram import Dispatcher, types
from aiogram.types import InputMessageContent


class Command:
    def __init__(self, dispatcher: Dispatcher):
        self.dispatcher: Dispatcher = dispatcher
        self.title: str or None = None
        """Название команды"""
        self.name: str or None = None
        """Уникальный путь команды. По нему вызываются команды"""
        self.description: str or None = None
        """Описание команды"""
        self.inline_support: bool = False
        """Поддерживается ли inline команда"""

    async def handler(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        pass

    def inline_handler(self, query: types.InlineQuery) -> InputMessageContent:
        pass

    def register(self, handler, commands: list[str]):
        self.dispatcher.register_message_handler(callback=handler, commands=commands)

    def register_inline(self, inline_handler):
        self.dispatcher.register_inline_handler(callback=inline_handler)

