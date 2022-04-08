# Module to change wallpapers
import ctypes
import os
import requests


def set_wallpaper(link: str) -> None:
    """
    Set the wallpaper to the given link or file
    """
    if link.startswith('http'):
        with open(str(os.getenv('TEMP') + 'wallpaper' + link.split('.')[-1]), 'wb') as f:
            f.write(requests.get(link).content)
        path = os.getenv('TEMP') + 'wallpaper' + link.split('.')[-1]
    else:
        path = link

    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
