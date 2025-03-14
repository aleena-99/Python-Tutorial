from collections import Counter

def remove_all_duplicates(lst):
    counts = Counter(lst)
    return [x for x in lst if counts[x] == 1]

print(remove_all_duplicates([1, 2, 2, 3, 4, 4, 5]))
