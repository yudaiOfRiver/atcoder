S = input()

class solution():
    def __init__(self) -> None:
        self.res = 0

    def BubbleSort(self, num):
        for i in range(len(num)):
            for j in range(len(num)-1, i, -1):
                if num[j] < num[j-1]:
                    num[j], num[j-1] = num[j-1], num[j]
                    self.res += 1

        return num


dict = {"a": 1, "t":2, "c":3, "o":4, "d":5, "e":6, "r":7}
data = []
for i in range(len(S)):
    data.append(dict[S[i]])
#print(data)

obj = solution()
obj.BubbleSort(data)
print(obj.res)
