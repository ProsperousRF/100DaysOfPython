from fractions import Fraction


# Replace trials by probabilities of occurrences
def replace_probability(m):
    for row in range(len(m)):
        total = 0
        for item in range(len(m[row])):
            total += m[row][item]
        if total != 0:
            for item in range(len(m[row])):
                m[row][item] /= float(total)
    return m


# R - non-terminal -> terminal
# Q - non-terminal -> non-terminal
def rq(m, terminal_state, non_terminal_state):
    r = []
    q = []
    for i in non_terminal_state:
        temp_t = []
        temp_n = []
        for j in terminal_state:
            temp_t.append(m[i][j])
        for j in non_terminal_state:
            temp_n.append(m[i][j])
        r.append(temp_t)
        q.append(temp_n)
    return r, q


# Get Identity Matrix - Q
def subtract_q_from_identity(q):
    """
    If Q = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ]
    I - Q:
    [[1,0,0]            [[0,-2,-3]
     [0,1,0]   - Q =     [-4,-4,-6]
     [0,0,1]]            [-7,-8,-8]]
    """

    for row in range(len(q)):
        for item in range(len(q[row])):
            if row == item:
                q[row][item] = 1 - q[row][item]
            else:
                q[row][item] = -q[row][item]
    return q


# Get minor matrix
def get_minor_matrix(q, i, j):
    """
    Q = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ]
    Minor matrix corresponding to 0,0 is
    [
        [5,6],
        [8,9],
    ]
    """

    minor_matrix = []
    for row in q[:i] + q[i + 1:]:
        temp = []
        for item in row[:j] + row[j + 1:]:
            temp.append(item)
        minor_matrix.append(temp)
    return minor_matrix


# Get determinant of a square matrix
def get_determinant(q):
    if len(q) == 1:
        return q[0][0]
    if len(q) == 2:
        return q[0][0] * q[1][1] - q[0][1] * q[1][0]

    determinant = 0
    for first_row_item in range(len(q[0])):
        minor_matrix = get_minor_matrix(q, 0, first_row_item)
        determinant += (((-1) ** first_row_item) * q[0][first_row_item] * get_determinant(minor_matrix))

    return determinant


# Get transpose of a square matrix
def get_transpose_square_matrix(q):
    for i in range(len(q)):
        for j in range(i, len(q), 1):
            q[i][j], q[j][i] = q[j][i], q[i][j]
    return q


def get_inverse(q):
    q1 = []
    for row in range(len(q)):
        temp = []
        for column in range(len(q[row])):
            minor_matrix = get_minor_matrix(q, row, column)
            determinant = get_determinant(minor_matrix)
            temp.append(((-1) ** (row + column)) * determinant)
        q1.append(temp)
    main_determinant = get_determinant(q)
    q1 = get_transpose_square_matrix(q1)
    for i in range(len(q)):
        for j in range(len(q[i])):
            q1[i][j] /= float(main_determinant)
    return q1


def multiply_matrix(a, b):
    result = []
    dimension = len(a)
    for row in range(len(a)):
        temp = []
        for column in range(len(b[0])):
            product = 0
            for selector in range(dimension):
                product += (a[row][selector] * b[selector][column])
            temp.append(product)
        result.append(temp)
    return result


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def sanitize(m):
    needed = m[0]
    to_fraction = [Fraction(i).limit_denominator() for i in needed]
    lcm = 1
    for i in to_fraction:
        if i.denominator != 1:
            lcm = i.denominator
    for i in to_fraction:
        if i.denominator != 1:
            lcm = lcm * i.denominator / gcd(lcm, i.denominator)
    to_fraction = [(i * lcm).numerator for i in to_fraction]
    to_fraction.append(lcm)
    return to_fraction


def solution(m):
    n = len(m)
    if n == 1:
        if len(m[0]) == 1 and m[0][0] == 0:
            return [1, 1]
    terminal_state = []
    non_terminal_state = []

    # Get terminal and non-terminal states
    for row in range(len(m)):
        count = 0
        for item in range(len(m[row])):
            if m[row][item] == 0:
                count += 1
        if count == n:
            terminal_state.append(row)
        else:
            non_terminal_state.append(row)
    # Replace trials by probabilities
    probabilities = replace_probability(m)
    # Get r and q matrix
    r, q = rq(probabilities, terminal_state, non_terminal_state)
    iq = subtract_q_from_identity(q)
    # Get Fundamental Matrix (F)
    iq1 = get_inverse(iq)
    product_iq1_r = multiply_matrix(iq1, r)
    return sanitize(product_iq1_r)
