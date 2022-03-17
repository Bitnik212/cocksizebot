from dotenv import load_dotenv, dotenv_values
from pathlib import Path


class Config:
    def __init__(self):
        self.ENV_FILENAME = ".env"
        self.env_file_path = self.project_root_folder / self.ENV_FILENAME
        self.__env = dotenv_values(self.env_file_path)

    @property
    def project_root_folder(self) -> Path:
        return Path(".").absolute().parent

    @property
    def telegram_token(self) -> str:
        return self.__env['TELEGRAM_TOKEN']

    @property
    def inline_query_cache_time(self) -> int:
        return int(self.__env["INLINE_QUERY_CACHE_TIME"])

    @property
    def debug(self) -> bool:
        raw_string = self.__env["DEBUG"]
        print(raw_string)
        return raw_string.lower() == "true"
