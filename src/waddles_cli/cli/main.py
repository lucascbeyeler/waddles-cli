#!/usr/bin/python3

from waddles_cli.cli.arguments import main_parser


"""
This is where the CLI will be called.
"""
if __name__ == "__main__":
    args = main_parser.parse_args()
    args.func(params=args)
    try:
        args.func(params=args)
    except TypeError:
        args.func()
    except AttributeError:
        main_parser.print_help()