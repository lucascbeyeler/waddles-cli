from dataclasses import dataclass

from jsonschema import validate

from waddles_cli.constants.keywords import EXECUTION_PATH
from waddles_cli.helpers.file_manipulation import yaml_safe_load
from waddles_cli.helpers.utils import merge_two_dictionaries

# Config file path
SCHEMA_PATH = EXECUTION_PATH + "src/waddles_cli/schemas/config.yaml"
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

    @staticmethod
    def __get_configs__() -> dict:
        """ Retrieve and build the active global_config. The active global_config is a mix of what is inside ".waddles_cli" and
            "/etc/waddles/waddles_cli".

        :return: The Waddles global_config
        """
        local_config = yaml_safe_load(path_to_file=LOCAL_CONFIG_PATH)
        general_config = yaml_safe_load(path_to_file=GENERAL_CONFIG_PATH)
        return merge_two_dictionaries(object_1=general_config, object_2=local_config)

    def __validate__(self) -> dict:
        """ Validate if the active global_config is valid or not.

        :return: The Waddles global_config
        """
        config = self.__get_configs__()
        schema = yaml_safe_load(path_to_file=SCHEMA_PATH)
        validate(instance=config, schema=schema)
        return config
