import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import report

def row(h, secs):
    return {"host": h, "boot_seconds": str(secs)}

class TestBootTime(unittest.TestCase):
    def test_slow(self):
        self.assertEqual(report([row("PC-1", 180)])[0][2], "SLOW")
    def test_ok(self):
        self.assertEqual(report([row("PC-1", 45)])[0][2], "OK")
    def test_exactly_at_threshold_ok(self):
        self.assertEqual(report([row("PC-1", 120)])[0][2], "OK")
    def test_custom_threshold(self):
        self.assertEqual(report([row("PC-1", 90)], threshold=60)[0][2], "SLOW")
    def test_slowest_first(self):
        r = report([row("A", 45), row("B", 300)])
        self.assertEqual(r[0][0], "B")
