import random

# Generate a random integer between a specified range (inclusive)
random_number = random.randint(1, 100)

print("Random Number:", random_number)

# let make a game using while loop
input_num = int(input("Enter Number between 10 and 20 :"))
while input_num != 13:
    input_num = int(input("Enter Number between 10 and 20. Guess again :"))