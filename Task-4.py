class Animal:
    color = "white"  # Class variable

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    @classmethod
    def change_color(cls, new_color):
        cls.color = new_color


first_animal = Animal(nickname="Simon", weight=10)
second_animal = Animal(nickname="Charlie", weight=15)


first_animal.change_color("red")


print(f"Color after change: {Animal.color}")
print(f"Color for first_animal: {first_animal.color}") 
print(f"Color for second_animal: {second_animal.color}") 