from collections import UserDict

class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys

# Приклад використання:
my_dict = LookUpKeyDict({'a': 1, 'b': 2, 'c': 2})
print(my_dict.lookup_key(2))