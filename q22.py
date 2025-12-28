#Create a random 4x4 list of lists and extract the diagonal elements.

import random
arr = [[random.randint(0,100) for x in range(4)] for x in range(4)]
diagonal_elements = [arr[i][i] for i in range(4)]
print("Array:", arr)
print("Diagonal Elements:", diagonal_elements)
