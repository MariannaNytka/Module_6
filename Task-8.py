class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def info(self):
        return f"{self.nickname}-{self.weight}"


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog(Cat, Dog):
    def say(self):
        return super().say()  # Викликаємо метод say з класу Cat


class DogCat(Dog, Cat):
    def say(self):
        return super().say()  # Викликаємо метод say з класу Dog


# Приклад використання:
cat_dog = CatDog("Catty", 5)
print(cat_dog.say())  # Виведе "Meow"
print(cat_dog.info())  # Виведе "Catty-5"

dog_cat = DogCat("Doggy", 10)
print(dog_cat.say())  # Виведе "Woof"
print(dog_cat.info())  # Виведе "Doggy-10"
    
        


    
        