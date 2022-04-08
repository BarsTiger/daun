# Module for downloading files from the internet
import requests


def download(url: str, file_name: str) -> None:
    """
    Downloads a file from the internet and saves it to the specified file
    """
    with open(file_name, 'wb') as f:
        f.write(requests.get(url).content)
