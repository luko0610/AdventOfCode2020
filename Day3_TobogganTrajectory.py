def arrayProd(array):
    prod = array[0]
    for idx in range(1, len(array)):
        prod *= array[idx]
    return prod
        

with open('./input_Day3.txt') as f:
    input = f.readlines()

input = [row.rstrip('\n') for row in input]

stepDict = [{"right": 1, "down": 1},
            {"right": 3, "down": 1},
            {"right": 5, "down": 1},
            {"right": 7, "down": 1},
            {"right": 1, "down": 2}]

treeCounts = []


for step in stepDict:
    trees = 0
    colIdx = step["down"]
    rowIdx = step["right"]
    atEnd = False
    
    while(not atEnd):
        # found tree
        if(input[colIdx][rowIdx] == '#'):
            trees += 1
            
        colIdx += step["down"]
        rowIdx += step["right"]

        # out if row index -> continue at row 0
        if(len(input[0]) <= rowIdx and len(input) > colIdx):
            rowIdx = rowIdx - len(input[0])
            
        atEnd = len(input) <= colIdx or len(input[0]) <= rowIdx

    treeCounts.append(trees)

print(str(treeCounts) + ' trees found')
print('multiplied result ' + str(arrayProd(treeCounts)))



            
