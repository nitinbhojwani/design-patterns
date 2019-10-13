import unittest
from creational.singleton.test_singleton import TestSingleton
from creational.builder.test_house_builder import TestHouseBuilder


def test():
    test_cases = [
        TestSingleton,
        TestHouseBuilder
    ]

    suites = [unittest.defaultTestLoader.loadTestsFromTestCase(
        test_case) for test_case in test_cases]
    all_tests_suite = unittest.TestSuite(suites)
    runner = unittest.TextTestRunner()
    runner.run(all_tests_suite)


test()
