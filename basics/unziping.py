# Unzip Back to Two Lists

# Because this teaches the reverse process (zip(*pairs)), which is the trickiest part of this section.
# pairs = [("a", 1), ("b", 2), ("c", 3)]
# turn it into :
# ["a", "b", "c"]
# [1, 2, 3]

pairs = [("a", 1), ("b", 2), ("c", 3)]
letters, nums = zip(*pairs)
print(list(letters), list(nums))
