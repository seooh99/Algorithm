import heapq
import sys

INF = 10 * 125 * 125 # 무한대 값 설정
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0] # 상하좌우 이동을 위한 dx, dy 설정

def dijkstra(x, y):
    heap = [] # heap 초기화
    distance[x][y] = graph[x][y] # 시작 노드의 거리를 초기화
    heapq.heappush(heap, [distance[x][y], x, y]) # heap에 시작 노드 정보 추가

    while heap:
        # heap에서 최소 거리를 가진 노드 정보 pop
        dist, cur_x, cur_y = heapq.heappop(heap)

        # 이미 방문한 노드이면 continue
        if visited[cur_x][cur_y]:
            continue

        # 방문하지 않은 노드이면 방문 처리
        visited[cur_x][cur_y] = True

        # 인접한 노드 순회
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]

            # 경계 체크
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            # 방문하지 않은 노드이면 최소 거리 업데이트 후 heap에 추가
            if not visited[nx][ny] and distance[nx][ny] > dist + graph[nx][ny]:
                distance[nx][ny] = dist + graph[nx][ny]
                heapq.heappush(heap, [distance[nx][ny], nx, ny])

    return distance[n - 1][n - 1] # 마지막 노드까지의 최소 거리 반환

# 입력
t = 0
while True:
    n = int(input())
    if n == 0:
        break

    t += 1
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    # 시작 노드부터 마지막 노드까지의 최소 거리를 저장할 2차원 리스트 초기화
    distance = [[INF] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)] # 방문 여부를 저장할 2차원 리스트 초기화

    print("Problem {}: {}".format(t, dijkstra(0, 0))) # 시작 노드 (0, 0)으로부터 마지막 노드까지의 최소 거리 출력
