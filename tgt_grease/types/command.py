"""definition of the core types class"""
from .base_class import CLASS
from abc import abstractmethod, ABCMeta


class Command(CLASS):
    """abstract base for grease commands"""

    __metadata__ = ABCMeta

    def __init__(self):
        super(Command, self).__init__()
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
