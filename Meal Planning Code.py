import random

# Load recipes from recipe file
recipe_list = []
recipe_file = open ("recipe_list.txt", "r")
for line in recipe_file:
    recipe_list.append(line.strip())

def random_gen():
    if len(choice_list) > 0:
        recipe_list.remove(choice_list[-1])
    # remove user choices from list
    r1=random.sample(recipe_list, 5)
    # then from remaining list generate new random samples
    for i in range(5):
        #prints samples out with the numbers next to it
        print(str(i+1) + ' ' + r1[i])
    return r1
#random_list = random_gen()

#user_choice = input("\nChoose a Recipe Using Numbers 1-5, (Q) to Quit: ")
#ans = user_choice.lower()
choice_list = []
quit_list = ["q", "quit", "end", "finished", "finish"]


first_run = True

while first_run == True or ans not in quit_list:
    random_list = random_gen()
    user_choice = input("\nChoose a Recipe Using Numbers 1-5, (Q) to Quit: ")
    first_run=False
    try:
        choice_list.append(random_list[int(user_choice)-1])
        ans = user_choice
    except ValueError as e:
        ans = user_choice.lower()

print ("\nYou Chose: ")
for line in choice_list:
    print(line)



