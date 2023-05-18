#!/usr/bin/python3
""" LRU Caching """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """a class LRUCache that inherits from BaseCaching
    and is a caching system """
    def __init__(self):
        """ Initialize class instance. """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key """
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(discarded[0]))

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
