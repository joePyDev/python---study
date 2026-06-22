class Dog:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    def bark(self):
        print(f"Woof! My name is {self._name} and I'm a {self._breed}.")


my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()
