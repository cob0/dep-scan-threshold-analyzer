import logging

from log.formatter.iso8601 import ISO8601Formatter

LOGGER_LEVEL = logging.DEBUG
LOGGER_DATE_FORMAT = "%Y-%m-%d'T'%H:%M:%S.%f%z"
LOGGER_FORMAT = "{asctime} {levelname} {process} --- [{filename}] [thread-{thread}] {funcName}:{lineno}: {message}"


class Logger:
    instance: logging.Logger = None

    def __init__(self, level: int = LOGGER_LEVEL, date_format: str = LOGGER_DATE_FORMAT, format: str = LOGGER_FORMAT):
        if Logger.instance is None:
            if level:
                self.level = level
            if date_format:
                self.date_format = date_format
            if format:
                self.format = format
            self.instance = self._init_logger()

    def _init_logger(self) -> logging.Logger:
        logger = logging.getLogger()
        logger.setLevel(self.level)
        logger.addHandler(self._create_log_handler())
        return logger

    def _create_log_handler(self):
        handler = logging.StreamHandler()
        iso_8601_formatter = ISO8601Formatter(fmt=self.format, datefmt=self.date_format, style="{")
        handler.setFormatter(iso_8601_formatter)
        return handler


log = Logger().instance
