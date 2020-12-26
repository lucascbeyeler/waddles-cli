from __future__ import annotations

from typing import TYPE_CHECKING

from waddles_cli.helpers.decorators import requires_config
from waddles_cli.constants.keywords import BACKUP_PATH
from waddles_cli.helpers.file_manipulation import write_file

from waddles_cli.libraries.zimbra.models.session import ZimbraUserAPI

if TYPE_CHECKING:  # pragma: no cover
    from waddles_cli.models import config
    from argparse import Namespace


@requires_config
def download(params: Namespace, config_output: config.ConfigLoader) -> bool:
    """ An abstraction for the method download_single or download_multiple

    :param params: A Namespace object with the parameters informed by the user
    :param config_output: All the global_config values available
    """
    if params.option == "single":
        download_single(params=params, config_output=config_output)
    return True

def download_single(params: Namespace, config_output: config.ConfigLoader) -> bool:
    """ Return the active global_config for this user.

    :param params: A Namespace object with the parameters informed by the user
    :param config_output: All the global_config values available
    """
    zimbra_connection = ZimbraUserAPI(admin_username=config_output.zimbra.admin_username,
                                      admin_password=config_output.zimbra.admin_password,
                                      webproto=config_output.zimbra.webproto,
                                      server_address=config_output.zimbra.server_address,
                                      admin_port=config_output.zimbra.server_port,
                                      username=params.username)

    output = zimbra_connection.get_account_tgz()
    path = BACKUP_PATH.format(path=config_output.backup_info.storage_path, username=params.username)
    write_file(request_output=output, backup_path=path)
    return True
