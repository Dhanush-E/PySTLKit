class Stack:
    def __init__(self, maxsize=None):
        """
        Initializes the stack.
        :param maxsize: Maximum number of elements the stack can hold (optional).
        """
        self.stack_list = []
        self.maxsize = maxsize

    def push(self, element):
        """
        Pushes an element onto the stack.
        :param element: Element to be added to the stack.
        :raises OverflowError: If the stack is full.
        """
        if self.maxsize is not None and len(self.stack_list) >= self.maxsize:
            raise OverflowError("Stack is full")
        self.stack_list.append(element)

    def pop(self):
        """
        Removes and returns the top element of the stack.
        :return: The top element of the stack.
        :raises IndexError: If the stack is empty.
        """
        if len(self.stack_list) <= 0:
            raise IndexError("Pop from empty stack")
        return self.stack_list.pop()

    def peek(self):
        """
        Returns the top element of the stack without removing it.
        :return: The top element of the stack.
        :raises IndexError: If the stack is empty.
        """
        if len(self.stack_list) <= 0:
            raise IndexError("Peek from empty stack")
        return self.stack_list[-1]

    def size(self):
        """
        Returns the number of elements in the stack.
        :return: The size of the stack.
        """
        return len(self.stack_list)

    def is_empty(self):
        """
        Checks if the stack is empty.
        :return: True if the stack is empty, False otherwise.
        """
        return len(self.stack_list) == 0

    def is_full(self):
        """
        Checks if the stack is full.
        :return: True if the stack is full, False otherwise.
        """
        return self.maxsize is not None and len(self.stack_list) == self.maxsize

    def clear(self):
        """
        Clears all elements from the stack.
        """
        self.stack_list = []

    def to_list(self):
        """
        Returns a list representation of the stack.
        :return: A list containing the elements of the stack.
        """
        return self.stack_list.copy()

    def get_max(self):
        """
        Returns the maximum element in the stack.
        :return: The maximum element in the stack.
        :raises ValueError: If the stack is empty.
        """
        if self.is_empty():
            raise ValueError("Max from empty stack")
        return max(self.stack_list)

    def get_min(self):
        """
        Returns the minimum element in the stack.
        :return: The minimum element in the stack.
        :raises ValueError: If the stack is empty.
        """
        if self.is_empty():
            raise ValueError("Min from empty stack")
        return min(self.stack_list)