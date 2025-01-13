# sorting and reversing
# ---------------------
# reverse() and sort() do not return a list
# they manipulate the list in same place
# -----------------------------------------
# sorted() returns a new sorted list
# and keeps the original list unchanged

print()
# original list ----------------
lst = [10, 2, 0, 50, 4]
print(lst)

print()
# reverse() ----------------
lst.reverse()
print(lst)

print()
# sort() ----------------
lst.sort()
print(lst)

print()
# reverse in sort() ----------------
lst.sort(reverse=True)
print(lst)

print()
# sorted() ----------------
lst = [10, 2, 0, 50, 4]
x = sorted(lst)
print(x)
print(lst)

print()
# reverse in sorted() ----------------
lst = [10, 2, 0, 50, 4]
x = sorted(lst, reverse=True)
print(x)
print(lst)

print()
# reversed() ----------------
lst = [10, 2, 0, 50, 4]
print(list(reversed(lst)))

print()
# reversing using slicing ----------------
lst = [10, 2, 0, 50, 4]
x = lst[4:2:-1]
print(x)

y = lst[::-1]
print(y)
print(lst)


# examples
# ----------------------------------------------------------------------------------

# reversing a list using for loop
lst_numbers = [1, 2, 3, 4, 5]
length_lst_numbers = len(lst_numbers)
for index in range(0, length_lst_numbers - 1):
    if index < length_lst_numbers // 2:
        lst_numbers[index], lst_numbers[length_lst_numbers-1-index] = \
            lst_numbers[length_lst_numbers-1-index], lst_numbers[index]
print(lst_numbers)
