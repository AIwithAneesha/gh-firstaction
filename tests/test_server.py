
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from server import Add
adder = Add()


def test_add():
    assert adder.add(2, 3) == 5
    assert adder.add(-1, 1) == 0
    assert adder.add(0, 0) == 0
    assert adder.add(100, -100) == 0