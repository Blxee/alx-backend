#!/usr/bin/python3
"""1. FIFO caching"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Implements a FIFO caching system."""

    def put(self, key, item):
        """Puts a new entry into the cache system."""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key = list(self.cache_data.keys())[0]
            del self.cache_data[key]
            print('DISCARD:', key)

    def get(self, key):
        """Retrieves an entry from the cache system."""
        return self.cache_data.get(key)
