# For an integer k rearrange all the elements of the given array in such way, that:

# all elements that are less than k are placed before elements that are not less than k;
# all elements that are less than k remain in the same order with respect to each other;
# all elements that are not less than k remain in the same order with respect to each other.
# Example

# For k = 5 and elements = [1, 3, 5, 7, 6, 4, 2], the output should be
# splitByValue(k, elements) = [1, 3, 4, 2, 5, 7, 6].

# [input] integer k
# [input] array.integer elements
# [output] array.integer
def splitByValue(k, elements):
    if k == 0:
        return elements 
    
    k_great_list = list( filter( 
            lambda x: k > x,
            elements
        )
     )
    
    k_less_list = list(filter(
            lambda x: k <= x,
            elements
    ))
    
    return k_great_list + k_less_list


# A ciphertext alphabet is obtained from the plaintext alphabet by means of rearranging some characters. For example "bacdef...xyz" will be a simple ciphertext alphabet where a and b are rearranged.

# A substitution cipher is a method of encoding where each letter of the plaintext alphabet is replaced with the corresponding (i.e. having the same index) letter of some ciphertext alphabet.

# Given two strings, check whether it is possible to obtain them from each other using some (possibly, different) substitution ciphers.

# Example

# For string1 = "aacb" and string2 = "aabc", the output should be
# isSubstitutionCipher(string1, string2) = true.
# Any ciphertext alphabet that starts with acb... would make this transformation possible.

# For string1 = "aa" and string2 = "bc", the output should be
# isSubstitutionCipher(string1, string2) = false.
# [input] string string1

# A string consisting of lowercase characters.

# [input] string string2

# A string consisting of lowercase characters of the same length as string1.

# [output] boolean
def isSubstitutionCipher(string1, string2):
    first = set(string1)
    second = set(string2)
    
    return len(first) == len(second)
