"""bridge command definition"""
from tgt_grease.types import Command


class Bridge(Command):
    """This command serves as the cluster management system"""

    def __init__(self, config):
        super(Bridge, self).__init__(config)
        self.set_logger_name("bridge")

    def execute(self, context: dict):
        """Cluster Management Command"""
        self.log.error(f"context: {context}")
