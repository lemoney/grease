"""job configuration definition"""
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class JobConfig(object):
    """defines the configuration of a grease job"""
    name: str = field()
    command: str = field()
    scanner: str = field()
    scan_config: dict = field()
    deduplication: float = field()
    logic: Dict[str, List[Dict[str, str]]] = field()
    deduplication_fields: List[str] = field(default_factory=list)
