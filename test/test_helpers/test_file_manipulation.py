import pytest

from waddles_cli.helpers import file_manipulation

from mocks.config_data import GlobalDataConfigPath, GlobalDataConfigOutput

@pytest.mark.parametrize("path_to_file, intended_output",(
        ("/home/jurassic_park/test.yaml", {}),
        (GlobalDataConfigPath.MYSQL, GlobalDataConfigOutput.MYSQL),
        (GlobalDataConfigPath.SQLITE, GlobalDataConfigOutput.SQLITE),
))
def test_yaml_safe_load(path_to_file, intended_output):
    observed_output = file_manipulation.yaml_safe_load(path_to_file=path_to_file)
    assert intended_output == observed_output
