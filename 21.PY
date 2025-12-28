import random
arr = [[random.randint(1, 100) for x in range(3)] for x in range(4)]
sorted_arr = [sorted(row) for row in arr]
mean_rows = [sum(row) / len(row) for row in arr]

print("Original Array:", arr)
print("Sorted Array:", sorted_arr)
print("Mean of each row:", mean_rows)