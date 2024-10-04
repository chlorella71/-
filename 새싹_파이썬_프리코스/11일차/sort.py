nums = [[1,2],[2,1],[2,0],[4,2]]

# nums.sort()
nums.sort(key= lambda x: x[1])
print(nums)