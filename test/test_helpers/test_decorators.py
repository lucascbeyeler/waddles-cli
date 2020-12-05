import pytest

from waddles_cli.helpers import decorators

from mocks.config_data import GlobalDataConfigOutput


@pytest.mark.parametrize("content, intended_output",(
        ("all", GlobalDataConfigOutput),
))
def test_requires_config(content, intended_output):
    pass