from __future__ import annotations

import yaml
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from requests.models import Response

def yaml_safe_load(path_to_file: str) -> dict:
    """ Load safely a YAML file.

    :param path_to_file: Where the YAML is
    :except FileNotFoundError: If there is no YAML file return an empty dict
    :return: A dictionary with all the YAML keys
    """
    try:
        with open(path_to_file, "r") as fd:
            return yaml.safe_load(fd.read())
    except FileNotFoundError:
        return {}


def write_file(request_output: Response, backup_path: str):
    """

    :param request_output:
    :param backup_path:
    :return:
    """
    output = open(backup_path, "wb")
    for chunk in request_output.iter_content(chunk_size=1024):
        output.write(chunk)
