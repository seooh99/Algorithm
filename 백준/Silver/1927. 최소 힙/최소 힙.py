import sys
import heapq

input = sys.stdin.readline

N = int(input())
que = []

for _ in range(N):
    n = int(input())
    if n != 0:
        heapq.heappush(que, n)
    elif que:
        # que가 비어있는지 아닌지 확인해야함
        n2 = heapq.heappop(que)
        print(n2)
    else:
        print(0)
