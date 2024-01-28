#!/usr/bin/env python3
"""2. Hypermedia pagination"""
import csv
import math
from typing import Dict, List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a page from a CSV file."""
        assert type(page) == int, "page must be an integer"
        assert type(page_size) == int,  "page_size must be an integer"
        assert page > 0, "page must be greater than 0"
        assert page_size > 0,  "page_size must be greater than 0"
        self.dataset()
        i, j = index_range(page, page_size)
        if self.__dataset is None:
            return []
        return self.__dataset[i:j]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns page from the dataset with additional meta data."""
        data = self.get_page(page, page_size)
        if self.__dataset is None:
            return {}

        next_page = page + 1
        if next_page * page_size >= len(self.__dataset):
            next_page = None

        prev_page = page - 1
        if prev_page < 0:
            prev_page = None

        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }
