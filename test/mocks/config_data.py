import os

from yaml import safe_load

EXECUTION_PATH = os.path.dirname(os.path.abspath(__file__))

class GlobalDataConfigPath:

    MYSQL = EXECUTION_PATH + "/../data/global_config/waddles_cli_mysql.yaml"
    SQLITE = EXECUTION_PATH + "/../data/global_config/waddles_cli_sqlite.yaml"


class LocalDataConfigPath:

    MYSQL = EXECUTION_PATH + "/../data/local_config/waddles_cli_mysql.yaml"
    SQLITE = EXECUTION_PATH + "/../data/local_config/waddles_cli_sqlite.yaml"


class MixedDataConfigPath:

    MYSQL_MYSQL = EXECUTION_PATH + "/../data/mixed_config/waddles_cli_mysql.yaml"
    SQLITE_SQLITE = EXECUTION_PATH + "/../data/mixed_config/waddles_cli_sqlite.yaml"
    MYSQL_SQLITE = EXECUTION_PATH + "/../data/mixed_config/waddles_cli_mysql_sqlite.yaml"
    SQLITE_MYSQL = EXECUTION_PATH + "/../data/mixed_config/waddles_cli_sqlite_mysql.yaml"


class GlobalDataConfigOutput:

    MYSQL = safe_load(stream=open(GlobalDataConfigPath.MYSQL))
    SQLITE = safe_load(stream=open(GlobalDataConfigPath.SQLITE))


class LocalDataConfigOutput:

    MYSQL = safe_load(stream=open(LocalDataConfigPath.MYSQL))
    SQLITE = safe_load(stream=open(LocalDataConfigPath.SQLITE))


class MixedDataConfigOutput:

    MYSQL_MYSQL = safe_load(stream=open(MixedDataConfigPath.MYSQL_MYSQL))
    SQLITE_SQLITE = safe_load(stream=open(MixedDataConfigPath.SQLITE_SQLITE))
    MYSQL_SQLITE = safe_load(stream=open(MixedDataConfigPath.MYSQL_SQLITE))
    SQLITE_MYSQL = safe_load(stream=open(MixedDataConfigPath.SQLITE_MYSQL))