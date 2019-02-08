"""definition for the attribute loader"""
from tgt_grease.types import CLASS
from tgt_grease import Configuration
import importlib


class AttributeLoader(CLASS):
    """the AttributeLoader class enables dynamic loading of modules

    Attributes:
          config (Configuration): active configuration instance being used to configure the Attr Loader

    """

    __config: Configuration

    def __init__(self, config: Configuration):
        super(AttributeLoader, self).__init__()
        self.__config = config
        self.set_logger_name("attrloader")

    def load(self, name: str) -> object:
        """load a specified exported "attribute of a class

        Args:
            name (str): name of attribute to load

        Returns:
            object: the attribute requested
            None: if not found a None

        Raises:
            ImportError: when there is an error importing the attribute
            TypeError: when there is an error importing the attribute
            AttributeError: when there is an error importing the attribute

        """
        if not isinstance(name, str) or not name:
            self.log.error(f"invalid attribute: {name}")
            raise ImportError("attribute name invalid")
        if name.startswith("__"):
            raise ImportError(f"AttributeLoader does not support private imports; name: {name} not acceptable")
        self.log.debug(f"attempting to load: {name}")
        for path in self.config.import_path:
            self.log.debug(f"searching path: {path} for attribute: {name}")
            try:
                search_module = importlib.import_module(str(path))
            except ImportError:
                self.log.error(f"Failed to import module [{path}]")
                continue
            if AttributeLoader.dir_contains(search_module, name):
                req = AttributeLoader.get_attr(search_module, str(name))
                if req is not None:
                    return req
                else:
                    raise ImportError(f"the requested attribute was not available: {path}.{name}")
        raise ImportError(f"{name} not found")

    @staticmethod
    def get_attr(obj, name, default=None):
        """Wrapper function for the built-in getattr function. Wrapper is required to mock the built-in function.
        Args:
            obj (Any object): Object you are searching for a named attribute for
            name (str): Name of the attribute you want to get from object
            default (Any object): Return value if attr name is not found in object. exception if no default is provided
        Returns:
            object: If an attribute is found it is returned. If it is not found, default is returned.
        """
        return getattr(obj, name, default)

    @staticmethod
    def dir_contains(module, cont_name):
        """Wrapper function for built in dir function. Needed for mocking.
        Args:
            module (module): Module you are searching, imported with importlib.import_module
            cont_name (str): Attribute (class) name you are searching the module for
        Returns:
            bool: Returns true if module contains name, else false.
        """
        return cont_name in dir(module)

    @property
    def config(self) -> Configuration:  # pylint: disable=C0111
        return self.__config

    @config.setter
    def config(self, c: Configuration):  # pylint: disable=C0111
        if not isinstance(c, Configuration):
            raise AttributeError("`config` must be of type tgt_grease.Configuration")
        self.__config = c
