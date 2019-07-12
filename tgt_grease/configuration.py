"""engine configuration class definition"""
from dataclasses import dataclass, field
from typing import List, Dict
from collections import defaultdict


def default_import_path() -> list:
    """default module path for AttributeLoader"""
    return [
        "tgt_grease.commands",
        "tgt_grease.prototypes",
    ]


DEFAULT_GREASE_DIR = "/var/tmp/grease"


@dataclass
class Configuration(object):
    """configuration for a grease node"""
    roles: List[str] = field(default_factory=list)
    prototypes: List[str] = field(default_factory=list)
    mongo_uri: str = field(default="mongodb://localhost:27017", repr=False)
    grease_dir: str = field(default=DEFAULT_GREASE_DIR)
    import_path: List[str] = field(default_factory=default_import_path)
    resource_max_cpu: int = field(default=95)
    resource_max_mem: int = field(default=95)
    sourcing_deduplication_threads: int = field(default=150)
    additional: Dict[str, any] = field(default_factory=defaultdict)
