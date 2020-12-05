from argparse import ArgumentParser

from waddles_cli import operations
from waddles_cli.constants.information import WaddlesInfo

main_parser = ArgumentParser(
    prog="waddles_cli",
    description=WaddlesInfo.DESCRIPTION
)

sub_parser = main_parser.add_subparsers()

# Version
version_parser = sub_parser.add_parser("version", description="Return the status of the product")
version_parser.set_defaults(func=operations.version)

# Show
show_parser = sub_parser.add_parser("show", description="Used as a debug tool - return the values used as global_config")
show_parser.add_argument("option", nargs="?", default="all",
                         help="Define which section of the global_config you want to see - all for all the configs")
show_parser.set_defaults(func=operations.show)
