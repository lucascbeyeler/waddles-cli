from unittest import mock

from mocks.config_data import GlobalDataConfigOutput
from waddles_cli.operations import show


def test_show():
    with mock.patch("waddles_cli.models.config.yaml_safe_load",
                    side_effect=[GlobalDataConfigOutput.MYSQL, GlobalDataConfigOutput.MYSQL, {}]):
        assert show()
