import pytest
from src.custom_stack_class import CustomStack, StackEmptyException, StackFullException

def test_push_and_top():
    stack = CustomStack(3)
    stack.push(10)
    assert stack.top() == 10
    stack.push(20)
    assert stack.top() == 20

def test_push_until_full_then_exception():
    stack = CustomStack(2)
    stack.push(1)
    stack.push(2)
    with pytest.raises(StackFullException):
        stack.push(3)

def test_pop_returns_last_and_reduces_size():
    stack = CustomStack(2)
    stack.push(100)
    stack.push(200)
    assert stack.pop() == 200
    assert stack.pop() == 100
    assert stack.size() == 0

def test_pop_from_empty_stack_raises_exception():
    stack = CustomStack(1)
    with pytest.raises(StackEmptyException):
        stack.pop()

def test_top_from_empty_stack_raises_exception():
    stack = CustomStack(1)
    with pytest.raises(StackEmptyException):
        stack.top()

def test_is_empty_and_size():
    stack = CustomStack(5)
    assert stack.is_empty() is True
    stack.push(42)
    assert stack.is_empty() is False
    assert stack.size() == 1
