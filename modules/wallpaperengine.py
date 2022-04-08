# Module to enable and disable wallpaper engine
from modules.process import get_location
import os


def control_we(command: str) -> None:
    """
    Control wallpaper engine,
    pause, stop, play, mute, unmute
    """
    os.system(str(get_location("wallpaper64.exe") or get_location("wallpaper32.exe")) + ' -control ' + command)
