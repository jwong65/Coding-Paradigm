# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.
# Array of integers ie: [ 4, 5, 6, 7, 3, 6]

def functional(array):
    newarray = []
    array.sort(reverse=True)
    print(array)

functional ([ 3, 8, 9, 2])