from __future__ import annotations

from typing import TYPE_CHECKING, Union

from prettytable import PrettyTable

from waddles_cli.helpers.decorators import requires_config

if TYPE_CHECKING:  # pragma: no cover
    from waddles_cli.models import config


@requires_config
def show(config_output: Union[config.ConfigLoader, config.Database]):
    """ Return the active global_config for this user.

    :param config_output: All the global_config values available
    """
    for config_key, config_value in config_output.dict_object.items():
        print(f"Returning the configured values for {config_key}".format(config_key=config_key.capitalize()))
        table = PrettyTable(["Option", "Value"])
        for key, value in config_value.items():
            table.add_row([key, value])
        print(table)
    return True
