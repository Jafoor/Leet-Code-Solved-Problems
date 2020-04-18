import collections

dq = collections.deque()

# append in the right
dq.append(1)
dq.append(2)
dq.append(3)

print(dq)

#append in the left
dq.appendleft(4)
dq.appendleft(5)

print(dq)

#pop from right

dq.pop()
print(dq)

#pop from feft

dq.popleft()
print(dq)
