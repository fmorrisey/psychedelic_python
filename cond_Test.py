from random import random
from random import randint

num = input("gimme a number bud: ")

rand = randint(0, 10)

print(rand)

if int(num) == rand:  # The condition is true
    print(num + " The number is equal to 5")  

elif int(num) > rand:  # The condtion is false
    print(num + " The number is greater than 5")  

else:  # The condtion is false
    print("The number is less than 5 since " + num + " is less than 5") 