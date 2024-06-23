# Creating sets for demonstration
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

# i) add() - Adds an element to the set
set1.add(4)
print("After add(4):", set1)

# ii) update() - Updates the set with the union of itself and others
set1.update([5, 6])
print("After update([5, 6]):", set1)

# iii) copy() - Returns a shallow copy of the set
set_copy = set1.copy()
print("Copy of set1:", set_copy)

# iv) pop() - Removes and returns an arbitrary set element
popped_element = set1.pop()
print("Popped element:", popped_element)
print("After pop():", set1)

# v) remove() - Removes a specified element (raises KeyError if not found)
set1.remove(2)
print("After remove(2):", set1)

# vi) discard() - Removes a specified element (does nothing if not found)
set1.discard(3)
print("After discard(3):", set1)
set1.discard(10)  # 10 is not in the set, so nothing happens
print("After discard(10):", set1)

# vii) clear() - Removes all elements from the set
set1.clear()
print("After clear():", set1)

# Resetting sets for further demonstrations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

# viii) union() - Returns the union of sets as a new set
union_set = set1.union(set2, set3)
print("Union of set1, set2, set3:", union_set)

# ix) intersection() - Returns the intersection of sets as a new set
intersection_set = set1.intersection(set2, set3)
print("Intersection of set1, set2, set3:", intersection_set)

# x) difference() - Returns the difference of sets as a new set
difference_set = set1.difference(set2, set3)
print("Difference of set1 with set2 and set3:", difference_set)
