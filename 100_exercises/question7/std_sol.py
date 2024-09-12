input_str = input()
dimensionList = [int(x) for x in input_str.split(',')]
rowNum = dimensionList[0]
colNum = dimensionList[1]
arr = [[0 for col in range(colNum)] for row in range(rowNum)]
for i in range(rowNum):
    for j in range(colNum):
        arr[i][j] = i * j
print(arr)