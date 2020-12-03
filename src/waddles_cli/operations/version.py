from waddles_cli.constants.information import WaddlesInfo


def version():
    """ Return information about the Waddles build
    """
    print(WaddlesInfo.DESCRIPTION)
    print("Version: {version}".format(version=WaddlesInfo.VERSION))
    print("Status: {status}".format(status=WaddlesInfo.STATUS))
