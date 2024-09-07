import numpy as np

def calculate(list):
    try:
        np_list = np.array(list).reshape(3,3)

        mean = {'mean':[np_list.mean(axis=0),np_list.mean(axis=1),np_list.mean()]}
        variance = {'variance':[np_list.var(axis=0),np_list.var(axis=1),np_list.var()]}
        standard_deviation = {'standard deviation':[np_list.std(axis=0),np_list.std(axis=1),np_list.std()]}
        max = {'max':[np_list.max(axis=0),np_list.max(axis=1),np_list.max()]}
        min = {'min':[np_list.min(axis=0),np_list.min(axis=1),np_list.min()]}
        sum = {'sum':[np_list.sum(axis=0),np_list.sum(axis=1),np_list.sum()]}

        
        # Dictionary with all the results
        calculations = {}
        calculations['mean'] = [np.mean(np_list,axis=0),np.mean(np_list,axis=1),np.mean(np_list.flatten())]
        calculations['variance']=[np.var(np_list,axis=0),np.var(np_list,axis=1),np.var(np_list.flatten())]
        calculations['standard deviation']=[np.std(np_list,axis=0),np.std(np_list,axis=1),np.std(np_list.flatten())]
        calculations['max']=[np.max(np_list,axis=0),np.max(np_list,axis=1),np.max(np_list.flatten())]
        calculations['min']=[np.min(np_list,axis=0),np.min(np_list,axis=1),np.min(np_list.flatten())]
        calculations['sum']=[np.sum(np_list,axis=0),np.sum(np_list,axis=1),np.sum(np_list.flatten())]

        return calculations
    except:
        raise ValueError("List must contain nine numbers.")
        