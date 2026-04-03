import unittest
from http-client.core import Processor

class TestProcessor(unittest.TestCase):
    def test_process(self):
        p = Processor()
        result = p.process({{"key": "value"}})
        self.assertEqual(result["status"], "ok")