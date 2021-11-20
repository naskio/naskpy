from typing import Tuple


def split_url(url: str) -> Tuple[str, str, str]:
    """
    Splits a url into its components: filename, basename, extension
    Example: ('v.png', 'v', 'png')
    :param url:
    :return: Tuple[str, str, str]
    """
    filename = url.split("/")[-1]
    x, _ = filename.split("?")
    basename, extension = x.split(".")
    return x, basename, extension
