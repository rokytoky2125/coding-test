def func (nums):
    s = 0
    for i in nums:
        s = s + (i**2)
    r = s % 10
    return r

nums = list(map(int, input().split()))
r = func(nums)
print(r)
