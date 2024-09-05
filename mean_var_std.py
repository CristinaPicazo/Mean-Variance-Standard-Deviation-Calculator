import numpy as np

def calculate(list):
    try:
        np_list = np.array(list).reshape(3,3)

        mean = {'mean':[np_list.mean(axis=0),np_list.mean(axis=1),np_list.mean()]}
        variance = {'mean':[np_list.var(axis=0),np_list.var(axis=1),np_list.var()]}
        standard_deviation = {'standard deviation':[np_list.std(axis=0),np_list.std(axis=1),np_list.std()]}
        max = {'max':[np_list.max(axis=0),np_list.max(axis=1),np_list.max()]}
        min = {'min':[np_list.min(axis=0),np_list.min(axis=1),np_list.min()]}
        sum = {'sum':[np_list.sum(axis=0),np_list.sum(axis=1),np_list.sum()]}

        
        # Dictionary with all the results
        calculations = {mean,variance,standard_deviation,max,min,sum}

        return calculations
    except:
        raise ValueError("List must contain nine numbers.")
        