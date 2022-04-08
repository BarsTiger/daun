# Module for screenshotting
from mss import mss
import tempfile
import pyimgur
import os


def save_screenshot(filename='C:/ProgramData/screenshot.jpg') -> str:
    """
    Saves a screenshot to the specified directory and filename
    """
    mss().shot(mon=-1, output=filename)
    return filename


def upload_to_imgur(client_id: str) -> str:
    """
    Saves a screenshot and uploads it to imgur
    """
    tempdir = tempfile.TemporaryDirectory()
    temp = os.path.join(tempdir.name)
    save_screenshot(temp + '\screenshot.jpg')
    return pyimgur.Imgur(client_id).upload_image(temp + '\screenshot.jpg').link
