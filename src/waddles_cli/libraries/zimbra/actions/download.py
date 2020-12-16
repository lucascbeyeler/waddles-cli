from __future__ import annotations

from requests import Session
from requests.auth import HTTPBasicAuth
from typing import TYPE_CHECKING
from datetime import datetime

from waddles_cli.lib.zimbra.constants.urls import ADMIN_URL, START_DATE

if TYPE_CHECKING:
    from waddles_cli.models.config import Zimbra


def download_single_package(username: str, zimbra_config: Zimbra, date:datetime = datetime.now()):
    """

    :param username:
    :param zimbra_config:
    :param date:
    :return:
    """
    session = Session()
    session.verify = False
    session.stream = True
    session.auth = HTTPBasicAuth(zimbra_config.admin_username, zimbra_config.admin_password)
    start_date = START_DATE.format(seconds=date.second)
    url = ADMIN_URL.format(webproto=zimbra_config.webproto, server_address=zimbra_config.server_address,
                           server_port=zimbra_config.server_port, username=username,
                           start_date=start_date)
    return session.get(url=url)

