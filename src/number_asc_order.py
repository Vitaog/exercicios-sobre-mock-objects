from src.custom_stack_class import CustomStack, StackEmptyException

class NumberAscOrder:
    def sort(self, stack: CustomStack) -> list:
        if stack.is_empty():
            return []

        sorted_numbers = []
        while not stack.is_empty():
            try:
                sorted_numbers.append(stack.pop())
            except StackEmptyException:
                break

        return sorted(sorted_numbers)
