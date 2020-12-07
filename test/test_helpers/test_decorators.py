import pytest
from unittest import mock

from waddles_cli.helpers import decorators


@pytest.mark.parametrize("content", ["database"])
@mock.patch("jsonschema.validate", mock.Mock)
def test_requires_config_with_content(content):
    @decorators.requires_config
    def test(_):
        return True

    assert test(inner_content=content)


@mock.patch("jsonschema.validate", mock.Mock)
def test_requires_config_without_content():
    @decorators.requires_config
    def test(_):
        return True

    assert test()
