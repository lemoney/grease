"""definition of the core command class"""
from .base_class import CLASS
from abc import abstractmethod, ABCMeta


class Command(CLASS):
    """abstract base for grease commands"""

    __metadata__ = ABCMeta

    def __init__(self):
        super().__init__()
        self.set_logger_name("prototype")

    def safe_execute(self, context: dict):
        """safely execute prototype to ensure thread doesn't crash

        Args:
            context (dict): command context

        """
        try:
            self.execute(context)
        except BaseException as e:
            self.log.critical(f"failed to execute command due to {type(e)}")

    def execute(self, context: dict):
        """command prototype (user main method effectively)

        Args:
            context (dict): command context object

        """
        if int(context.get("loop", "0")) == 0:
            while True:
                self.run(context)
        else:
            i = 0
            m = int(context.get("loop"))
            while i <= m:
                self.run(context)

    @abstractmethod
    def run(self, context: dict):
        """user defined prototype to execute"""
