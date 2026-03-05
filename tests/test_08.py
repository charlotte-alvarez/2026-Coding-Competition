# Test file for problem 08
from problems.problem_08.problem import answer

tests = [
        [359999, "99:59:59"],
        [0, "00:00:00"],
        [1, "00:00:01"],
        [59, "00:00:59"],
        [60, "00:01:00"],
        [78, "00:01:18"],
        [3661, "01:01:01"],
        [12345, "03:25:45"],
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
