"""Sync/async download of files from the internet."""

from typing import Tuple, Iterator
from pathlib import Path
import grequests


def g_download_multiple(urls: list[str], filename: list[Path]) -> Iterator[Tuple[str, Path]]:
    """download multiple files in parallel.

    :param urls: list of urls to download
    :type urls: list[str]
    :param filename: list of filenames to save to
    :type filename: list[Path]
    :rtype: Iterator[Tuple[str, Path]]
    """

    def exception_handler(request, exception):
        print(f"{request} has failed: {exception}")

    responses = (grequests.get(u) for u in urls)
    responses = grequests.map(responses, exception_handler=exception_handler)
    for i, (response, file) in enumerate(zip(responses, filename)):
        with open(file, 'wb') as f:
            if response:
                f.write(response.content)
                x = (urls[i], True)
            else:
                x = (urls[i], False)
        yield x
