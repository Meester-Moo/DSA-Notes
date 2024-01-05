queue = []

#All of the items get added
#with the leftmost being the
#front of the queue

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)

print(queue)

#remove the first in line
queue.pop(0)

print(queue)
print("The frontmost (leftmost) element is now gone")

queue.pop(0)
queue.pop(0)
print(queue)
print("Above, we just popped the next two in the queue")
print("Now we will add some more items back to the queue")

queue.append(1)
queue.append(2)

print(queue)

print("and now you can see that the back of the queue is at the right side")


