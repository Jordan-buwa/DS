class Queue:
  N = 10
  def __init__(self, para = []):
    self.queue = para

  def enqueue(self,new):
    if not self.isFull():
      self.queue.append(new)
    else:
      print("The queue is full")
  def isNull(self):
    return len(self.queue) == 0
  def dequeue(self):
    if not self.isNull():
      self.queue.pop()
    else:
      print("The queue is empty")
  def rear(self):
    return self.queue[-1] if not self.isNull() else None
  def peek(self):
    return self.queue[0] if not self.isNull() else None
  def isFull(self):
    return len(self.queue) == self.__class__.N

  def display_queue(self):
        print(self.queue)
