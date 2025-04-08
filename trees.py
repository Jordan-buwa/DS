class BinaryTree(Node):
  def __init__(self, value = None, l = None, r = None):
    self.root = self
    Node.__init__(self, value, l, r)
  
  def __str__(self) -> str:
    return str(self.value)

  def pre_order(self):
    if not self:
      return
    tem = self.root
    print(tem.value)
    if tem.left:
      tem.left.pre_order()
    if tem.right:
      tem.right.pre_order()
  def in_order(self):
    if not self:
      return
    tem = self.root
    if tem.left:
      tem.left.in_order()
    print(tem.value)
    if tem.right:
      tem.right.in_order()
  
  def post_order(self):
    if not self:
      return
    tem = self.root
    if tem.left:
      tem.left.post_order()
    if tem.right:
      tem.right.post_order()
    print(tem.value) 

  def search_node(self, target):
    if not self.root:
      return False
    if self.value == target:
      return True
    # Calling search_node on children.
    if self.left and self.left.search_node(target):
      return True
    if self.right and self.right.search_node(target):
      return True
    return False 

  def search_BST(self, target):
    if not self.root:
      return False
    if self.value == target:
      return True
    if target < self.value and self.left: return self.left.search_BST(target)
    elif target >= self.value and self.right: return self.right.search_BST(target)
    return False

  def addnode(self, data):
    newNode = BinaryTree(data)
    if self.root is None:
      self.root = newNode
      return

    current = self.root
    while True:
      if data < current.value:
        if current.left is None:
          current.left = newNode
          return
        current = current.left
      else:
        if current.right is None:
          current.right = newNode
          return
        current = current.right

        
def delete_node_bst(root, key):

  def find_min(node):
    current = node
    while current.left is not None:
      current = current.left
    return current

  def find_max(node):
    current = node
    while current.right is not None:
      current = current.right
    return current

    if not root:
      return root

  if key < root.value:
      root.left = delete_node_bst(root.left, key)
  elif key > root.value:
      root.right = delete_node_bst(root.right, key)
  else:  # Key is equal to root's data (node to be deleted)
      # Case 1: Leaf node
      if root.left is None and root.right is None:
          root = None
      # Case 2: Node with one child
      elif root.left is None:
          root = root.right
      elif root.right is None:
          root = root.left
      # Case 3: Node with two children
      else:
          # Find the inorder successor (smallest in the right subtree)
          successor = find_min(root.right)
          # Replace the current node's data with the successor's data
          root.value = successor.value
          # Delete the successor from the right subtree
          root.right = delete_node_bst(root.right, successor.value)

  return root


