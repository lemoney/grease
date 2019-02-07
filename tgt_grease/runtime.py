"""GREASE Runtime Definition"""
from .types import CLASS
from .configuration import Configuration


class Runtime(CLASS):
    """responsible for running the E in GREASE (the engine)"""

    __config: Configuration
    
    def __init__(self, conf: Configuration):
        super(Runtime, self).__init__()
        self.__config = conf
        self.set_logger_name("runtime")
        self.log.debug("runtime startup")

    @property
    def config(self) -> Configuration:
        return self.__config

    @config.setter
    def config(self, c: Configuration):
        if not isinstance(c, Configuration):
            raise AttributeError("`config` must be of type tgt_grease.Configuration")
        self.__config = c
