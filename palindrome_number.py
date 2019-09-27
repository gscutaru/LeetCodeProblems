"""
Determine whether an integer is a palindrome. An integer is a palindrome when it
reads the same backward as forward.
"""

def isPalindrome(x):
    x_s = str(x)
    if x_s == x_s[::-1]:
        return True
    return False

print(isPalindrome(120121))
