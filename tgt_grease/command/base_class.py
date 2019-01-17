"""base class for all classes to implement in grease"""
import logging


class CLASS:
    """fundamental building block of all classes throughout GREASE

    Attributes:
        log (logging.Logger): log instance for class to operate

    """
    __log: logging.Logger

    def __init__(self):
        self.log = logging.getLogger("grease")

    @property
    def log(self) -> logging.Logger:
        return self.__log

    @log.setter
    def log(self, l: logging.Logger):
        self.__log = l
