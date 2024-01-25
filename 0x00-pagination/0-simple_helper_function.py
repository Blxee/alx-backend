#!/usr/bin/env python3
"""0. Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Simple helper function to get oage start and end indices."""
    start = page_size * (page - 1)
    end = page_size * page
    return (start, end)
