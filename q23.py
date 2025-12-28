#Count the number of occurrences of a specific value in a list.

import random
arr = list(random.randint(1,10) for x in range(10))
print(arr)
print(count := arr.count(5))