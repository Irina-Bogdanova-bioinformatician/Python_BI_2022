# numpy_challenge.py

The module that includes following functions:

**multiplication_check(matrices_list)**
  Input: a list of 2-dimensional matrices.
  Return: True if they can be multiplied by each other in the order in which they are in the list, and False if they cannot be multiplied.

**matrix_multiplication(m_1, m_2)**
  Carry out multiplication of two matrices.
  Return: result matrix.

**multiply_matrices(matrices_list)**
  Input: a list of matrices.
  Return: result of multiplication in the order in which matrices are in the list, and None if they cannot be multiplied.

**compute_2d_distance(arr_1, arr_2)**
  Input: 2 one-dimensional arrays with a pair of values (as coordinates of a point on a plane).
  Return: the distance between them.

**compute_multidimensional_distance(arr_1, arr_2)**
  Input: 2 one-dimensional arrays with values (as coordinates of a point in n-dimensional space).
  Return: the distance between them.

**compute_pair_distances(arr)**
  Input: 2d array, where each row is an observation, and each column is a feature.
  Return: a matrix of pairwise distances.

### Requirements:
python>=3.6

### Create and activate virtual environment
Run:
~~~sh
python3 -m venv new_venv_name
source new_venv_name/bin/activate
~~~

### Install requirements from requirements.txt
Run:
~~~sh
pip install -r requirements.txt
~~~

### Run numpy_challenge.py

The output of running numpy_challenge.py (result of running 'if __name__ == "__main__":' module) are three arrays, that are created with 3 different ways using numpy lib.

Run:
~~~sh
python3 numpy_challenge.py
~~~
