"""definition of the core types class"""
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
        """safely execute types to ensure thread doesn't crash

        Args:
            context (dict): types context

        """
        try:
            self.execute(context)
        except BaseException as e:
            self.log.critical(f"failed to execute command due to {type(e).__name__}")

    @abstractmethod
    def execute(self, context: dict):
        """types execution (user main method effectively)

        Args:
            context (dict): types context object

        """

    @property
    def config(self) -> Configuration:  # pylint: disable=C0111
        return self.__config

    @config.setter
    def config(self, c: Configuration):  # pylint: disable=C0111
        if not isinstance(c, Configuration):
            raise AttributeError("`config` must be of type tgt_grease.Configuration")
        self.__config = c
