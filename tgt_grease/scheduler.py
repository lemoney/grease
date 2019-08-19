"""defines the scheduler"""
from tgt_grease.types import CLASS, ScanData
from tgt_grease import Runtime
from typing import List
import pinject


class Scheduler(CLASS):
    """The scheduler is responsible for explaining to nodes what work they have to do"""

    __runtime: Runtime

    def __init__(self):
        super().__init__()
        self.__runtime = pinject.new_object_graph().provide(Runtime)

    def schedule_for_detection(self, data: List[ScanData]):
        for d in data:
            self.runtime.mongo_database.get_collection("scan_data").insert(d)

    @property
    def runtime(self):
        return self.__runtime

    @runtime.setter
    def runtime(self, r: Runtime):
        if isinstance(r, Runtime):
            self.__runtime = r
        else:
            raise TypeError(f"type {type(r)} not allowed for Scheduler.runtime expected {type(Runtime)}")
