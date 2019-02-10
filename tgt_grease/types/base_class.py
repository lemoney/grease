"""base class for all classes to implement in grease"""
import logging
from logging.config import fileConfig
import pkg_resources


class CLASS:
    """fundamental building block of all classes throughout GREASE

    Attributes:
        log (logging.Logger): log instance for class to operate

    """
    __log: logging.Logger

    def __init__(self):
        fileConfig(pkg_resources.resource_filename("tgt_grease", "logging.conf"))
        self.log = logging.getLogger("grease")

    @property
    def log(self) -> logging.Logger:
        """returns the commands active logger

        Returns:
            logging.Logger: active logger instance

        """
        return self.__log

    @log.setter
    def log(self, l: logging.Logger):
        self.__log = l

    def set_logger_name(self, name: str):
        """set the logger name

        Args:
            name (str): name of the logger underneath `grease`

        Note:
            this will set the logger to grease.`name`

        """
        self.log = logging.getLogger(f"{self.log.name}.{name}")
