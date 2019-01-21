"""definition of the core command class"""
from .base_class import CLASS
import logging
from abc import abstractmethod, ABCMeta


class Command(CLASS):
    """abstract base for grease commands"""

    __metadata__ = ABCMeta

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger("grease.command")

    def safe_execute(self, context: dict):
        """safely execute command to ensure thread doesn't crash

        Args:
            context (dict): command context

        """
        try:
            self.execute(context)
        except BaseException as e:
            self.log.critical(f"failed to execute command due to {type(e)}")

    @abstractmethod
    def execute(self, context: dict):
        """command execution (user main method effectively)

        Args:
            context (dict): command context object

        """
