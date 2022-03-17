import hashlib

from aiogram import types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent

from app.Config import Config
from app.commands.Command import Command


class InlineHandler:

    def __init__(self, commands: list[id(Command)]):
        self.__commands: list[id(Command)] = commands
        self.config = Config()

    async def handler(self, query: types.InlineQuery):
        if query.query == "/":
            await query.bot.answer_inline_query(
                query.id,
                results=self.get_commands_names_result(query),
                cache_time=self.config.inline_query_cache_time,
                is_personal=True
            )

    def get_commands_names_result(self, query: types.InlineQuery) -> list[InlineQueryResultArticle]:
        """
        Получение готового ответа для пустого запроса. Список всех команд.
        :return: Список всех команд
        """
        result: list[InlineQueryResultArticle] = []
        for command in self.__commands:
            title: str = command.title
            if command.inline_support:
                result.append(InlineQueryResultArticle(
                    id=hashlib.md5(title.encode()).hexdigest(),
                    title=title,
                    description=command.description,
                    input_message_content=command.inline_handler(query)
                ))
        if not result:
            result.append(InlineQueryResultArticle(
                    id="1",
                    title="Нет результатов",
                    input_message_content=InputTextMessageContent("Нет результатов")
                ))
        return result
