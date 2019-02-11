"""daemon utilities"""


def start_daemon() -> bool:
    """start the GREASE daemon

    Returns:
        bool: success of start command

    """
    raise NotImplementedError("start daemon not implemented")


def stop_daemon() -> bool:
    """stop the GREASE daemon

    Returns:
        bool: success of stop command

    """
    raise NotImplementedError("stop daemon not implemented")


def restart_daemon() -> bool:
    """restart the GREASE daemon

    Returns:
        bool: success of restart command

    """
    raise NotImplementedError("restart daemon not implemented")


def install_daemon() -> bool:
    """install the GREASE daemon

    Returns:
        bool: success of install command

    """
    raise NotImplementedError("install daemon not implemented")
