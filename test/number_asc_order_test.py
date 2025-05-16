import sys
import os
from unittest.mock import MagicMock
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from custom_stack_class import CustomStack
from number_asc_order import NumberAscOrder

def test_sort_with_six_random_numbers():
    elements = [34, 7, 23, 1, 56, 12]
    stack = MagicMock()
    stack.is_empty.side_effect = lambda: len(elements) == 0
    stack.pop.side_effect = lambda: elements.pop()
    sorter = NumberAscOrder()
    result = sorter.sort(stack)
    assert result == [1, 7, 12, 23, 34, 56]

def test_sort_with_empty_stack():
    stack = MagicMock()
    stack.is_empty.return_value = True
    sorter = NumberAscOrder()
    result = sorter.sort(stack)
    
    assert result == []