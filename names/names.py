import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name1 in names_1:
#     for name2 in names_2:
#         if name1 == name2:
#             duplicates.append(name1)

names_1.sort()

mid = names_1[5000]

for name2 in names_2:
    if name2 < mid:
        if name2 in names_1[:5000]:
            duplicates.append(name2)
    elif name2 >= mid:
        if name2 in names_1[5000:]:
            duplicates.append(name2)
          



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
