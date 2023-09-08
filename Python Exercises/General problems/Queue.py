class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def rear(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            return None

    def size(self):
        return len(self.queue)
