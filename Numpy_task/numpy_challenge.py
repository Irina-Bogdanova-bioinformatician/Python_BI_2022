import numpy as np


def multiplication_check(matrices_list):
    """ Input: a list of 2-dimensional matrices.
        Return: True if they can be multiplied by each other in the order in which they are in the list,
        and False if they cannot be multiplied.
    """
    result = True
    multiplication_result_shape = matrices_list[0].shape
    for i in range(1, len(matrices_list)):
        if multiplication_result_shape[1] != matrices_list[i].shape[0]:
            result = False
            break
        else:
            multiplication_result_shape = (multiplication_result_shape[0], matrices_list[i].shape[1])
    return result


def matrix_multiplication(m_1, m_2):
    # Carry out multiplication of two matrices. Return: result matrix.
    result = np.matmul(m_1, m_2)
    return result


def multiply_matrices(matrices_list):
    """ Input: a list of matrices.
        Return: result of multiplication in the order in which matrices are in the list,
        and None if they cannot be multiplied.
    """

    multiplication_result = matrices_list[0]
    try:
        for i in range(1, len(matrices_list)):
            multiplication_result = np.matmul(multiplication_result, matrices_list[i])
    except ValueError:
        multiplication_result = None
    return multiplication_result


def compute_2d_distance(arr_1, arr_2):
    """ Input: 2 one-dimensional arrays with a pair of values (as coordinates of a point on a plane).
        Return: the distance between them.
    """
    result = np.sqrt(np.sum((arr_1 - arr_2) ** 2))
    return result


def compute_multidimensional_distance(arr_1, arr_2):
    """ Input: 2 one-dimensional arrays with values (as coordinates of a point in n-dimensional space).
        Return: the distance between them.
    """
    result = compute_2d_distance(arr_1, arr_2)
    return result


def compute_pair_distances(arr):
    """ Input: 2d array, where each row is an observation, and each column is a feature.
        Return: a matrix of pairwise distances.
    """

    def calculate_distances(rows_indices, array=arr):
        new_result = compute_multidimensional_distance(array[rows_indices[0]], array[rows_indices[1]])
        return new_result

    indices_matrix = np.fromfunction(lambda i, j: [i, j], (arr.shape[0], arr.shape[0]), dtype=int)
    result = np.apply_along_axis(calculate_distances, 0, indices_matrix)
    return result


if __name__ == "__main__":
    # task: create 3 numpy arrays with different ways
    first_array = np.eye(3, dtype=int)
    second_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    third_array = np.fromfunction(lambda i, j: i + j, (4, 4), dtype=int)
    print(f"Three arrays:\n{first_array}\n{second_array}\n{third_array}")
