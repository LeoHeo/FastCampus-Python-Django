# set
# If that value is not present, discard() does nothing, but remove() will raise a KeyError exception.
# >>> test_set = {1, 2}
# >>> test_set.discard(5)
# >>> test_set.remove(5)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 5


# >> a = {2, 4, 5, 9}
# >> b = {2, 4, 11, 12}
# >> a.union(b) # Values which exist in a or b
# {2, 4, 5, 9, 11, 12}
# >> a.intersection(b) # Values which exist in a and b
# {2, 4}
# >> a.difference(b) # Values which exist in a but not in b
# {9, 5}
# all difference set
# >> a ^ b
# {5, 9, 11, 12}

# >> a.union(b) == b.union(a)
# True
# >> a.intersection(b) == b.intersection(a)
# True
# >> a.difference(b) == b.difference(a)
# False

a = {2, 4, 5, 9}
b = {2, 4, 11, 12}


print("\n".join(
    list(
        map(
            str,
            sorted(a ^ b)
        )
    )
))
