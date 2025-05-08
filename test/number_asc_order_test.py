import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from custom_stack_class import CustomStack
from number_asc_order import NumberAscOrder

def test_sort_with_six_random_numbers():
    stack = CustomStack(6)
    for number in [34, 7, 23, 1, 56, 12]:
        stack.push(number)

    sorter = NumberAscOrder()
    result = sorter.sort(stack)
    
    assert result == [1, 7, 12, 23, 34, 56]

def test_sort_with_empty_stack():
    stack = CustomStack(6)
    sorter = NumberAscOrder()
    result = sorter.sort(stack)
    
    assert result == []