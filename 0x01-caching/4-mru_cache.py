#!/usr/bin/python3
"""4. MRU Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Implements a MRU caching system."""

    def __init__(self):
        super().__init__()
        self._most_recently_used = []

    def put(self, key, item):
        """Puts a new entry into the cache system."""
        if key is None or item is None:
            return
        if key in self._most_recently_used:
            self._most_recently_used.remove(key)
        self._most_recently_used.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key = self._most_recently_used[-2]
            self._most_recently_used.remove(key)
            del self.cache_data[key]
            print('DISCARD:', key)

    def get(self, key):
        """Retrieves an entry from the cache system."""
        if key not in self.cache_data:
            return None
        if key in self.cache_data:
            self._most_recently_used.remove(key)
        self._most_recently_used.append(key)
        return self.cache_data.get(key)
