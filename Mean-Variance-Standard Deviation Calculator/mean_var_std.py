import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    calculations = dict()
    matrix = np.array(list).reshape(3,3)

    col_mean = np.mean(matrix, axis=0).tolist()
    row_mean = np.mean(matrix, axis=1).tolist()
    flat_mean = np.mean(list)

    col_var = np.var(matrix, axis=0).tolist() 
    row_var = np.var(matrix, axis=1).tolist()
    flat_var = np.var(list)

    col_sd = np.std(matrix, axis=0).tolist()
    row_sd = np.std(matrix, axis=1).tolist()
    flat_sd = np.std(list)

    col_max = np.max(matrix, axis=0).tolist()
    row_max = np.max(matrix, axis=1).tolist() 
    flat_max = np.max(list)  

    col_min = np.min(matrix, axis=0).tolist()  
    row_min = np.min(matrix, axis=1).tolist() 
    flat_min = np.min(list)  

    col_sum = np.sum(matrix, axis=0).tolist()  
    row_sum = np.sum(matrix, axis=1).tolist()  
    flat_sum = np.sum(list)

    calculations['mean'] = [col_mean, row_mean, flat_mean]
    calculations['variance'] = [col_var, row_var, flat_var]
    calculations['standard deviation'] = [col_sd, row_sd, flat_sd]
    calculations['max'] = [col_max, row_max, flat_max]
    calculations['min'] = [col_min, row_min, flat_min]
    calculations['sum'] = [col_sum, row_sum, flat_sum]


    return calculations
