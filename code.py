m = int(input("Input number of rows: "))
n = int(input("Input number of columns: "))
l = [[0 for col in range(m)] for row in range(n)]
for row in range(n):
    for col in range(m):
      l[row][col]= row*col
print(l)
