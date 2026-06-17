import heapq

h = []

heapq.heappush(h, 3)
print("debug " , h)

heapq.heappush(h, 1)
print("debug " , h)

heapq.heappush(h, 2)
print("debug " , h)

print([heapq.heappop(h) for _ in range(3)])

