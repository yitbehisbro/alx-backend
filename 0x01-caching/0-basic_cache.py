#!/usr/bin/python3
""" Basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ a class BasicCache that inherits from BaseCaching
    and is a caching system """
    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)
