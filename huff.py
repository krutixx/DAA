#1classdef
import heapq

class Node:

  def __init__(self, char, freq):
    self.char = char
    self.freq=freq
    self.left=None
    self.right=None

  def __lt__(self,other):
    return self.freq<other.freq

#2take input
text = input("Enter text")

#calculate freq
freq={}

for char in text:
  freq[char] = freq.get(char, 0) +1

#3create node and put in heap
heap=[]
for char in freq:
  heapq.heappush(heap, Node(char, freq[char]))

#4build tree
while len(heap)>1:
  left=heapq.heappop(heap)
  right=heapq.heappop(heap)

  parent = Node(None, left.freq+right.freq)

  parent.left=left
  parent.right=right

  heapq.heappush(heap, parent)

#5get the codes
def get_codes(root, code=""):

  if root.char is not None:
    codes[root.char] = code
    return

  get_codes(root.left, code+"0")
  get_codes(root.right, code+"1")

#6calculate huffman code
root=heap[0]
codes = {}

get_codes(root)

#7print huffman_codes
for char in codes:
  print(char, ":", codes[char])


#8encoded text
encoded=""

for char in text:
  encoded += codes[char]
print("ENcoded:", encoded)