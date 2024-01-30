#!/usr/bin/python3
"""3. LRU Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Implements a LRU caching system."""

    def __init__(self):
        super().__init__()
        self._least_recently_used = []

    def put(self, key, item):
        """Puts a new entry into the cache system."""
        if key is None or item is None:
            return
        if key in self._least_recently_used:
            self._least_recently_used.remove(key)
        self._least_recently_used.insert(0, key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key = self._least_recently_used.pop()
            del self.cache_data[key]
            print('DISCARD:', key)

    def get(self, key):
        """Retrieves an entry from the cache system."""
        if key not in self.cache_data:
            return None
        if key in self.cache_data:
            self._least_recently_used.remove(key)
        self._least_recently_used.insert(0, key)
        return self.cache_data.get(key)
