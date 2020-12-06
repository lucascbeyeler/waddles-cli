from typing import Callable

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

    def wrapper(inner_content: str = None):
        con = inner_content or content
        config = ConfigLoader()
        if con:
            return function(getattr(config, con))
        else:
            return function(config)

    return wrapper
