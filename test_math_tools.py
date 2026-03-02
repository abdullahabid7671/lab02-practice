# test_math_tools.py
from math_tools import add, multiply, is_even, subtract, max_of_three, is_palindrome, find_min, remove_duplicates 

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("test_add: ALL PASSED")

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0
    print("test_multiply: ALL PASSED")

def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    print("test_is_even: ALL PASSED")

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 4) == -4
    assert subtract(-2, -3) == 1
    print("test_subtract: ALL PASSED")
    
def test_max_of_three():
    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(10, 5, 7) == 10
    assert max_of_three(-1, -5, -3) == -1
    assert max_of_three(4, 4, 2) == 4   # two equal
    assert max_of_three(6, 6, 6) == 6   # all equal
    print("test_max_of_three: ALL PASSED")

def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True           # empty
    assert is_palindrome("a") == True          # single char
    assert is_palindrome("nurses run") == True # with space
    print("test_is_palindrome: ALL PASSED")



def test_find_min():
    assert find_min([5, 3, 8, 1]) == 1
    assert find_min([10, 20, 30]) == 10  # catches min_val=0 bug
    assert find_min([-5, -2, -10]) == -10
    print("test_find_min: ALL PASSED")


def test_remove_duplicates():
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([1, 2, 1, 3, 2]) == [1, 2, 3]
    assert remove_duplicates(["a", "a", "b"]) == ["a", "b"]
    assert remove_duplicates([1, "1", 1]) == [1, "1"]  # mixed types
    print("test_remove_duplicates: ALL PASSED")

# Run all tests
test_add()
test_multiply()
test_is_even()
test_subtract()
test_max_of_three()
test_is_palindrome()
test_find_min()
test_remove_duplicates()
print("--- All tests passed! ---")