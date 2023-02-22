class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


class Pet(Animal):
    def __init__(self, name, species, commands=None):
        super().__init__(name, species)
        self.commands = [] if commands is None else commands

    def add_command(self, command):
        self.commands.append(command)

    def list_commands(self):
        print(f"{self.name} the {self.species} knows the following commands:")
        for command in self.commands:
            print(f"- {command}")


class DraftAnimal(Animal):
    def __init__(self, name, species, commands=None):
        super().__init__(name, species)
        self.commands = [] if commands is None else commands

    def add_command(self, command):
        self.commands.append(command)

    def list_commands(self):
        print(f"{self.name} the {self.species} can perform the following tasks:")
        for command in self.commands:
            print(f"- {command}")


class Command:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return self.description


class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None or self.count > 0:
            raise RuntimeError("Resource not properly managed")


def main():
    counter = Counter()
    pets = []
    while True:
        print("Welcome to the Pet Registry")
        print("Please select an option:")
        print("1. Add a new pet")
        print("2. List all pets")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            with counter:
                name = input("Enter pet name: ")
                species = input("Enter pet species (dog, cat, hamster, horse, camel, or donkey): ")
                if species not in ["dog", "cat", "hamster", "horse", "camel", "donkey"]:
                    print("Invalid species. Please try again.")
                    continue
                if species in ["dog", "cat", "hamster"]:
                    pet = Pet(name, species)
                else:
                    pet = DraftAnimal(name, species)

                pets.append(pet)
                while True:
                    print(f"Commands for {pet.name}:")
                    pet.list_commands()
                    print("Please select an option:")
                    print("1. Add a new command")
                    print("2. Back to previous menu")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        command_name = input("Enter command name: ")
                        command_description = input("Enter command description: ")
                        command = Command(command_name, command_description)
                        pet.add_command(command)
                    elif choice == "2":
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "2":
            print("All pets in the registry:")
            for pet in pets:
                if isinstance(pet, Pet):
                    print(f"{pet.name} the {pet.species} (pet)")
                else:
                    print(f"{pet.name} the {pet.species} (draft animal)")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


main()
