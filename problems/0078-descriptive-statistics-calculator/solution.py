import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    mean = np.mean(data)
    median = np.median(data)
    count = dict()
    for i in data:
        if i in count:
            count[i] += 1
        else:
            count[i] = 0
    mode = max(data, key = count.get)
    variance = sum((i-mean)**2 for i in data)/len(data)
    deviation = variance**(1/2)
    per25 = np.percentile(data, 25)
    per50 = np.percentile(data, 50)
    per75 = np.percentile(data, 75)
    iqr = per75 - per25
    return {'mean': mean, 'median': median, 'mode': mode, 'variance': variance, 'standard_deviation': deviation, '25th_percentile': per25, '50th_percentile': per50, '75th_percentile': per75, 'interquartile_range': iqr}