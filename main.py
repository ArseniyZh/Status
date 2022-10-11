from pprint import *


class TreeStore:
    def __init__(self, _items):
        self.items = _items

    def getAll(self) -> tuple:
        return self.items

    def getItem(self, _id: int) -> dict | str:
        try:
            return self.items[_id - 1]
        except:
            return 'Введено некорректное значение'

    def getChildren(self, _id: int) -> list:
        childrens = [item for item in self.items if item['parent'] == _id]
        return childrens

    def getAllParents(self, _id: int) -> list | str:
        flag = True
        parents_array = []
        while flag:
            try:
                _id = self.items[_id]['parent']
                parent = self.items[_id - 1]

                if len(parents_array) > 0 and parent == parents_array[-1]:
                    flag = False
                parents_array.append(parent)
            except:
                return 'Введено некорректное значение'

        return parents_array[:-1]


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)
pprint(ts.getAll())
print()
pprint(ts.getItem(7))
print()
pprint(ts.getChildren(4))
print()
pprint(ts.getAllParents(7))
