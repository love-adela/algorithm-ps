class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value


class HashTable():

  def __init__(self, size=7):
    self._table = [[] for _ in range(size)]
    self.size = size

  def set(self, key, value):
    
    new_node = Node(key, value)

    bucket, item, _ = self.find(key)
    
    if item == None:
      bucket.append(new_node)
    else:
      item = new_node
    


  def get(self, key):

    _, item, _ = self.find(key)
    if item == None:
      return None

    return item.value


  def delete(self, key):

    box, item, in_index = self.find(key)
    if item is None:
      return False
    
    del_item = box.pop(in_index)
    return del_item.value


  def find(self, key):
    
    hash_key = hash(key)
    index = hash_key % self.size

    bucket = self._table[index]
    
    cnt = len(bucket)
    for in_index in range(0, cnt):
      item = bucket[in_index]
      if item.key == key:
        return bucket, item, in_index 

    return bucket, None, -1


hash_table = HashTable()

def hash_set(key, value):
  return hash_table.set(key, value)
    

def hash_get(key):
  return hash_table.get(key)


def hash_delete(key):
  return hash_table.delete(key)