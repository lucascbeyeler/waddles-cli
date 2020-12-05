import pytest

from waddles_cli.models import config

from mocks import config_data

@pytest.mark.parametrize("database_config_output", [config_data.GlobalDataConfigOutput.MYSQL, config_data.GlobalDataConfigOutput.SQLITE])
class TestDatabase:

    @pytest.fixture(scope="function", autouse=True)
    def __setup__(self, database_config_output):
        self.dict_output = database_config_output.get("database")
        self.database = config.Database(**self.dict_output)

    def test_database_success(self):
        assert self.database.database_name == self.dict_output.get("database_name")
        assert self.database.server_type == self.dict_output.get("server_type")
        assert self.database.address == self.dict_output.get("address", config.Database.address)
        assert self.database.port == self.dict_output.get("port", config.Database.port)
        assert self.database.username == self.dict_output.get("username", config.Database.username)
        assert self.database.password == self.dict_output.get("password", config.Database.password)


@pytest.mark.parametrize("global_config_path, local_config_path, mixed_configs",(
        (config_data.GlobalDataConfigPath.SQLITE, config_data.LocalDataConfigPath.SQLITE, config_data.MixedDataConfigOutput.SQLITE_SQLITE),
        (config_data.GlobalDataConfigPath.MYSQL, config_data.LocalDataConfigPath.MYSQL, config_data.MixedDataConfigOutput.MYSQL_MYSQL),
        (config_data.GlobalDataConfigPath.SQLITE, config_data.LocalDataConfigPath.MYSQL, config_data.MixedDataConfigOutput.SQLITE_MYSQL),
        (config_data.GlobalDataConfigPath.MYSQL, config_data.LocalDataConfigPath.SQLITE, config_data.MixedDataConfigOutput.MYSQL_SQLITE),
        ("", config_data.GlobalDataConfigPath.SQLITE, config_data.GlobalDataConfigOutput.SQLITE),
        (config_data.GlobalDataConfigPath.MYSQL, "", config_data.GlobalDataConfigOutput.MYSQL),
))
class TestConfigLoader:

    @pytest.fixture(scope="function", autouse=True)
    def __setup__(self, global_config_path, local_config_path):
        config.LOCAL_CONFIG_PATH = local_config_path
        config.GENERAL_CONFIG_PATH = global_config_path
        self.config = config.ConfigLoader()

    def test_get_configs(self, mixed_configs):
        assert self.config.dict_object == mixed_configs

    def test_validate_success(self):
        pass