def add (a, b):
    return a + b

def multiply(a,b):
    return a*b

def is_even(n):
    return n%2==0

def subtract(a, b):
    return a - b

def max_of_three(a, b, c):
    return max(a, b, c)

def is_palindrome(s):
    s = s.replace(" ", "")
    return s == s[::-1]

def find_min(numbers):
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result
