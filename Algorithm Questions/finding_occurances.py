'''
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a substring of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution

'''


def find_max(t, z):

    # We will find all the possible substrings
    max_value = 0
    for i in range(len(t)):
        for j in range(i + 1, len(t) + 1):
            substring = t[i:j]
            count_in_z = z.count(substring)
            value = len(substring) * count_in_z
            
            if value > max_value:
                max_value = value
    
    return max_value

if __name__ == '__main__':
    result = find_max("acldm1labcdhsnd", "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")
    print(result)
