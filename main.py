# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.
# Array of integers ie: [ 4, 5, 6, 7, 3, 6]

def functional(array):
    newarray = []
    array.sort(reverse=True)
    print(array)

# functional ([ 3, 8, 9, 2])

# Object Oriented Prompt

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    
    def repair(self):
        self.condition = 'repaired'
        
# Define a repair() method that will update the condition of the podracer to "repaired".
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def boost(self):
        self.max_speed = self.max_speed*2


# Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

class SebulbasPod(AnakinsPod):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self):
        self.condition = 'trashed'