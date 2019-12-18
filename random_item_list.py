from random import randint

class RandomItemList:

    def __init__(self, item_list):
        self._item_list = item_list
        self._items = []
        self._last_item_seen = None
        self._reset_items()
    
    def next_item(self):
        if len(self._items) == 0:
            self._reset_items()
        
        # Make sure the item selected wasn't the last item seen (in the case of a reset)
        next_item = self._last_item_seen
        while next_item == self._last_item_seen:
            next_item = self._items[randint(0, len(self._items) - 1)]
        self._last_item_seen = next_item

        self._items.remove(next_item)

        return next_item
    
    def _reset_items(self):
        for item in self._item_list:
            self._items.append(item)