import numpy as np
class Array_new:
  def __init__(self, data):
    self.data = data
    self.shape = (len(data),)
    self.size = np.array(data).size
    self.dim = np.array(data).ndim

  def __str__(self):
    """Returns a list where all the elements are transformed to strings"""
    return np.array([str(x) for x in self.data])

  def __getitem__(self, index):
      if isinstance(index, int):
          # Handle single index subscription
          return self.data[index]
      elif isinstance(index, slice):
          # Handle slicing
          start, stop, step = index.indices(len(self))
          return Array_new(self.data[start:stop:step])  # Create a new Array_new object for the slice
      else:
          raise TypeError("Invalid index type")
  def __len__(self):
    return len(self.data)

  def reshape(self, new_shape):
    size = 1
    for dim in new_shape:
        size *= dim

    if size != len(self.data):
        raise ValueError("Cannot reshape array: incompatible size")

    self.shape = new_shape
    self.data = np.array(self.data).reshape(new_shape)
    return self.data

  def max(self):
      """Returns the maximum value in the array."""
      return max(self.data)

  def min(self):
      """Returns the minimum value in the array."""
      return min(self.data)

  def sum(self):
      """Returns the sum of all elements in the array."""
      return sum(self.data)

  def show(self):
    print(self.data)

  def pop(self):
    a = self.data[-1]
    self.data = self.data[:self.__len__()-1]
    return a

  def insert(self, elt, pos = -1):
    return np.insert(np.array(self.data), pos, elt)
    

  def append(self, NewElt):
    a = [x for x in self.data]
    a.append(NewElt)
    return np.array(a)


  def mean(self):
      """Returns the mean (average) of the array elements."""
      return self.sum() / len(self) if len(self) else 0

  def std(self):
      """Returns the standard deviation of the array elements."""
      mean = self.mean()
      variance = sum([(x - mean) ** 2 for x in self.data]) / len(self)
      return variance ** 0.5
