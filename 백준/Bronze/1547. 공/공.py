M = int(input())
# 컵 번호가 위치에 따라 어떻게 놓여있는지를 표현
# 예: positions[0] = 1 이면, 첫 번째 위치에 1번 컵이 있다는 뜻
positions = [1, 2, 3]  # 초기 상태: 1번, 2번, 3번 컵이 1~3번 위치에 있음

for _ in range(M):
    x, y = map(int, input().split())
    # 위치는 0-indexed로 바꿔줌
    positions[x-1], positions[y-1] = positions[y-1], positions[x-1]

# 공은 처음에 1번 컵에 있었으므로, 그 컵이 어디 위치에 있는지 찾아야 함
for i in range(3):
    if positions[i] == 1:
        print(i + 1)  # 위치는 1번부터 시작
        break
