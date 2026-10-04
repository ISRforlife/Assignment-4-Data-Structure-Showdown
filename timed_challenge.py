# Timed Challenge #7: First Repeated Value
# Return the first value that repeats in the collection.
# Input: [1, 4, 3, 5, 3, 2, 1]
# Output: 3


def first_repeated_value(values):
    # A set lets me quickly keep track of values I have already seen.
    seen = set()

    for value in values:
        if value in seen:
            return value

        seen.add(value)

    # Return None if nothing repeats
    return None


# Tests
if __name__ == "__main__":
    print(first_repeated_value([1, 4, 3, 5, 3, 2, 1]))  # 3
    print(first_repeated_value([1, 2, 3, 4]))            # None
    print(first_repeated_value([]))                      # None
    print(first_repeated_value([5, 5]))                  # 5
    print(first_repeated_value(["a", "b", "a"]))         # a
