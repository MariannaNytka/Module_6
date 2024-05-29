class Animal:
    color = "white"

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

class Cat(Animal):
    def say(self):
        return "Meow"


cat = Cat(nickname="Simon", weight=10)


print(f"Nickname: {cat.nickname}, Weight: {cat.weight}")
print(cat.say())