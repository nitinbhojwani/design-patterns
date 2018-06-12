def test():
    import unittest
    from creational.singleton.test_singleton import TestSingleton
    test_cases = [
        TestSingleton
    ]

    suites = [unittest.defaultTestLoader.loadTestsFromTestCase(
        test_case) for test_case in test_cases]
    all_tests_suite = unittest.TestSuite(suites)
    runner = unittest.TextTestRunner()
    runner.run(all_tests_suite)


test()
