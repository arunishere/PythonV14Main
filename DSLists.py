
#CRUD
#Created
#Data be accessed - indexing
#add more data - Updation
#Delete values
#working with more than one


#Data Structure or Object

#List

# 1. append
# 2. extend
# 3. insert
# 4. len
# 5. count
# 6. pop
# 7. remove


cities = ["Hyderabad", "Chennai", "Mumbai", "Kolkota"]

# cities.append("Pune")
# cities.append("Noida")
# cities.append("Delhi")

# cities.insert(1, "Pune")



# x = [1,4,9,16,25, ]


# x = []
# a = 1
# while a < 7:
#     x.append(a*a)
#     a = a + 1
# print(x)

# print(cities)

cities = ["Hyderabad", "Chennai", "Mumbai", "Mumbai", "Kolkota"]
cities_2 = ["Pune", "Noida", "Delhi"]

# cities.append(cities_2)

cities.extend(cities_2)

# cities.remove("Mumbai")
# test_list = [1, 23.6, "Hyderabad", True]

# print(test_list)

print(cities.pop())
print(cities.pop())

print(cities)

