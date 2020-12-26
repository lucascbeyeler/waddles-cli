from datetime import datetime

from requests import Session
from requests.auth import HTTPBasicAuth

from waddles_cli.libraries.zimbra.constants.urls import ADMIN_URL, START_DATE

class ZimbraAPI:

    def __init__(self, admin_username: str, admin_password: str, webproto: str, server_address: str, admin_port: str):
        self._session = Session()
        self._session.verify = False
        self._session.stream = True
        self._session.auth = HTTPBasicAuth(admin_username, admin_password)
        self._url = ADMIN_URL.format(webproto=webproto, server_address=server_address, server_port=admin_port)


class ZimbraUserAPI(ZimbraAPI):

    def __init__(self, username: str , *args, **kwargs):
        super(ZimbraAPI).__init__(*args, **kwargs)
        self.username = username

    def get_account_tgz(self, date:datetime = datetime.now()):
        """ Download a single package from the Zimbra server based on the informed requirements.

        :param date: Not required - the start point to retrieve the backup
        :return: A requests.session.get output
        """
        start_date = START_DATE.format(seconds=date.second)
        return self._session.get(url=self._url.format(username=self.username, start_date=start_date))

    def set_account_tgz(self):
        pass