class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, value):
        if value in self.q:
            print("you added same element many times")
        else:
            self.q.append(value)

    def dequeue(self):
        if self.isEmpty():
            print("the list is empty")
        else:
            return self.q.pop(0)

    def front(self):
        if self.isEmpty():
            return None
        return self.q[0]

    def isEmpty(self):
        return len(self.q) == 0


queue = Queue()
queue.enqueue(10)
queue.enqueue(10)   # uyarı verecek
print(queue.front())  # 10
queue.dequeue()
print(queue.isEmpty())  # True
