import sys

sys.stdin = open("6th\\input","r")

h,w,x,y = list(map(int,sys.stdin.readline().split()))

B_array = [ 0*(w+y) for _ in range(h+x)]



for i in range(h+x):
  B_array[i] = list(map(int,sys.stdin.readline().split()))

# 배열 A 초기화
A_array = [[0]*w for _ in range(h)]

for i in range(h):
  for j in range(w):
    A_array[i][j] = B_array[i][j]
  
for i in range(x,h):
  for j in range(y,w):
    A_array[i][j] = B_array[i][j] - A_array[i-x][j-y]

for i in range(h):
  for j in range(w):
    print(A_array[i][j],end=" ")
  print("")