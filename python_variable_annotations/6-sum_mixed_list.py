#!/usr/bin/env python3
"""Returns the sum of a mixed list of integers and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum of integers and floats in a list."""
    return sum(mxd_lst)
