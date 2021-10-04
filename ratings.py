"""Restaurant rating lister."""
import random

# put your code here
the_file = open("scores.txt")

scores_dictionary = {}

for line in the_file:
    line = line.rstrip()

    element = line.split(":")
    scores_dictionary[element[0]] = int(element[1])
# user input for new restaurant and score to be added to dictionary

restaurant_name = input("> ").title()

while True:
    try:
        restaurant_rating = int(input("Please enter a score for new restaurant: "))
        break
    except ValueError:
        print("uh oh!  That was no valid number.  Try again...")

while restaurant_rating not in range(1,6):
    print("Please pick number from 1 to 5")
    while True:
        try:
            restaurant_rating = int(input("Please enter a score for new restaurant: "))
            break
        except ValueError:
            print("uh oh!  That was no valid number.  Try again...")

scores_dictionary[restaurant_name] = restaurant_rating
alpha_list = scores_dictionary.keys()
alpha_list_sorted = sorted(alpha_list)
# for store in alpha_list_sorted:
#     print(f'{store} is rated at {scores_dictionary[store]}')


#select random restaurant from dictionary and prompt suer to change score
random_restaurant = random.choice(list(scores_dictionary.keys()))
# print(f'{random_restaurant} has a score of {scores_dictionary[random_restaurant]}')

while True:
    try:
        new_rating = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

while new_rating not in range(1, 6):
    print("Please pick number from 1 to 5")
    while True:
        try:
            new_rating = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            
scores_dictionary[random_restaurant] = new_rating
print(f'{random_restaurant} has a score of {scores_dictionary[random_restaurant]}')