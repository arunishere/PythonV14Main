#CRUD
#Created
#Data be accessed - indexing
#add more data - Updation
#Delete values
#working with more than one

#Dictonary

cities = {
        'Hyderabad': None, 
         'Ahmedabad' : 27.3, 
         'Mumbai': 22.0, 
         'Chennai': 28.4, 
         'Kochin': 27
         }

cities['Kolkata'] = 30.1
cities['Hyderabad'] = 22.3

# cities.keys()
# cities.values()
# cities.items()
# cities.get('Kolkata')
# cities.popitem()

cities_2 = {'London': None,
            'Dubai' : None,
            'Manila': None,
            'Singapore': None,
            'Paris': None
            }

major_cities_continent = {
                        'Asia': ['Delhi', 'Lahore', 'Dhaka', 'Khatmandu', 'Beiging'],
                        'Europe': ['Bucharest', 'Sicily', 'London', 'Venice'],
                        'NA': ['New Jersey', 'LA'],
                        'Africa': ['Cape Town', 'Cario', 'Addis Ababa']
                        }

print(major_cities_continent['Africa'])