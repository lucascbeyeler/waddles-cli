from unittest import mock

import pytest

from waddles_cli.helpers import decorators


@pytest.mark.parametrize("content", ["database"])
@mock.patch("waddles_cli.models.config.ConfigLoader", mock.Mock)
def test_requires_config_with_content(content):
    @decorators.requires_config
    def test(_):
        return True

    assert test(inner_content=content)


@mock.patch("waddles_cli.models.config.ConfigLoader", mock.Mock)
def test_requires_config_without_content():
    @decorators.requires_config
    def test(_):
        return True

    assert test()
