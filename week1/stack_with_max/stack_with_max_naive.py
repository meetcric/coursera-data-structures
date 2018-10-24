#python3
import sys


items=[0]
for i in range(int(input())):
    nums = list(map(str, input().split()))
    # print (nums)
    if(nums[0]=='push'):
        items.append(max(int(nums[1]),int(items[-1])))
    elif(nums[0]=='pop'):
        items.pop()
    else:
        print(items[-1])
