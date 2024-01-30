#!/usr/bin/python3
"""0. Basic dictionary"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A class for a basic caching system."""

    def put(self, key, item):
        """Puts a new entry into the cache system."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an entry from the cache system."""
        self.cache_data.get(key)
