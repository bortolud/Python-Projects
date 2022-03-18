from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]
  
  #internal
  #used to create and compress the hash used to index the array
  def hash(self, key):
    return sum(key.encode())
  def compress(self, hash_code):
    return hash_code%self.array_size

  #external
  #assign and retrieve key and value pairs from the hash map
  def assign(self, key, value):
    hashed_key = self.hash(key)
    array_index = self.compress(hashed_key)

    payload = Node([key,value])
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if key == item[0]:
        item[1] = value
    list_at_array.insert(payload)

  def retrieve(self, key):
    hashed_key = self.hash(key)
    array_index = self.compress(hashed_key)

    list_at_index = self.array[array_index]
    for item in list_at_index:
      if key == item[0]:
        return item[1]
    else:
      return None

#Tests
blossom = HashMap(len(flower_definitions))
for item in flower_definitions:
  blossom.assign(item[0], item[1])
print(blossom.retrieve('poppy'))