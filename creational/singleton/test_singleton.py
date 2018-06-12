import unittest
from . import singleton_logger


class TestSingleton(unittest.TestCase):
    def setUp(self):
        self.logger1 = singleton_logger.Logger()
        self.logger2 = singleton_logger.Logger()

    def test_singleton(self):
        self.assertTrue(self.logger1 is self.logger2)

        log_lines = [
            'Hi',
            'My Name is Nitin',
            'Goodbye'
        ]
        self.logger1.log(log_lines[0])
        self.logger2.log(log_lines[1])
        self.logger1.log(log_lines[2])
        self.assertEqual(self.logger1.get_logs(), log_lines)
        self.assertEqual(self.logger2.get_logs(), log_lines)

    def tearDown(self):
        del self.logger1
        del self.logger2
