import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    if arr.ndim == 1:
        if norm_type == 'l1':
            return float(sum([abs(i) for i in arr]))
        elif norm_type == 'l2':
            return float((sum([i**2 for i in arr]))**(1/2))
        elif norm_type == 'linf':
            return float(max([abs(i) for i in arr]))
    elif arr.ndim == 2:
        if norm_type == 'l1':
            return float(sum([abs(i) for j in arr for i in j]))
        elif norm_type == 'l2' or norm_type == 'frobenius':
            return float((sum([i**2 for j in arr for i in j]))**(1/2))
        elif norm_type == 'linf' :
            return float(max([abs(i) for j in arr for i in j]))
    raise ValueError()   

