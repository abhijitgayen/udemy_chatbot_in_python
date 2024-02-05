class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

    def celebrate_birthday(self):
        self.age += 1
        return f"Happy Birthday, {self.name}! You are now {self.age} years old."

# Example usage:
# Create an instance of the Person class
person1 = Person("Alice", 25)
person2 = Person("Abhijit", 24)


# Get information about the person
print(person1.get_info())

# Celebrate birthday
print(person1.celebrate_birthday())

# After celebrating birthday, get updated information
print(person1.get_info())