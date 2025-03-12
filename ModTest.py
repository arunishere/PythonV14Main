import math

# x = math.factorial(100)

# print(x)

#Write a program which calculates factorial only of even numbers from 1-10


# I want to count the total even numbers from 1 - 10 


# a = 1

# while a < 11:

#     if a%2 != 0:
#         result = math.factorial(a)
#         print(f'{a}! = {result}')


#     a = a + 1

# a = 1
# total_even = 0
# while a < 101:
#     if a%2 == 0:
#         total_even = total_even + 1
#     a = a + 1
# print(total_even)

import random


# a = 1

# while a < 11:

#     print(random.randint(1000, 9999))
    
#     a = a + 1


# print(random.randint(1, 10))

# print(help(random.shuffle))


#Front End - HTML, CSS, JavaScript

a = 1
pranav_count = 0
afroz_count = 0
khaja_count = 0

while a < 1000:

    result = random.choice(["John", "Afroz", "Pranav", "Khaja"])
    if result ==  "Afroz":
        afroz_count = afroz_count + 1
    elif result ==  "Pranav":
        pranav_count = pranav_count + 1
    elif result ==  "Khaja":
        khaja_count = khaja_count + 1
    a = a + 1

print(f"Afroz: {afroz_count}, Pranav: {pranav_count}, Khaja: {khaja_count}")