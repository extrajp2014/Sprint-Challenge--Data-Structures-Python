import time

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value > self.value:
            if not self.right:
                self.right =BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif (self.value < target) and self.right:
            return self.right.contains(target)
        elif (target < self.value) and self.left:
            return self.left.contains(target)
        else:
            return False

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

print("-------------Original--------------")
start_time = time.time()
duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
# runtime: 9.031611204147339 seconds

end_time = time.time()
duplicates.sort()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

print("\n--------------Improved Version--------------")
start_time = time.time()
duplicates = []
# create tree
tree = BinarySearchTree(names_1[0])
for name_1 in names_1:
    tree.insert(name_1)
# search tree
for name_2 in names_2:
    if tree.contains(name_2):
        duplicates.append(name_2)
# runtime: 0.1669931411743164 seconds

end_time = time.time()
duplicates.sort()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
