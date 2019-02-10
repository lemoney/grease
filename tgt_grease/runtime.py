"""GREASE Runtime Definition"""
from .types import CLASS, Command
from .util import AttributeLoader
from .configuration import Configuration
from typing import Dict, List, Union


class Runtime(CLASS):
    """responsible for running the E in GREASE (the engine)"""

    __config: Configuration
    __context: Dict[str, Union[str, List[str]]]
    __loader: AttributeLoader

    def __init__(self, conf: Configuration, context: Dict[str, Union[str, List[str]]]):
        super(Runtime, self).__init__()
        self.__config = conf
        self.__context = context
        self.__loader = AttributeLoader(self.config)
        self.set_logger_name("runtime")
        self.log.debug("runtime startup")

    def execute(self, cmd: str):
        """execute the command from the CLI

        Args:
            cmd (str): command to execute

        Returns:
            None: should execute cleanly

        Raises:
            RuntimeError: if the command throws an exception or fails execution

        """
        try:
            command = self.loader.load(cmd)  # type: Command
            command()
            command.safe_execute(self.context)
        except ImportError as e:
            raise RuntimeError(f"command failed due to error: {e}")
        except TypeError as e:
            raise RuntimeError(f"command failed due to error: {e}")
        except AttributeError as e:
            raise RuntimeError(f"command failed due to error: {e}")

    @property
    def config(self) -> Configuration:  # pylint: disable=C0111
        return self.__config

    @config.setter
    def config(self, c: Configuration):  # pylint: disable=C0111
        if not isinstance(c, Configuration):
            raise AttributeError("`config` must be of type tgt_grease.Configuration")
        self.__config = c

    @property
    def context(self) -> Dict[str, any]:  # pylint: disable=C0111
        return self.__context

    @context.setter
    def context(self, ctx: Dict[str, any]):  # pylint: disable=C0111
        if not isinstance(ctx, dict):
            raise AttributeError("`context` must be of type dict")
        self.__context = ctx

    @property
    def loader(self) -> AttributeLoader:
        return self.__loader

    @loader.setter
    def loader(self, l: AttributeLoader):
        if not isinstance(l, AttributeLoader):
            raise AttributeError("`loader` must be type tgt_grease.util.AttributeLoader")
        self.__loader = l

    @staticmethod
    def parse_data_args(data: List[str], sep: str) -> Dict[str, Union[str, List[str]]]:
        """This is useful for transforming a list of key/values into a dictionary
        EX::
            ["key1=val1", "key2=val2", "key3=val3"] -> {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
            ["key1=val1", "key2=val2", "key3=val3,val4"] -> {'key1': 'val1', 'key2': 'val2', 'key3': ['val3', 'val4']}
            ["key1=val1", "key2=val2", "key3=val3, val4"] -> {'key1': 'val1', 'key2': 'val2', 'key3': ['val3', 'val4']}
        Args:
            data (List[str]): List to parse
            sep (str): separator for the string to parse by
        Returns:
            dict: key/value pairs from data list
        Note:
            Parse failures yield ValueErrors
        """
        final = {}
        for elem in data:
            kv = elem.split(sep)
            if len(kv) != 2:
                raise ValueError(
                    f'could not split key value pair properly, please use = as separator::{elem} generated {kv}')
            if ',' in kv[1] and '\,' not in kv[1]:
                final[kv[0]] = kv[1].split(',')
            else:
                final[kv[0]] = kv[1].replace('\,', ',')
        return final
