"""Sync/async download of files from the internet."""

from typing import Tuple, Iterator
from pathlib import Path
import grequests
import urllib.request
import urllib.error
import asyncio
import aiohttp


def g_download_multiple(urls: list[str], filepaths: list[Path]) -> list[Tuple[str, Path, bool]]:
    """Download multiple files in parallel.

    :param urls: list of urls to download
    :type urls: list[str]
    :param filepaths: list of filenames to save to
    :type filepaths: list[Path]
    :return: list of tuples of (url, filepath, success)
    :rtype: list[Tuple[str, Path, bool]]
    """

    def exception_handler(request, exception):
        print(f"{request} has failed: {exception}")

    responses = (grequests.get(u) for u in urls)
    responses = grequests.map(responses, exception_handler=exception_handler)
    results = []
    for i, (response, filepath) in enumerate(zip(responses, filepaths)):
        if response:
            with open(filepath, 'wb') as f:
                f.write(response.content)
                results.append(True)
        else:
            results.append(False)
    return list(zip(urls, filepaths, results))


def download(url: str, filepath: Path) -> bool:
    """Download the file from the url and save it to file.

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


async def _async_download(session: aiohttp.ClientSession, url: str, filepath: Path) -> Tuple[str, Path, str, bool]:
    """Async download a file from url and save it to filepath.

    :param session: aiohttp session
    :type session: aiohttp.ClientSession
    :param url: url to download
    :type url: str
    :param filepath: file to save to
    :type filepath: Path
    :return: tuple of (url, filepath, message, success)
    """
    # try:
    async with session.get(url) as response:
        # if response.status == 200:
        if response.ok:  # response.status < 400
            content = await response.read()
            with open(filepath, 'wb') as f:
                f.write(content)
            return url, filepath, str(response.status), True
        else:
            return url, filepath, str(response.status), False
    # except Exception as e:
    #     return url, filepath, e, False


async def _async_download_multiples(urls: list[str], filepaths: list[Path]) -> Iterator[Tuple[str, Path, str, bool]]:
    """Download multiple files concurrently.

    :param urls: list of urls to download
    :type urls: list[str]
    :param filepaths: list of filenames to save to
    :type filepaths: list[Path]
    :return: iterator of tuples of (url, filepath, message, success)
    :rtype: Iterator[Tuple[str, Path, str, bool]]
    """
    # async with aiohttp.ClientSession(raise_for_status=True) as session:
    async with aiohttp.ClientSession() as session:
        downloads = [_async_download(session, urls[i], filepaths[i]) for i in range(len(urls))]
        results = []
        for dl in asyncio.as_completed(downloads):
            result = await dl
            print(result)
            results.append(result)
        return results


def _download_multiple_async_wrapper(urls: list[str], filepaths: list[Path]) -> Iterator[Tuple[str, Path, str, bool]]:
    """Async wrapper for download multiple files concurrently."""
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(_async_download_multiples(urls, filepaths))
    return results


def download_multiple(urls: list[str], filepaths: list[Path], chunk_size: int = None) -> \
        Iterator[Tuple[str, Path, str, bool]]:
    """Download multiple files concurrently, chunk by chunk.

    :param urls: list of urls to download
    :type urls: list[str]
    :param filepaths: list of filenames to save to
    :type filepaths: list[Path]
    :param chunk_size: number of files to download at once
    :type chunk_size: int, optional
    :rtype: Iterator[Tuple[str, Path, str, bool]]
    """
    if not chunk_size:
        return _download_multiple_async_wrapper(urls, filepaths)
    results = []
    for i in range(0, len(urls), chunk_size):
        print(f'Downloading {i} to {i + chunk_size}...')
        results.extend(_download_multiple_async_wrapper(urls[i:i + chunk_size], filepaths[i:i + chunk_size]))
    return results
