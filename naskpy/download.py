"""Sync/async download of files from the internet."""

from typing import Tuple, Iterator
from pathlib import Path
import grequests
import urllib.request
import urllib.error


def g_download_multiple(urls: list[str], filepaths: list[Path]) -> Iterator[Tuple[str, Path, bool]]:
    """download multiple files in parallel.

    :param urls: list of urls to download
    :type urls: list[str]
    :param filepaths: list of filenames to save to
    :type filepaths: list[Path]
    :return: iterator of tuples of (url, filepath, success)
    :rtype: Iterator[Tuple[str, Path, bool]]
    """

    def exception_handler(request, exception):
        print(f"{request} has failed: {exception}")

    responses = (grequests.get(u) for u in urls)
    responses = grequests.map(responses, exception_handler=exception_handler)
    results = []
    for i, (response, filepath) in enumerate(zip(responses, filepaths)):
        with open(filepath, 'wb') as f:
            if response:
                f.write(response.content)
                results.append(True)
            else:
                results.append(False)
    return zip(urls, filepaths, results)


def download(url: str, filepath: Path) -> bool:
    """download the file from the url and save it to file.

    :param url: url to download
    :type url: str
    :param filepath: file to save to
    :type filepath: Path
    :rtype: bool
    """
    try:
        urllib.request.urlretrieve(url, filepath)
        return True
    except urllib.error.URLError:
        return False
