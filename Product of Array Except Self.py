def products(nums):
  # Fill this in.
    
    n = len(nums)
    if n == 1 :
        return 0
    
    l = [0]*n
    r = [0]*n
    prod =[0]*n
    l[0] = 1
    r[n-1] = 1
    for i in range(1 , n):
        l[i] = nums[i-1] * l[i-1]
    for j in range(n-2 , -1 , -1):
        r[j] = nums[j+1] * r[j+1]
    for i in range(n):
        prod[i] = r[i] * l[i]
    return prod
print (products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]
