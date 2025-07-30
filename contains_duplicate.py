nums = [1,2,3,1]
n = len(nums)
nums.sort()
for i in range(n-1):
    if nums[i]==nums[i+1]:
        print(True)
        break
    print(False)