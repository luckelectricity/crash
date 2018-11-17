# def add(*nums):
#     sum = 0
#     for num in nums:
#         sum += num
#     return sum
import random

b = []

for i in range(11):
    x = random.randint(1,6)
    if x == 6 or x == 1:
        # break
        continue
    else:
        print(x)
