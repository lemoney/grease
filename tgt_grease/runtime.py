"""GREASE Runtime Definition"""
from .types import CLASS


class Runtime(CLASS):
    """responsible for running the E in GREASE (the engine)"""
    
    def __init__(self):
        super(Runtime, self).__init__()
        self.set_logger_name("runtime")
        self.log.debug("runtime startup")
