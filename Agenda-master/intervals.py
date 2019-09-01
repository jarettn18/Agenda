"""Intervals are like a list of integers"""
import unittest
import typing

class Interval:

    def __init__(self,low: int,high: int):
        self.low = min(low, high)
        self.high = max(high, low)

    def __str__(self) -> str:
        return f"{self.low}--{self.high}"

    def __gt__(self, other: "Interval") -> bool:
        return self.low >= other.high

    def __ge__(self, other: "Interval") -> bool:
        return self.low >= other.high

    def __eq__(self,other: "Interval") -> bool:
        if self.high == other.high and self.low == other.low:
            return True

    def overlap(self, other: "Interval") -> bool:
        """Overlaps if they share at least 1 point"""
        if self > other:
            return False
        if other > self:
            return False
        return True

    def has_overlaps(l: "list[Interval]") -> bool:
        for i in range(len(l)):
            i_elem = l[i]
            for j in range(i+1,len(l)):
                j_elem = l[j]
                if i_elem.overlap(j_elem):
                    return True
        return False


class TestInterval(unittest.TestCase):

    def test_gt(self):
        i = Interval(5,12)
        j = Interval(13,17)
        self.assertTrue(j > i)
        self.assertFalse(i > j)
        k = Interval(12,17)
        self.assertTrue(k > i)

    def test_ge(self):
        i = Interval(5,12)
        j = Interval(13,17)
        self.assertTrue(j >= i)
        self.assertFalse(i >= j)
        k = Interval(12,17)

    def test_overlap(self):
        i = Interval(5,12)
        j = Interval(13,17)
        k = Interval(12,17)
        k2 = Interval(17,12)
        self.assertFalse(j.overlap(i))
        self.assertFalse(k2.overlap(i))

    def test_equal(self):
        i = Interval(5,12)
        j = Interval(13,17)
        k = Interval(12,17)
        k2 = Interval(17,12)
        self.assertFalse(i == k)
        self.assertTrue(i == i)

class TestOverlap(unittest.TestCase):

    def test_they_should(self):
        l1 = [Interval(5,7), Interval(3,2), Interval(7,9)]
        self.assertTrue(has_overlaps(l1))

unittest.main()