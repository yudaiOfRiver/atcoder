S1 = input()
S2 = input()
S3 = input()

all = set()
all.add("ABC")
all.add("ARC")
all.add("AGC")
all.add("AHC")

all.remove(S1)
all.remove(S2)
all.remove(S3)

print(all.pop())
