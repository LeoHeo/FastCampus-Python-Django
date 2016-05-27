# Given an array of integers, we need to find the number of "holes" that need to be filled such that it contains all the integers from some range.
#
# Example
#
# For sequence = [6, 2, 3, 8], the output should be
# makeArrayConsecutive2(sequence) = 3.
#
# We need to add in 4, 5 and 7.
def make_array_consecutive2(sequence):
    max_num = max(sequence)
    min_num = min(sequence)

    median_list = list(filter(
        lambda x: x not in sequence,
        range(min_num, max_num)
    ))

    return len(median_list)


# Consider an array of integers A. Let minA be its minimal element, and let avgA be its mean.
#
# Define the center for the array A as the array B such that:
#
# B is formed from A by erasing some of its elements.
# For each i, |B[i] - avgA| < minA.
# B has the maximal number of elements among all the arrays satisfying the above requirements.
# Given an array of integers, return its center.
#
# Example
#
# For A = [8, 3, 4, 5, 2, 8], the output should be
# arrayCenter(A) = [4, 5].
#
# Here minA = 2, avgA = 5.
#
# For A = [1, 3, 2, 1], the output should be
# arrayCenter(A) = [1, 2, 1].
#
# Here minA = 1, avgA = 1.75.
def arrayCenter(A):
    minA = min(A)
    avgA = sum(A) / float(len(A))


    return [
        num
        for num
        in A
        if num > (avgA-minA) and num < (avgA+minA)
    ]


# Given a sequence of non-negative integers, find its median.
#
# Example
#
# For sequence = [1, 3, 2, 1], the output should be
# arrayMedian(sequence) = 1.5;
# For sequence = [1, 3, 2], the output should be
# arrayMedian(sequence) = 2.
def arrayMedian(sequence):
    sequence.sort()
    arr_len = len(sequence)
    mid = arr_len / 2

    if arr_len % 2 == 0:
        median = (sequence[mid - 1] + sequence[mid]) / 2.0
        return median
    else:
        return sequence[mid]