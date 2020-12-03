from argparse import ArgumentParser

from waddles_cli.constants.information import WaddlesInfo
from waddles_cli import operations

main_parser = ArgumentParser(
    prog="waddles_cli",
    description=WaddlesInfo.DESCRIPTION
)

sub_parser = main_parser.add_subparsers()

# Version
version_parser = sub_parser.add_parser("version", description="Return the status of the product")
version_parser.set_defaults(func=operations.version)
