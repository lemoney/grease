"""definition of a scan data object"""
from dataclasses import dataclass, field
from datetime import datetime, timedelta


def expire_object() -> datetime:
    """generates an expiry time for an object"""
    return datetime.utcnow() + timedelta(days=1)


@dataclass
class ScanData(object):
    """storage of scan data from a scan"""
    source: str = field()
    config: str = field()
    origin_server: str = field()
    detection_server: str = field()
    data: dict = field(default_factory=dict)
    created: datetime = field(default_factory=datetime.utcnow)
    expiry: datetime = field(default_factory=expire_object)
