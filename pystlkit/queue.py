class Queue:
    def __init__(self, maxsize=None):
        """
        Initializes the queue.
        :param maxsize: Maximum number of elements the queue can hold (optional).
        """
        self.queue_list = []
        self.maxsize = maxsize

    def enqueue(self, element):
        """
        Adds an element to the end of the queue.
        :param element: Element to be added to the queue.
        :raises OverflowError: If the queue is full.
        """
        if self.maxsize is not None and len(self.queue_list) >= self.maxsize:
            raise OverflowError("Queue is full")
        self.queue_list.append(element)

    def dequeue(self):
        """
        Removes and returns the front element of the queue.
        :return: The front element of the queue.
        :raises IndexError: If the queue is empty.
        """
        if len(self.queue_list) == 0:
            raise IndexError("Dequeue from empty queue")
        return self.queue_list.pop(0)

    def peek(self):
        """
        Returns the front element of the queue without removing it.
        :return: The front element of the queue.
        :raises IndexError: If the queue is empty.
        """
        if len(self.queue_list) == 0:
            raise IndexError("Peek from empty queue")
        return self.queue_list[0]

    def size(self):
        """
        Returns the number of elements in the queue.
        :return: The size of the queue.
        """
        return len(self.queue_list)

    def is_empty(self):
        """
        Checks if the queue is empty.
        :return: True if the queue is empty, False otherwise.
        """
        return len(self.queue_list) == 0

    def is_full(self):
        """
        Checks if the queue is full.
        :return: True if the queue is full, False otherwise.
        """
        return self.maxsize is not None and len(self.queue_list) >= self.maxsize

    def clear(self):
        """
        Clears all elements from the queue.
        """
        self.queue_list = []

    def to_list(self):
        """
        Returns a list representation of the queue.
        :return: A list containing the elements of the queue.
        """
        return self.queue_list.copy()

    def get_max(self):
        """
        Returns the maximum element in the queue.
        :return: The maximum element in the queue.
        :raises ValueError: If the queue is empty.
        """
        if self.is_empty():
            raise ValueError("Max from empty queue")
        return max(self.queue_list)

    def get_min(self):
        """
        Returns the minimum element in the queue.
        :return: The minimum element in the queue.
        :raises ValueError: If the queue is empty.
        """
        if self.is_empty():
            raise ValueError("Min from empty queue")
        return min(self.queue_list)
