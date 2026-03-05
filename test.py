# This file is used to run automated tests against the functions in each problem

# **WARNING**: This file should **NOT** be edited. It has been specially crafted to run specific assertions against problem functions. Editing this file could break the competition.

# Note: Find a backup of this file in the Backups directory

from sys import argv

from tests.test_01 import test as t1
from tests.test_02 import test as t2
from tests.test_03 import test as t3
from tests.test_04 import test as t4
from tests.test_05 import test as t5
from tests.test_06 import test as t6
from tests.test_07 import test as t7
from tests.test_08 import test as t8

all_tests = [t1, t2, t3, t4, t5, t6, t7, t8]


def run_tests(problem_number: int = None) -> None:
    """
    Run automated tests aginst the problem suite.

    Prints if you have a problem correct or not.

    Args:
        problem_number(int): Only run tests against this problem number

    Return:
        None
    """
    if problem_number:
        c, t = all_tests[problem_number - 1]()
        print(f"You got {c} tests passing out of {t}")
    else:
        run_all_tests()


def run_all_tests() -> None:
    """
    Run all tests. Print the correct / total tests

    Args:
        None
    Returns:
        None
    """
    correct = 0
    total = 0
    for test in all_tests:
        c, t = test()
        correct += c
        total += t

    print(f"You got {correct} tests passing out of {total}")


if __name__ == "__main__":
    num = None
    try:
        num = int(argv[1])
    except Exception:
        pass
    run_tests(num)
