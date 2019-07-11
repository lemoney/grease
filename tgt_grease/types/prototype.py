"""definition of the core Prototype class"""
from .command import Command
from abc import abstractmethod, ABCMeta
from tgt_grease.configuration import Configuration


class Prototype(Command):
    """abstract base for grease commands

    Note:
        providing `loop` in context will execute the prototype that many times

    """

    __metadata__ = ABCMeta

    def __init__(self, config: Configuration):
        super().__init__(config)
        self.set_logger_name(f"prototype.{self.__class__.__name__}")

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
                i += 1

    @abstractmethod
    def run(self, context: dict):
        """user defined prototype to execute forever or for as many 'loop's as provided"""
