import copy
from collections.abc import MutableSequence

from .token import BOS, EOS


class Sentence(MutableSequence):
    def __init__(self, members=None):
        if not members:
            members = []
        self.__members = members

        self.update_pointer()

    def insert(self, i, x):
        self.__members.insert(i, x)
        self.update_pointer()

    def update_pointer(self):
        if len(self.__members) == 0:
            return

        node = self.__members[0]
        node.next = None
        node.prev = BOS(node.next)

        if len(self.__members) > 1:
            for m in self.__members[1:]:
                node.next = m
                node.next.prev = node

                node = node.next
            node.next = EOS(node)

    def __iter__(self):
        for member in self.__members:
            yield member

    def __contains__(self, x):
        if isinstance(x, str) and x in [m.surface for m in self.__members]:
            return True
        if x in self.__members:
            return True
        return False

    def __reversed__(self):
        """"""
        copied_self = copy.deepcopy(self)
        copied_self.reverse()

        for copied_member in copied_self:
            yield copied_member

    def __getitem__(self, key):
        return self.__members[key]

    def __delitem__(self, key):
        self.__members.pop(key)

    def __len__(self):
        return len(self.__members)

    def __setitem__(self, key, value):
        self.__members[key] = value
        self.update_pointer()

    def __str__(self):
        return repr(self.__members)

    def __repr__(self):
        return self.__str__()
