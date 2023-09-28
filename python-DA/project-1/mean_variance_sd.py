import numpy as np

def calculate(list):
    

    try:

        np_array=np.reshape(list,(3,3))
        mean_axis0=np.all(np_array, axis=0).mean()
        mean_axis1=np.mean(np_array, axis=1).mean()
        mean_flattened=np.all(np_array).mean()
        
        # calculate variance
        var_axis0=np.var(np_array, axis=0).mean()
        var_axis1=np.var(np_array, axis=1).mean()
        var_flattened=np.var(np_array)

        #calculate standard deviation

        std_axis0=np.std(np_array, axis=0).mean()
        std_axis1=np.std(np_array, axis=1).mean()
        std_flattened=np.std(np_array)

        # calculate max
        max_axis0=np.max(np_array, axis=0).mean()
        max_axis1=np.max(np_array, axis=1).mean()
        max_flattened=np.max(np_array)
        #min
        min_axis0=np.min(np_array, axis=0).mean()
        min_axis1=np.min(np_array, axis=1).mean()
        min_flattened=np.min(np_array)

        #sum

        sum_axis0=np.any(np_array, axis=0).sum()
        sum_axis1=np.any(np_array, axis=1).sum()
        sum_flattened=np.sum(np_array)



        calculations={'mean': [mean_axis0,mean_axis1, mean_flattened],
        'variance': [var_axis0,var_axis1, var_flattened],
        'standard deviation': [std_axis0,std_axis1, std_flattened],
        'max': [max_axis0,max_axis1, max_flattened],
        'min': [min_axis0,min_axis1, min_flattened],
        'sum': [sum_axis0,sum_axis1, sum_flattened]}
    
    except ValueError:


        raise ValueError("List must contain nine numbers.")



    return calculations

calculate([2,6,2,8,4,0,1,5,7])