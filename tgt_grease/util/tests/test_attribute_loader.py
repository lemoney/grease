from tgt_grease import Configuration
from tgt_grease.util import AttributeLoader
from collections import defaultdict
import pytest


def test_valid_import():
    config = Configuration(import_path=["collections"])
    attr_loader = AttributeLoader(config)
    default_dict = attr_loader.load("defaultdict")  # type: defaultdict
    m = default_dict()
    assert isinstance(m, defaultdict)


def test_invalid_import():
    config = Configuration(import_path=["collections"])
    attr_loader = AttributeLoader(config)
    with pytest.raises(ImportError):
        attr_loader.load("does_not_exist")  # type: defaultdict


def test_invalid_attribute_name():
    config = Configuration(import_path=["collections"])
    attr_loader = AttributeLoader(config)
    with pytest.raises(ImportError):
        attr_loader.load("__defaultdict")  # type: defaultdict
