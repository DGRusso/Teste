import numpy as np

def calculate(nums):
    try:
        array = np.array(nums)
        matrixnp = array.reshape((3, 3))
        matrix = matrixnp.tolist()
    except ValueError:
        print("List must contain nine numbers.")
    else:
        print(matrix)
        meanT = np.mean(matrix)
        meanrow = np.mean(matrix, axis=1)
        meancolumn = np.mean(matrix, axis=0)
        varT = np.var(matrix)
        varcolumn = np.var(matrix, axis=0)
        varrow = np.var(matrix, axis=1)
        stdT = np.std(matrix)
        stdcolumn = np.std(matrix, axis=0)
        stdrow = np.std(matrix, axis=1)
        maxT = np.max(matrix)
        maxcolumn = np.max(matrix, axis=0)
        maxrow = np.max(matrix, axis=1)
        minT = np.min(matrix)
        mincolumn = np.min(matrix, axis=0)
        minrow = np.min(matrix, axis=1)
        sumT = np.sum(matrix)
        sumcolumn = np.sum(matrix, axis=0)
        sumrow = np.sum(matrix, axis=1)
        print(f'''"mean": [{meancolumn}, {meanrow}, {meanT}] 
"variance": [{varcolumn}, {varrow}], {varT}]
"standard deviation": [{stdcolumn}, {stdrow}, {stdT}]
"max": [{maxcolumn}, {maxrow}, {maxT}]
"min": [{mincolumn}, {minrow}, {minT}]
"sum": [{sumcolumn}, {sumrow}, {sumT}]''')


calculate([0,1,2,3,4,5,6,7,8])