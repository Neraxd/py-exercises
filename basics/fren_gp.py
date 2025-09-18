# Friend Groups

# Print all unique friends (union).

# Print friends in both groups (intersection).

# Print friends only in group1.

group1 = {"Eric", "John", "Terry"}
group2 = {"Terry", "Graham", "Brian"}


print("union: " , group1.union(group2) , group1 | group2 )
print("intersection: ", group1.intersection(group2) , group1 & group2 )
print("difference: " , group1.difference(group2) , group1 - group2 )
