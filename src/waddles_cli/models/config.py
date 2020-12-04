from dataclasses import dataclass

from jsonschema import validate

from waddles_cli.helpers.file_manipulation import yaml_safe_load

# Config file path
SCHEMA_PATH = "waddles_cli/schemas/config.yaml"
LOCAL_CONFIG_PATH = "~/.waddles_cli"
GENERAL_CONFIG_PATH = "/etc/waddles/waddles_cli"


# Database options
@dataclass
class Database:
    server_type: str
    database_name: str
    address: str = None
    port: int = 8080
    username: str = None
    password: str = None


# The loader for configs
class ConfigLoader:
    database: Database
    dict_object: dict

    def __init__(self):
        config = self.__validate__()
        self.__load_configs__(config=config)

    def __load_configs__(self, config: dict):
        """ Build the ConfigLoader object
        :param config: a valid YAML file
        """
        self.database = Database(**config.get("database"))
        self.dict_object = config

    def __get_configs__(self) -> dict:
        """ Retrieve and build the active config. The active config is a mix of what is inside ".waddles_cli" and
            "/etc/waddles/waddles_cli".

        :return: The Waddles config
        """
        local_config = yaml_safe_load(path_to_file=LOCAL_CONFIG_PATH)
        general_config = yaml_safe_load(path_to_file=GENERAL_CONFIG_PATH)
        return {**general_config, **local_config}

    def __validate__(self) -> dict:
        """ Validate if the active config is valid or not.

        :return: The Waddles config
        """
        schema = yaml_safe_load(path_to_file=SCHEMA_PATH)
        config = self.__get_configs__()
        validate(instance=config, schema=schema)
        return config
