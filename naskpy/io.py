from pathlib import Path
from typing import Tuple, Union


def get_project_dir() -> Path:
    """
    Returns the project directory Path object
    :return: Path
    """
    return Path(__file__).parent.parent.absolute()


def split_path(file_path: Union[Path, str]) -> Tuple[str, str, str]:
    """
    Splits a path or a url into its components: filename, basename, extension
    Example: ('v.png', 'v', 'png')
    :param file_path:
    :return: Tuple[str, str, str]
    """
    file_path_str = str(file_path)
    filename = file_path_str.split("/")[-1]
    basename, extension = filename.split(".")
    return filename, basename, extension


def get_parent_folder(file_path: Path) -> Path:
    """
    Returns the parent folder of a file
    :param file_path: Path
    :return: Path
    """
    return file_path.parent
