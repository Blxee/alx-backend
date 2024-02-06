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

        if ((len(self.cache_data) >= BaseCaching.MAX_ITEMS)
                and (key not in self.cache_data)):
            rmkey = heappop(self._least_frequently_used)[1]
            del self.cache_data[rmkey]
            print('DISCARD:', rmkey)

        freqency = 0
        for i, (f, k) in enumerate(self._least_frequently_used):
            if k == key:
                self._least_frequently_used.pop(i)
                freqency = f
        heappush(self._least_frequently_used, (freqency + 1, key))

        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an entry from the cache system."""
        if key not in self.cache_data:
            return None
        freqency = 0
        for i, (f, k) in enumerate(self._least_frequently_used):
            if k == key:
                self._least_frequently_used.pop(i)
                freqency = f
        heappush(self._least_frequently_used, (freqency + 1, key))
        return self.cache_data[key]
