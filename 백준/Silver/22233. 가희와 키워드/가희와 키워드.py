import sys 
N, M = map(int, input().split())
memo = set()
for n in range(N):
    # 줄바꿈이 있기 때문에 strip으로 제거해줘야 한다.
    memo.add(sys.stdin.readline().strip())
cnt = 0
for m in range(M):
    # discard() 함수는 인자로 list를 받지 않으므로 tuple 사용
    data = set(sys.stdin.readline().rstrip().split(','))   
    # discard() 메소드는 엘리먼트가 없어도 정상종료한다. remove()는 실제 존재하는 대상을 지우는 동작에, discard()는 존재하지 않음을 보장하려고 할때 사용
    # memo.discard(data)
    for i in data:
        if i in memo:
          memo.discard(i)
          cnt += 1
    print(N - cnt)