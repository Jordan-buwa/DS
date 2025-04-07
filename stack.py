# Add features to handle linked lists

class Stack:
    def __init__(self, para):
      self.stack = para
      pass

    def push(self,newElement, index = 0):
      """This insert an element at a specific position. The default position is 0"""
      if type(self.stack) == Array_new:
        self.stack.insert(index,newElement)
        return self.stack
      if type(self.stack) == LinkedList:
        self.stack.InsertAtPos(newElement, index)


    def peek(self):
      """Return the last element of the stack"""
      return self.stack[-1]

    def pop(self, index = -1):
      """Delete and return the last element (default value) of the stack"""
      if type(self.stack) == Array_new:
        self.stack.pop(index)
        return self.stack[index]

      if type(self.stack) == LinkedList:
        self.stack.deleteItem(index)
        return self.stack.access(index)

    # Checks if the stack is empty
    def isEmpty(self):
      return self.size == 0

    # Size of the stack
    def size(self):
      if type(self.stack) == LinkedList:
        return self.stack.get_length()
      if type(self.para) == Array_new:
        return self.stack.__len__()

    # Stack display
    def display_stack(self):
      if type(self.stack) == LinkedList:
        self.stack.display()
      if type(self.stack) == Array_new:
        self.stack.show()

