from bisect import bisect_left, bisect_right

_list = [1,2,3,4,5]

print(bisect_left(_list,1))
print(bisect_right(_list,3))