import numpy as np

def calculate(list):
    if(len(list) != 9):
        raise ValueError("List must contain nine numbers.")
    
    # Convert list in numpy array
    np_list = np.array(list)
    
    mean_columns = ([np_list[[0,3,6]].mean(), np_list[[1,4,7]].mean(), np_list[[2,5,8]].mean()])
    mean_rows = [np_list[[0,1,2]].mean(), np_list[[3,4,5]].mean(), np_list[[6,7,8]].mean()]

    variance_columns = ([np_list[[0,3,6]].var(), np_list[[1,4,7]].var(), np_list[[2,5,8]].var()])
    variance_rows = [np_list[[0,1,2]].var(), np_list[[3,4,5]].var(), np_list[[6,7,8]].var()]

    std_columns = ([np_list[[0,3,6]].std(), np_list[[1,4,7]].std(), np_list[[2,5,8]].std()])
    std_rows = ([np_list[[0,1,2]].std(), np_list[[3,4,5]].std(), np_list[[6,7,8]].std()])

    max_columns = ([np_list[[0,3,6]].max(), np_list[[1,4,7]].max(), np_list[[2,5,8]].max()])
    max_rows = ([np_list[[0,1,2]].max(), np_list[[3,4,5]].max(), np_list[[6,7,8]].max()])

    min_columns = ([np_list[[0,3,6]].min(), np_list[[1,4,7]].min(), np_list[[2,5,8]].min()])
    min_rows = ([np_list[[0,1,2]].min(), np_list[[3,4,5]].min(), np_list[[6,7,8]].min()])

    sum_columns = ([np_list[[0,3,6]].sum(), np_list[[1,4,7]].sum(), np_list[[2,5,8]].sum()])
    sum_rows = ([np_list[[0,1,2]].sum(), np_list[[3,4,5]].sum(), np_list[[6,7,8]].sum()])


    calculations= {
        'mean' : [mean_columns,mean_rows,np_list.mean()],
        'variance' : [variance_columns,variance_rows,np_list.var()],
        'standard deviation' : [std_columns,std_rows,np_list.std()],
        'max' : [max_columns,max_rows,np_list.max()],
        'min' : [min_columns,min_rows,np_list.min()],
        'sum' : [sum_columns,sum_rows,np_list.sum()]
    }

    return calculations
        
        