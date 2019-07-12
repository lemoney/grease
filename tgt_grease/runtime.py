"""Defines the runtime object"""
from tgt_grease.types import CLASS
from .configuration import Configuration, DEFAULT_GREASE_DIR
from pymongo import MongoClient
import os
import json

MONGO_CONNECTION: MongoClient


class Runtime(CLASS):
    """The Runtime class acts as a sort of container maintaining more complex state

    Complex state management consists of things like the MongoDB connection and interacting with config

    """

    __config: Configuration = None

    def __init__(self):
        super(CLASS).__init__()
        self.set_logger_name(self.__class__.__name__)

    @property
    def mongo_client(self) -> MongoClient:
        global MONGO_CONNECTION
        if MONGO_CONNECTION is None:
            self.log.info("initializing MongoDB Connection")
            MONGO_CONNECTION = MongoClient(self.configuration.mongo_uri)
        return MONGO_CONNECTION

    @mongo_client.setter
    def mongo_client(self, client: MongoClient):
        global MONGO_CONNECTION
        if isinstance(client, MongoClient):
            MONGO_CONNECTION = client
        else:
            raise TypeError(f"type {type(client)} not allowed for Runtime.mongo_client expected for {type(MongoClient)}")

    @property
    def configuration(self) -> Configuration:
        if self.__config is None:
            self.log.debug("loading configuration")
            self.__config = Configuration()
            c: dict = dict()
            if os.getenv("GREASE_CONFIGURATION"):
                self.log.debug("loading configuration via `GREASE_CONFIGURATION` environment variable")
                with open(os.getenv("GREASE_CONFIGURATION"), "r") as fil:
                    c.update(json.load(fil))
            else:
                self.log.debug(f"loading configuration via default grease directory: {DEFAULT_GREASE_DIR}")
                with open(DEFAULT_GREASE_DIR, "r") as fil:
                    c.update(json.load(fil))
            self.__config.roles = c.get("roles")
            self.__config.prototypes = c.get("prototypes")
            self.__config.mongo_uri = c.get("mongo_uri")
            self.__config.grease_dir = c.get("grease_dir")
            self.__config.import_path = c.get("import_path")
            self.__config.resource_max_cpu = c.get("resource_max_cpu")
            self.__config.resource_max_mem = c.get("resource_max_mem")
            self.__config.sourcing_deduplication_threads = c.get("sourcing_deduplication_threads")
            self.__config.additional = c.get("additional")
        return self.__config

    @configuration.setter
    def configuration(self, config: Configuration):
        if isinstance(config, Configuration):
            self.__config = config
        else:
            raise TypeError(f"type {type(config)} not allowed for Runtime.configuration expected {type(Configuration)}")
