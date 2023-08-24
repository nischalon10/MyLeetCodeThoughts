nums = [2,3,0,0]
prod = nums[0]
num0 = 0
for x in nums[1:]:
    if x != 0:
        prod *= x
    else:
        num0 += 1
res = []
for x in nums:
    if (x == 0 and num0==1):
        res.append(prod)
    elif (num0 >= 1):
        res.append(int(0))
    else:
        res.append(int(prod/x))
print(res)