"""definition of the core Command class"""
from .base_class import CLASS
from tgt_grease import Configuration
from abc import abstractmethod, ABCMeta


class Command(CLASS):
    """abstract base for grease commands"""

    __metadata__ = ABCMeta
    __config: Configuration

    def __init__(self, config: Configuration):
        super(Command, self).__init__()
        self.__config = config
        self.set_logger_name("command")

    def safe_execute(self, context: dict):
        """safely execute the command to ensure thread doesn't crash

        Args:
            context (dict): context object to execute with

        """
        try:
            self.execute(context)
        except BaseException as e:
            self.log.critical(f"failed to execute command due to {type(e).__name__}")

    @abstractmethod
    def execute(self, context: dict) -> bool:
        """user code to execute upon trigger

        Args:
            context (dict): context for command

        Returns:
            bool: if the command succeeded then True else False

        """

    @property
    def config(self) -> Configuration:
        """returns the commands active configuration

        Returns:
            tgt_grease.Configuration: active command configuration

        :noindex:
        """
        return self.__config

    @config.setter
    def config(self, c: Configuration):
        if not isinstance(c, Configuration):
            raise AttributeError("`config` must be of type tgt_grease.Configuration")
        self.__config = c
