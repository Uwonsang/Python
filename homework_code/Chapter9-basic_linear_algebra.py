def vector_size_check(*vector_variables):
    return len(set([len(vector) for vector in vector_variables])) == 1

def vector_addition(*vector_variables):
    return [ sum(vector) for vector in zip (*vector_variables)]


def vector_subtraction(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    return [ vector[0]*2 - sum(vector) for vector in zip (*vector_variables)]


def scalar_vector_product(alpha, vector_variable):
    return [alpha * vector for vector in vector_variable]


def matrix_size_check(*matrix_variables):
    return len(set([len(vector) for vector in (matrix_variables)])) == 1

def is_matrix_equal(*matrix_variables):
    result = sum([[len(set(index)) for index in zip (*vector)] for vector in zip (*matrix_variables)],[])
    return result.count(1) == len(result)



def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return [[sum(element) for element in zip (*vector)] for vector in zip(*matrix_variables)]


def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return [[element[0]*2 - sum(element) for element in zip (*vector)] for vector in zip(*matrix_variables)]


def matrix_transpose(matrix_variable):
    return [[element for element in vector] for vector in zip (*matrix_variable)]


def scalar_matrix_product(alpha, matrix_variable):
    return [[alpha * element for element in vector] for vector in matrix_variable]


def is_product_availability_matrix(matrix_a, matrix_b):
    return [set([len(vector) for vector in matrix_a])] == [set([len([element for element in vector]) for vector in zip (*matrix_b)])]

def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    return [[sum(a * b for a, b in zip (row_a, column_b)) for column_b in zip(*matrix_b)] for row_a in matrix_a]
