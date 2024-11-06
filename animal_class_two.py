class Animal:
    def __init__(self, name: str, age: int, race: str, weight: int):
        self.name = name
        self.age = age
        self.race = race
        self.weight = weight

    def __str__(self):
        return (f"Nombre: {self.name}, edad: {self.age} años, "
                f"raza: {self.race}, peso: {self.weight}")

horse = Animal("Zeus", 5, "Pura Sangre", 450)
lion = Animal("Boulder", 10, "Atlas", 130)
print(horse, lion, sep="\n")
