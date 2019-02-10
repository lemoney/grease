"""definition of the core Prototype class"""
from .base_class import CLASS
from abc import abstractmethod, ABCMeta


class Prototype(CLASS):
    """abstract base for grease commands

    Note:
        providing `loop` in context will execute the prototype that many times

    """

    __metadata__ = ABCMeta

    def __init__(self):
        super().__init__()
        self.set_logger_name("prototype")

    def safe_execute(self, context: dict):
        """safely execute prototype to ensure thread doesn't crash

        Args:
            context (dict): context for execution

        """
        try:
            self.execute(context)
        except BaseException as e:
            self.log.critical(f"failed to execute prototype {self.__class__.__name__} due to {type(e)}")

    def execute(self, context: dict):
        """prototype main loop

        Args:
            context (dict): context object

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
        """user defined prototype to execute forever or for as many 'loop's as provided"""
