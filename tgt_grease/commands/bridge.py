from tgt_grease.types import Command


class Bridge(Command):
    
    def __init__(self):
        super(Bridge, self).__init__()
        self.set_logger_name("bridge")

    def execute(self, context: dict):
        """Cluster Management Command"""
        self.log.error(f"context: {context}")
