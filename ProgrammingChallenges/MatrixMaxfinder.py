# project EUler number 11


import random

rows = int(input("how many rows: "))
columns = int(input("how many columns: "))

best = (0,0)

matrix = [[random.randint(0,10) for i in range(columns)] for i in range(rows)]
print(matrix)


def getValues(li, index):
    newList = [li[index], li[index+1], li[index+2],li[index+3]]
    mult = newList[0] * newList[1] * newList[2] *newList[3]

    global best
    if mult >= best[1]:
        best= (newList,mult)

def getRowMults():
    for row in matrix:
        for i in range(columns - (4-1)):
            executeSummation= getValues(row,i)
        

def getColumnMults():
    columnOrderedMatrix = [[row[i] for row in matrix] for i in range(columns)]
    for column in columnOrderedMatrix:
        for i in range(rows - (4-1)):
            getValues(column,i)

def getDiagonalMults():

    #make diagonal matrices
    
    print(newDiagonalMatrices)
    for row in newDiagonalMatrices:
        for i in range(len(row)-4):
            getValues(row,i)
         

getDiagonalMults()

print(best)
    





#computedMults = [x[1] for x in computedValues]
#computedNumbers = [x[0] for x in computedValues]


#maxValue = max(computedNumbers)
#print(maxValue)
#print(computedNumbers[computedMults.index(maxValue)])

