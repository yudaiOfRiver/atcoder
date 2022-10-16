def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r) // 2
        if target == nums[m]:
            return m
        elif target < nums[m]:
            r = m-1
        elif nums[m] < target:
            l = m+1
    return l



H, W, rs, cs = map(int, input().split())
rs -= 1
cs -= 1

N = int(input())
walls = [[0] * H for _ in range(W)]
for _ in range(N):
    ri, ci = map(int, input().split())
    ri -= 1
    ci -= 1
    walls[ri][ci] = 1


Q = int(input())
d, l = [], []
for _ in range(Q):
    di, li = input().split()
    #d.append(di)
    #l.append(int(li))
    if d == "L":
        wall = walls[rs]
        li = min(li, )
        index = search()





