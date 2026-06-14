#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by position (supports deletion)"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a deletion-resilient page of the dataset.
        """

        indexed_data = self.indexed_dataset()

        if index is None:
            index = 0

        # validate index
        assert isinstance(index, int)
        assert isinstance(page_size, int) and page_size > 0
        assert index >= 0 and index <= max(indexed_data.keys())

        data = []
        current = index
        max_index = max(indexed_data.keys())

        # collect page_size valid items skipping missing indexes
        while len(data) < page_size and current <= max_index:
            if current in indexed_data:
                data.append(indexed_data[current])
            current += 1

        # find next valid index
        next_index = None
        while current <= max_index:
            if current in indexed_data:
                next_index = current
                break
            current += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
