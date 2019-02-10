"""GREASE Daemon Runtime definition"""
from tgt_grease.types import Command


class Daemon(Command):
    """This command is the daemon

    This command attempts to connect to MongoDB, join/create the GREASE cluster, perform cluster operations

    """

    def __init__(self, config):
        super(Daemon, self).__init__(config)
        self.set_logger_name("daemon")

    def execute(self, context: dict):
        self.log.critical(self.config.grease_dir)
        self.log.critical(context)
