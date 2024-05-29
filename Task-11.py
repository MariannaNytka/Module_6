from collections import UserString

class NumberString(UserString):
    def number_count(self):
        count = 0
        for char in self.data:
            if char.isdigit():
                count += 1
        return count

# Приклад використання:
my_string = NumberString("Hello12345")
print(my_string.number_count())