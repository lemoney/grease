"""bridge command definition"""
from tgt_grease.types import Command


class Bridge(Command):
    """This command serves as the cluster management system

    Args:
        config (tgt_grease.Configuration): configuration object to be used

    """

    def __init__(self, config):
        super(Bridge, self).__init__(config)
        self.set_logger_name("bridge")

    def execute(self, context: dict) -> bool:
        """Cluster Management Command"""
        self.log.error(f"context: {context}")
        return True
