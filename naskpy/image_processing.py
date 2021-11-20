from io import BytesIO
from typing import Tuple

import requests
from PIL import Image


def resize_by_width(image: Image.Image, nw: int) -> Image.Image:
    """
    Resize an image by a given width
    :param image: Image
    :param nw: int
    :return: Image
    """
    w, h = image.size
    if w == nw:
        return image
    w_ratio = float(nw) / float(w)
    new_size = (nw, round(float(h) * w_ratio))
    new_image = image.resize(new_size, Image.ANTIALIAS)
    # new_image = image.copy()
    # new_image.thumbnail(new_size, Image.ANTIALIAS)  works only to make it smaller but it doesn't make it bigger
    return new_image


def resize_by_height(image: Image.Image, nh: int) -> Image.Image:
    """
    Resize an image by a given height
    :param image: Image
    :param nh: int
    :return: Image
    """
    w, h = image.size
    if h == nh:
        return image
    h_ratio = float(nh) / float(h)
    new_size = (round(float(w) * h_ratio), nh)
    new_image = image.resize(new_size, Image.ANTIALIAS)
    return new_image


def resize(
        image: Image.Image,
        size: Tuple[int, int],
        crop: bool = False,
        position: Tuple[str, str] = ("center", "center"),
        fill_color=(0, 0, 0, 0),
) -> Image.Image:
    """
    Resize an image to a given size.
    :param image: Image
    :param size: Tuple[int, int]
    :param crop: bool
    :param position: Tuple[str, str]
    :param fill_color: Tuple[int, int, int, int]
    :return: Image
    """
    nw, nh = size
    n_ratio = float(nw) / float(nh)
    w, h = image.size
    ratio = float(w) / float(h)
    image_c = image.copy()
    background_color_image = Image.new("RGBA", size, fill_color)
    if n_ratio >= 1.0:
        if ratio >= 1.0:
            if crop:
                if n_ratio >= ratio:
                    image_c = resize_by_width(image_c, nw)
                else:
                    image_c = resize_by_height(image_c, nh)
            else:
                if n_ratio >= ratio:
                    image_c = resize_by_height(image_c, nh)
                else:
                    image_c = resize_by_width(image_c, nw)
        else:  # 1.0 > n_ratio > ratio
            if crop:
                image_c = resize_by_width(image_c, nw)
            else:
                image_c = resize_by_height(image_c, nh)
    else:  # n_ratio < 1.0
        if ratio >= 1.0:  # ratio > n_ratio
            if crop:
                image_c = resize_by_height(image_c, nh)
            else:
                image_c = resize_by_width(image_c, nw)
        else:  # ratio < 1.0
            if crop:
                if n_ratio >= ratio:
                    image_c = resize_by_width(image_c, nw)
                else:
                    image_c = resize_by_height(image_c, nh)
            else:
                if n_ratio >= ratio:
                    image_c = resize_by_height(image_c, nh)
                else:
                    image_c = resize_by_width(image_c, nw)
    x_position, y_position = (
        round(float(nw - image_c.size[0]) / 2.0),
        round(float(nh - image_c.size[1]) / 2.0),
    )
    if position[1] == "left":
        x_position = 0
    elif position[1] == "right":
        x_position = nw - image_c.size[0]
    if position[0] == "top":
        y_position = 0
    elif position[0] == "bottom":
        y_position = nh - image_c.size[1]
    background_color_image.paste(image_c, (x_position, y_position))
    return background_color_image


def to_square(
        image: Image.Image,
        side_length: int,
        fill_color=(0, 0, 0, 0),
        center_crop: bool = False,
) -> Image.Image:
    """
    Resize an image to a square of a given side length.
    :param image: Image
    :param side_length: int
    :param fill_color: Tuple[int, int, int, int]
    :param center_crop: bool
    :return: Image
    """
    return resize(
        image, (side_length, side_length), crop=center_crop, fill_color=fill_color
    )


def get_remote_image(url: str) -> Image.Image:
    """
    Get an image from a remote url.
    :param url: str
    :return: Image
    """
    res = requests.get(url)
    if res:
        image = Image.open(BytesIO(res.content))
        return image
