from aiogram import Dispatcher, types


class Command:
    def __init__(self, dispatcher: Dispatcher):
        self.dispatcher: Dispatcher = dispatcher
        self.names: list[dict[str, str]] or None = None

    def register(self, handler, commands: list[str]):
        self.dispatcher.register_message_handler(callback=handler, commands=commands)

    @staticmethod
    async def handler(**kwargs):
        pass

    @staticmethod
    def get_command_names(command_names: list[dict[str, str]]) -> list[str]:
        founded_command_names: list[str] = []
        for command_name in command_names:
            for name in command_name.keys():
                founded_command_names.append(name)
        return founded_command_names
