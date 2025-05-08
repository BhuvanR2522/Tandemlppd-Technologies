nums = list(map(int,input().split()))

counts = {}

for i in range(1 , 10):
    counts[i] = 0
    for n in nums:
        if n % i == 0:
            counts[i] += 1
print("Result :", counts) 