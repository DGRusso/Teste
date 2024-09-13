import numpy as np

def calculate(nums):
    if len(nums) != 9:
        raise ValueError('List must contain nine numbers.')
    array = np.array(nums)
    matrix = array.reshape((3, 3))
    print(matrix)
    meanT = np.mean(matrix).tolist()
    meanrow = np.mean(matrix, axis=1).tolist()
    meancolumn = np.mean(matrix, axis=0).tolist()
    varT = np.var(matrix).tolist()
    varcolumn = np.var(matrix, axis=0).tolist()
    varrow = np.var(matrix, axis=1).tolist()
    stdT = np.std(matrix).tolist()
    stdcolumn = np.std(matrix, axis=0).tolist()
    stdrow = np.std(matrix, axis=1).tolist()
    maxT = np.max(matrix).tolist()
    maxcolumn = np.max(matrix, axis=0).tolist()
    maxrow = np.max(matrix, axis=1).tolist()
    minT = np.min(matrix).tolist()
    mincolumn = np.min(matrix, axis=0).tolist()
    minrow = np.min(matrix, axis=1).tolist()
    sumT = np.sum(matrix).tolist()
    sumcolumn = np.sum(matrix, axis=0).tolist()
    sumrow = np.sum(matrix, axis=1).tolist()
    calculations =  {"mean": [meancolumn, meanrow, meanT], 
                    "variance": [varcolumn, varrow, varT],
                    "standard deviation": [stdcolumn, stdrow, stdT],
                    "max": [maxcolumn, maxrow, maxT],
                    "min": [mincolumn, minrow, minT],
                    "sum": [sumcolumn, sumrow, sumT]}
    return calculations
