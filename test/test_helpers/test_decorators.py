from unittest import mock

import pytest

from waddles_cli.helpers import decorators


@pytest.mark.parametrize("content", ["database"])
def test_requires_config_with_content(content):
    @decorators.requires_config
    def test(_):
        return True

    with mock.patch("waddles_cli.models.config.ConfigLoader", mock.Mock):
        assert test(inner_content=content)


def test_requires_config_without_content():
    @decorators.requires_config
    def test(_):
        return True

    with mock.patch("waddles_cli.models.config.ConfigLoader", mock.Mock):
        assert test()
