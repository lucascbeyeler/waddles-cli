from __future__ import annotations

from typing import TYPE_CHECKING

from waddles_cli.helpers.decorators import requires_config
from waddles_cli.constants.keywords import BACKUP_PATH
from waddles_cli.helpers.file_manipulation import write_file

from waddles_cli.lib.zimbra.actions.download import download_single_package

if TYPE_CHECKING:  # pragma: no cover
    from waddles_cli.models import config
    from argparse import Namespace


@requires_config
def download(params: Namespace, config_output: config.ConfigLoader):
    if params.option == "single":
        download_single(params=params, config_output=config_output)


def download_single(params: Namespace, config_output: config.ConfigLoader):
    """ Return the active global_config for this user.

    :param params:
    :param config_output: All the global_config values available
    """
    output = download_single_package(username=params.username, zimbra_config=config_output.zimbra)
    path = BACKUP_PATH.format(path=config_output.backup_info.storage_path, username=params.username)
    write_file(request_output=output, backup_path=path)

    return True
