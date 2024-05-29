class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
        self.cat = Cat(nickname, weight)  # Створюємо екземпляр класу Cat з переданим nickname та weight

    def say(self):
        return self.cat.say()  # Викликаємо метод say з класу Cat

    def change_weight(self, weight):
        self.weight = weight
        self.cat.change_weight(weight)  # Викликаємо метод change_weight з класу Cat

# Приклад використання:
cat_dog = CatDog("Whiskers", 5)
print(cat_dog.say())  # Виведе: "Meow"
print(cat_dog.weight)  # Виведе: 5

cat_dog.change_weight(7)
print(cat_dog.weight) 