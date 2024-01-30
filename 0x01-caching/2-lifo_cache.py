#!/usr/bin/python3
"""2. LIFO Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Implements a LIFO caching system."""

    def put(self, key, item):
        """Puts a new entry into the cache system."""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key = list(self.cache_data.keys())[-2]
            del self.cache_data[key]
            print('DISCARD:', key)

    def get(self, key):
        """Retrieves an entry from the cache system."""
        return self.cache_data.get(key)
