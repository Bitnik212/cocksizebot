from aiogram import Dispatcher, types

from commands.Command import Command
from commands.MyCockSizeCommand import MyCockSizeCommand
from commands.HelloCommand import HelloCommand


class CommandRouter:

    def __init__(self, dispatcher: Dispatcher):
        self.dispatcher: Dispatcher = dispatcher
        self.commands: list[id(Command)] = [HelloCommand, MyCockSizeCommand]
        self.commands_names: list[types.BotCommand] = []

    def register(self):
        """
        Регистрация команд
        """
        for command in self.commands:
            inited_command = command(self.dispatcher)
            inited_command.register(inited_command.handler, Command.get_command_names(inited_command.names))
            for name in inited_command.names:
                self.commands_names.append(types.BotCommand("".join(list(name.keys())), "".join(list(name.values()))))

    async def register_commands_names(self):
        """
        Регистрация команд бота
        """
        await self.dispatcher.bot.set_my_commands(self.commands_names)
