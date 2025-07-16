import random

rangeCount = (1,100) 

randomNumbers = [random.randint(rangeCount[0], rangeCount[1]) for _ in range(1000)]

mean = sum(randomNumbers)/len(randomNumbers)
print(mean)

randomNumbers.sort()

medianIndex1 = len(randomNumbers)//2 -1
medianIndex2 = len(randomNumbers)//2 +1
median = (medianIndex2-medianIndex1)/2
print(median)

modes = dict.fromkeys(range(1000), 0)
for i in randomNumbers:
    modes[i] += 1
print(modes)
