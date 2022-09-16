N = int(input())
p = list(map(int, input().split()))


points = [0] * N  # p0 が3時の位置にあるときの配置を index0とする
for i in range(N):
    pi = p[i]
    front = (pi - i) % N  # ちょうど料理piが人iの目の前にあるときの、回した数
    points[front] += 1
    points[(front+1)%N] += 1
    points[(front-1)%N] += 1

print(max(points))


