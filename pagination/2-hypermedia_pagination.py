#!/usr/bin/env python3
"""
Module for hypermedia pagination of a dataset.
"""

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns start and end indexes for a given pagination range.
    """
    start: int = (page - 1) * page_size
    end: int = start + page_size
    return start, end


class Server:
    """
    Server class to paginate a CSV dataset of Popular Baby Names.
    """

    DATA_FILE: str = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: List[List[str]] = None

    def dataset(self) -> List[List[str]]:
        """
        Loads and caches the dataset from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Returns a page of the dataset based on page number and page size.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns a hypermedia pagination dictionary with navigation metadata.
        """
        data_page = self.get_page(page, page_size)
        data = self.dataset()
        total_items = len(data)

        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 and page <= total_pages else None

        return {
            "page_size": len(data_page),
            "page": page,
            "data": data_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
