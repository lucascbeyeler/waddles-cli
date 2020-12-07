import pytest
from unittest import mock

from waddles_cli.helpers import decorators
from mocks.config_data import GlobalDataConfigOutput


@pytest.mark.parametrize("content", ["database"])
def test_requires_config_with_content(content):
    with mock.patch("yaml.safe_load", return_value=GlobalDataConfigOutput.MYSQL):
        @decorators.requires_config
        def test(_):
            return True

        assert test(inner_content=content)


def test_requires_config_without_content():
    with mock.patch("yaml.safe_load", return_value=GlobalDataConfigOutput.MYSQL):
        @decorators.requires_config
        def test(_):
            return True

        assert test()
