#!/usr/bin/python3
"""5. LFU Caching"""
from heapq import heappush, heappop
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Implements a LFO caching system."""

    def __init__(self):
        super().__init__()
        self._least_frequently_used = []

    def put(self, key, item):
        """Puts a new entry into the cache system."""
        if key is None or item is None:
            return
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            key = heappop(self._least_frequently_used)[1]
            del self.cache_data[key]
            print('DISCARD:', key)
        self.cache_data[key] = item
        frequency = 0
        if key in map(lambda x: x[1], self._least_frequently_used):
            frequency = heappop(self._least_frequently_used)[0]
        heappush(self._least_frequently_used, (frequency + 1, key))

    def get(self, key):
        """Retrieves an entry from the cache system."""
        if key not in self.cache_data:
            return None
        frequency = heappop(self._least_frequently_used)[0]
        heappush(self._least_frequently_used, (frequency + 1, key))
        return self.cache_data.get(key)
