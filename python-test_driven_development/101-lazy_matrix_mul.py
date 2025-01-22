import numpy as np

def lazy_matrix_mul(m_a, m_b):
    # Validate the inputs: m_a and m_b should be lists of lists
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check dimensions for matrix multiplication compatibility
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication using numpy
    return np.matmul(m_a, m_b)
