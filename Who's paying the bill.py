import random

names_string = input("Give me everybody's name, separated by a comma. ")
names = names_string.split(", ")
len_names = len(names)
rdm = random.randint(0,len_names - 1)
pull_name = names[rdm]
print(f"{pull_name} is going to buy the meal today!")