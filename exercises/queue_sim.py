from collections import deque

"""Demonstrating queues.

   first-in, first-out sim , we can also use built in pop and append 
   but they are slow beacuse we need to shift other elements 1 place to right everytime we pop!
"""

queue = deque(["Eric", "Dominic", "Jesse"])
queue.append("Johnson")  # ['Eric', 'Dominic', 'Jesse', 'Johnson']
queue.popleft()  # Removes the first element (left=index(0))


print(list(queue))  # ['Dominic', 'Jesse', 'Johnson']
