def matrix_mul(m_a, m_b):
    # Validate that m_a and m_b are lists of lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check for non-empty matrices
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    # Validate that all elements of the matrix are integers or floats
    if not all(all(isinstance(el, (int, float)) for el in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(isinstance(el, (int, float)) for el in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")

    # Check that each row of the matrix has the same size
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Validate that the number of columns in m_a matches the number of rows in m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(len(m_b[0])):
            # Perform the dot product of the row of m_a and column of m_b
            result_row.append(sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b))))
        result.append(result_row)

    return result
