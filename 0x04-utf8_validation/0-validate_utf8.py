#!/usr/bin/python3
"""Contains a method for validating data as UTF-8"""

from typing import List


def singlebyte(val):
    return val < 2**7


def validUTF8(data: List[int]) -> bool:
    """Determines of a given data set represents a valid UTF-8 encoding

    Return: True if data is a valid UTF-8 encoding, else return False
    """
    return not any((not singlebyte(val) for val in data))
