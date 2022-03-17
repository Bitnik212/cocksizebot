from aiogram import Dispatcher, types

from app.handlers.InlineHandler import InlineHandler
from commands.Command import Command
from commands.MyCockSizeCommand import MyCockSizeCommand
from commands.HelloCommand import HelloCommand


class CommandRouter:

    def __init__(self, dispatcher: Dispatcher):
        self.dispatcher: Dispatcher = dispatcher
        self.commands: list[id(Command)] = [HelloCommand, MyCockSizeCommand]
        self.registered_commands: list[id(Command)] = []
        self.commands_names: list[types.BotCommand] = []
        self.inline_handler = InlineHandler(self.registered_commands).handler

    def register_commands(self):
        for command in self.commands:
            inited_command = command(self.dispatcher)
            inited_command.register(
                handler=inited_command.handler,
                commands=inited_command.name)
            self.registered_commands.append(inited_command)
            self.commands_names.append(types.BotCommand(inited_command.name, inited_command.description))

    async def register_commands_names(self):
        """
        Регистрация команд бота так, чтобы их можно было увидеть в контекстном меню
        """
        await self.dispatcher.bot.set_my_commands(self.commands_names)

    def register_inline_commands(self):
        self.dispatcher.register_inline_handler(callback=self.inline_handler)
