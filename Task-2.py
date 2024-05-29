class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
    
    def say(self):
        pass

# Creating an instance of the Animal class with nickname and weight
animal = Animal(nickname="Buddy", weight=10)

# Printing the attributes of the animal instance to verify
print(f"Nickname: {animal.nickname}, Weight: {animal.weight}")
