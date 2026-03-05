# Test file for problem 06
from problems.problem_06.problem import answer

tests = [
    ["a1 2b 4d 3e", "a1 2b 3e 4d"],
    ["is2 Thi1s T4est 3a", "Thi1s is2 3a T4est"],
    ["c1oding 2is 3fun", "c1oding 2is 3fun"],
    ["hello1", "hello1"],
    ["", ""]
]

def test() -> tuple:
    """ 
    Test for problem. 

    Args:
        None

    Returns:
        tuple: The number of passing tests, the total number of tests
    """

    correct = 0
    num_tests = len(tests)
    for test in tests:
        if test_func(test[0], test[1]):
            correct += 1

    return (correct, num_tests)
    

def test_func(input, output) -> bool:
    try:
        assert answer(input) == output
        return True
    except AssertionError, Exception:
        return False


if __name__ == "__main__":
    test()
