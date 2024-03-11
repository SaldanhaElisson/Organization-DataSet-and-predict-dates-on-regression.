import numpy as np

sample = np.linspace(0, 20, 500, True)

dataSetOriginal = np.empty((100,5))

def setDatesInArray():
    for i in range(0,100):
        for j in range(0, 5):
            dataSetOriginal[i,j] = sample[i+j]


setDatesInArray()

np.random.shuffle(dataSetOriginal)

dataSetTrainer = np.empty((80,5))
dataSetTestes = np.empty((20,5))

def organizeDateSetToHoldOut():
    for i in range(0, 80):
        for j in range(0, 5):
            dataSetTrainer[i, j] = dataSetOriginal[i,j]

    for i in range(80, 100):
        for j in range(0, 5):
            dataSetTestes[i - 80, j ] = dataSetOriginal[i,j]



organizeDateSetToHoldOut()

print(100 * "-" )
print("Dados para teste")
print(100 * "-" )


print(dataSetTestes)

print(100 * "-" )
print("Dados para treino")
print(100 * "-" )

print(dataSetTrainer)



print(100 * "-" )
print( "Fim")
print(100 * "-" )