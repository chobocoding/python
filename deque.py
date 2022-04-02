# https://www.acmicpc.net/problem/10845

from collections import deque
queue = deque()

N = int(input())

for i in range(N):
    print(queue)
    command = input()
    if command == "pop":
        if len(queue) == 0: print(-1)
        else: print(queue.popleft())
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        if len(queue) == 0: print(1)
        else: print(0)
    elif command == "front":
        if len(queue) == 0: print(-1)
        else: print(queue[0])

    elif command == "back":
        if len(queue) == 0: print(-1)
        else: print(queue[-1])

    else:
        queue.append(command[5:])

        
'''
deque() : 초기화 함수
append(x) : 덱의 오른쪽에 x추가
appendleft(x) : 덱의 왼쪽에 x추가
pop(x) : 맨 뒤 제거 후 반한
popleft(x) : 맨 앞 제거 후 반환
clear() : 모든 원소 삭제
len() : 길이 반환
'''
