# Sets are used to store an unordered  collection of unique data
# Support fast search,
set = {0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, "done"}
print(type(set))
print(set)

set.add("wow")

print(set)

age = {20, 22, 34, "Jack"}
students = {"Adam", "Henry", "Lisa", "Jack"}

u = age.union(students)
print(u)

i = age.intersection(students)
print(i)

u.pop()
u.remove("Jack")
