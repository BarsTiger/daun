import ctypes
import os


def popup(title, text, style=0):
    """
    Styles:
    0 : OK
    1 : OK | Cancel
    2 : Abort | Retry | Ignore
    3 : Yes | No | Cancel
    4 : Yes | No
    5 : Retry | Cancel
    6 : Cancel | Try Again | Continue
    """
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def cls():
    os.system("cls" if os.name == "nt" else "clear")
