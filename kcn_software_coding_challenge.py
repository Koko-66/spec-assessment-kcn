## SECTION 2 ##
"""2.1 A) Write a function that takes in a string and returns the number of unique consonants [10 marks]

EXAMPLE INPUT: “cat”
EXAMPLE OUTPUT: 2 (‘c’ and ‘t’ are both unique)

EXAMPLE INPUT: “cataract”
EXAMPLE OUTPUT: 1 (‘r’ is the only unique consonant)"""

"""B) What is the time and space complexity of your solution?
If you are making any assumptions in your calculations, list them. [2 marks]
"""

from collections import Counter

def get_consonant_count(input_string):
    #get dictionary with all letters
    letter_count = Counter(input_string)

    # set counter to 0
    consontants = 0
    # iterate through the dict to filter consonants that are unique
    # assuming only alphabetic input
    for key, value in letter_count.items():
        if key not in "aeiou" and value == 1:
            consontants += 1
    return consontants

# print(get_consonant_count("cat"))
# print(get_consonant_count("cataract"))

"""B) What is the time and space complexity of your solution?
If you are making any assumptions in your calculations, list them. [2 marks]

The Counter function has a complexity of O(n) because it needs to iterate through the list to create a dictonary.
Similarly, the for loop in the program checking whether the result is unique and is a consonant is also of similar complexity O(n). In terms of space complexity, since function creates a dictionary that will increase with the length of the input string, it will also be that of O(n). In summary, the worst case of this function is
"""

"""
2.2 Write a function that finds how many squares are in a X by X grid.
For example a 2x2 Grid has 5 squares as shown below:
"""

def find_squares(n): # n = no of squares in the grid

    # base case
    if n == 1:
        return n
    else:
        # calculate the current grid (e.g. 2*2 and add to the 
        # previous calculated recursively)
        return (n*n) + find_squares(n-1)

print(f"1x1 grid has {find_squares(1)} square")
print(f"2x2 grid has {find_squares(2)} squares")
print(f"3x3 grid has {find_squares(3)} squares")
print(f"4x4 grid has {find_squares(4)} squares")


## SECTION 3 ##

"""3.1 
Design a basic hash function, keeping in mind memory constraints
and how you would deal with hash collisions.


"""
# A basic function using remainder method 

hash_table = [0] * 11

def hash_function(input_value, table_size):
    letter_list = []
    for s in input_value:
        letter_list.append(ord(s))
        converted = sum(letter_list)

    _hash = converted % table_size

    if  hash_table[_hash] != 0:
        _hash = (converted % table_size) + 1
        hash_table[_hash] = input_value
    else:  
        hash_table[_hash] = input_value

"""
3.2. 
Assuing we are trying to has the letter "a" this will get converted to a number using a remainder method - the value we get from conversion to integer is divided by the number of slots in the hash table and the place calculated. 
3.3. When the collion happens, the function will rehash the input adding 1 to its value and should check if that slot is already taken - this should be repeated until an empty slot is found, but also the loop should be broken if the whole table has been checked already. This loop has not been fully implemented due to time constraints).
"""
print(hash_function("abc", 11))
print(hash_table)
print(hash_function("cab", 11))
print(hash_table)
print(hash_function("cba", 11))

## SECTION 4 ##
## CODING CHALLENGE
# 25 MARKS
"""
A] Design a parent class called Planet

It must have:
- General attributes: name, distance_from_sun, planet_type
- A get_distance_to_earth() method that gives you the absolute distance from the Earth.

!!! You can take the distance from the Sun to the Earth as 147 million kilometres !!!

For example, if the planet’s distance_from_sun was 148 million kilometres when you call the get_distance_from_earth()
method, it should give us the distance like this: {'distance to earth’': 1000000} where the implied unit is kilometres.
This means that the planet is 1 million kilometres away from Earth.

   > This question uses an oversimplification of the solar system model, not taking into account orbit position or the
    eccentricity of the orbit, so in reality the result will be an approximate value with a reasonable margin of error.
"""

class Planet:

    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun 
        self.planet_type = planet_type

    def get_distance_from_earth(self):
        distance = abs(self.distance_from_sun - 147000000)
        return {'distance to earth': distance}
    
    
"""
B] Design a child class called Mercury, which inherits from the Planet class.
This class should have exactly the same attributes as its parent class,
Your child class should also have a static method called happy_new_year(), which
would give us the information on how long a year lasts on the planet (in whatever way you wish!). 
You can take Earth Days as the implied unit.

After, create a Mercury object and print out the value of all its attributes and methods.

!!! HELPFUL INFO ABOUT MERCURY !!!
Distance from Sun: 58 million
Planet Type: Terrestrial
Time taken for the planet to orbit the sun: 88 Earth days
!!!!!!!!!!!!!!!!!!!!

"""
class Mercury(Planet):
    
    @staticmethod
    def happy_new_year():
        year_length = 88
        return f"A year on Mercury lasts {year_length} Earth days"
    
## TEST CASE
pass
mercury = Mercury("Mercury", 58000000, "Terrestrial")
print(mercury.name, mercury.planet_type, mercury.distance_from_sun, mercury.get_distance_from_earth(), mercury.happy_new_year())

"""
C] Design a child class called Jupiter, which inherits from the Planet class.
This class should have exactly the same attributes as its parent class, as well as the additional attribute 
number_of_moons.
Your child class should also have a static method called happy_new_year(), which would give us the information on how 
long a year lasts on the planet (in whatever way you wish!). You can take Earth Days as the implied unit.

After, create a Jupiter object and print out the value of all its attributes and methods.


!!! HELPFUL INFO ABOUT JUPITER !!!
Distance from Sun: 779 million
Planet Type: Gas Giant
Time taken for the planet to orbit the sun: 4383 Earth days
Number of Moons: 80
!!!!!!!!!!!!!!!!!!!!

"""
class Jupiter(Planet):

    def __init__(self, name, distance_from_sun, planet_type, number_of_moons):
        Planet.__init__(self, name, distance_from_sun, planet_type)
        self.number_of_moons = number_of_moons

    @staticmethod
    def happy_new_year():
        year_length = 4383
        return f"A year on Jupyter lasts {year_length} Earth days"


## TEST CASE
jupiter = Jupiter("Jupiter", 779000000, "Gas Giant", 80)

print(jupiter.name, jupiter.planet_type, jupiter.distance_from_sun, jupiter.number_of_moons, jupiter.get_distance_from_earth(), jupiter.happy_new_year())