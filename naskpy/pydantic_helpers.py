"""helpers for pydantic (model validation and serialization library)."""

from unittest import TestCase


def show_diff(instance1, instance2) -> None:
    """Show difference between two pydantic instances.

    :param instance1: pydantic instance
    :type instance1: pydantic.BaseModel
    :param instance2: pydantic instance
    :type instance2: pydantic.BaseModel
    :rtype: None
    """
    if instance1 == instance2:
        print("EQUAL.")
    else:
        print("DIFFERENT:")
        try:
            TestCase().assertDictEqual(instance1.dict(), instance2.dict())
        except Exception as e:
            print(e)
