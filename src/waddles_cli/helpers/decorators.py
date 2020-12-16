from typing import Callable
from argparse import Namespace

from waddles_cli.models.config import ConfigLoader


def requires_config(function: Callable, content: str = None):
    """ Load the required configuration that will be used by the operations.

    :param content: The configurations you want to retrieve
    :param function: The function you want to execute.
    Example::
        @requires_config
        def func():
            pass

        @requires_config(content="database")
        def func2():
            pass
    """

    def wrapper(inner_content: str = None, params: Namespace = None):
        con = inner_content or content
        config = ConfigLoader()
        if params:
            if con:
                return function(params=params, config_output=getattr(config, con))
            else:
                return function(params=params, config_output=config)
        else:
            if con:
                return function(config_output=getattr(config, con))
            else:
                return function(config_output=config)

    return wrapper
