#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    except if the new instance attribute is called 'first_name'.
    """

    __slots__ = ["first_name"]
