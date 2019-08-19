"""GREASE Daemon Runtime definition"""
from tgt_grease.types import Command
from tgt_grease import Runtime
from tgt_grease.util import start_daemon, stop_daemon, restart_daemon, install_daemon
import pinject


class Daemon(Command):
    """This command is the daemon

    This command attempts to connect to MongoDB, join/create the GREASE cluster, perform cluster operations

    Args:
        config (tgt_grease.Configuration): configuration object to be used

    """

    __runtime: Runtime

    def __init__(self, config):
        super(Daemon, self).__init__(config)
        self.set_logger_name("daemon")
        self.__runtime = pinject.new_object_graph().provide(Runtime)

    def execute(self, context: dict) -> bool:
        process = context.get('process')
        if process == 'start':
            return start_daemon()
        elif process == 'stop':
            return stop_daemon()
        elif process == 'restart':
            return restart_daemon()
        elif process == 'install':
            return install_daemon()
        elif process == 'run':
            if context.get('loop'):
                i = 0
                loops = int(context.get('loop'))
                while i < loops:
                    self.run()
                    i += 1
            else:
                try:
                    while True:
                        self.run()
                except KeyboardInterrupt:
                    return True
                except BaseException as e:
                    self.log.critical(f"got exception: {type(e).__name__} during daemon run")
                    raise RuntimeError(f"got exception {type(e).__name__}")
        else:
            raise NotImplementedError(f"process {process} is not implemented")

    def run(self):
        """run the daemon process for a single iteration"""
        raise NotImplementedError("process run is not implemented")

    @property
    def runtime(self) -> Runtime:
        return self.__runtime

    @runtime.setter
    def runtime(self, r: Runtime):
        if isinstance(r, Runtime):
            self.__runtime = r
        else:
            raise TypeError(f"type {type(r)} not allowed for Daemon.runtime expected {type(Runtime)}")
