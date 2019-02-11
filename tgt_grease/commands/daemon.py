"""GREASE Daemon Runtime definition"""
from tgt_grease.types import Command


class Daemon(Command):
    """This command is the daemon

    This command attempts to connect to MongoDB, join/create the GREASE cluster, perform cluster operations

    Args:
        config (tgt_grease.Configuration): configuration object to be used

    """

    def __init__(self, config):
        super(Daemon, self).__init__(config)
        self.set_logger_name("daemon")

    def execute(self, context: dict):
        self.log.critical(context)
        process = context.get('process')
        if process == 'start':
            raise NotImplementedError(f"process {process} is not implemented")
        elif process == 'stop':
            raise NotImplementedError(f"process {process} is not implemented")
        elif process == 'restart':
            raise NotImplementedError(f"process {process} is not implemented")
        elif process == 'install':
            raise NotImplementedError(f"process {process} is not implemented")
        elif process == 'run':
            raise NotImplementedError(f"process {process} is not implemented")
        else:
            raise NotImplementedError(f"process {process} is not implemented")
