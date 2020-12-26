import os

from yaml import safe_load

from waddles_cli.constants.keywords import EXECUTION_PATH


class GlobalDataConfigPath:

    MYSQL = EXECUTION_PATH + "test/data/global_config/waddles_cli_mysql.yaml"
    SQLITE = EXECUTION_PATH + "test/data/global_config/waddles_cli_sqlite.yaml"


class LocalDataConfigPath:

    MYSQL = EXECUTION_PATH + "test/data/local_config/waddles_cli_mysql.yaml"
    SQLITE = EXECUTION_PATH + "test/data/local_config/waddles_cli_sqlite.yaml"


class MixedDataConfigPath:

    MYSQL_MYSQL = EXECUTION_PATH + "test/data/mixed_config/waddles_cli_mysql.yaml"
    SQLITE_SQLITE = EXECUTION_PATH + "test/data/mixed_config/waddles_cli_sqlite.yaml"
    MYSQL_SQLITE = EXECUTION_PATH + "test/data/mixed_config/waddles_cli_mysql_sqlite.yaml"
    SQLITE_MYSQL = EXECUTION_PATH + "test/data/mixed_config/waddles_cli_sqlite_mysql.yaml"


class BadDataConfigPath:

    MYSQL = EXECUTION_PATH + "test/data/bad_config/waddles_cli_mysql.yaml"
    SQLITE = EXECUTION_PATH + "test/data/bad_config/waddles_cli_sqlite.yaml"
    PORT = EXECUTION_PATH + "test/data/bad_config/server_port_mysql.yaml"
    PROTO = EXECUTION_PATH + "test/data/bad_config/web_proto_sqlite.yaml"

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


class BadDataConfigOutput:

    MYSQL = safe_load(stream=open(BadDataConfigPath.MYSQL))
    SQLITE = safe_load(stream=open(BadDataConfigPath.SQLITE))
    PORT = safe_load(stream=open(BadDataConfigPath.PORT))
    PROTO = safe_load(stream=open(BadDataConfigPath.PROTO))