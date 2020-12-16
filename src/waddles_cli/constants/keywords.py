import os

EXECUTION_PATH = os.path.dirname(os.path.abspath(__file__)) + "/../../../"

SQLALCHEMY_CONN_STRUCTURE = "{server_type}:///{database_name}"

BACKUP_PATH = "{path}/{username}.tgz"