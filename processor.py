def create_matrix(size_message, matrix_message):
    rows, cols = (int(x) for x in input(size_message).split())
    print(matrix_message)
    m = [[float(x) for x in input().split()] for _ in range(rows)]
    return m, rows, cols


def add_matrices(m1, m2):
    return [[sum(elem) for elem in zip(m1[row], m2[row])] for row in range(len(m1))]
    # OR
    # return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
    # OR
    # return list(list(map(sum, zip(M1[row], M2[row]))) for row in range(len(m1))


def multiply_matrix_by_const(m, c):
    return [[elem * c for elem in row] for row in m]
    # OR
    # return list(list(map(lambda x: x * c, M[row])) for row in m)


def multiply_matrices(m1, m2):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*m2)] for row in m1]
    # OR
    # return [[sum(M1[row][i] * M2[i][col] for i in range(cols1)) for col in range(cols2)]
    #          for row in range(rows1)]


def transpose_matrix(m, mode="main diagonal"):
    if mode == 'main diagonal':
        return list(map(list, zip(*m)))
    elif mode == 'side diagonal':
        return reversed([*zip(*reversed(m))])
        # OR
        # return [*zip(*m[::-1])][::-1]
    elif mode == 'vertical line':
        return [row[::-1] for row in m]
        # OR
        # return [[elem for elem in row[::-1]] for row in m]
    elif mode == 'horizontal line':
        return m[::-1]
        # OR
        # return [row for row in m[::-1]]


def calc_det(m, det=0):
    if len(m) == 1 and len(m[0]) == 1:
        return m[0][0]
    elif len(m) == 2 and len(m[0]) == 2:
        return m[0][0] * m[1][1] - m[1][0] * m[0][1]
    else:
        for c in range(len(m)):
            det += ((-1) ** c) * m[0][c] * calc_det(find_minor(m, 0, c))
        return det


def find_minor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def inverse_matrix(m, rows, cols):
    det = calc_det(m)
    if det == 0 or rows != cols:
        print("This matrix doesn't have an inverse.\n")
    else:
        if len(m) == 2:
            return [[m[1][1] / det, -1 * m[0][1] / det],
                    [-1 * m[1][0] / det, m[0][0] / det]]
        cofactors = []
        for row in range(len(m)):
            cofactor_row = []
            for col in range(len(m)):
                minor = find_minor(m, row, col)
                cofactor_row.append(((-1) ** (row + col)) * calc_det(minor))
            cofactors.append(cofactor_row)
        cofactors = transpose_matrix(cofactors)
        for row in range(len(cofactors)):
            for col in range(len(cofactors)):
                cofactors[row][col] = cofactors[row][col] / det
        return cofactors


def result_matrix(m):
    print("The result is:")
    for row in m:
        print(*row)
    print()


def menu():
    print("1. Add matrices",
          "2. Multiply matrix by a constant",
          "3. Multiply matrices",
          "4. Transpose matrix",
          "5. Calculate a determinant",
          "6. Inverse matrix",
          "0. Exit",
          sep='\n')
    choice = int(input("Your choice: "))
    if choice in (1, 3):
        m1, rows1, cols1 = create_matrix(
            "Enter size of first matrix: ", "Enter first matrix:"
        )
        m2, rows2, cols2 = create_matrix(
            "Enter size of second matrix: ", "Enter second matrix:"
        )
        if choice == 1 and rows1 == rows2 and cols1 == cols2:
            result = add_matrices(m1, m2)
        elif choice == 3 and cols1 == rows2:
            result = multiply_matrices(m1, m2)
        result_matrix(result)
    elif choice in (2, 5, 6):
        m1, rows1, cols1 = create_matrix("Enter matrix size: ", "Enter matrix:")
        if choice == 2:
            const = float(input("Enter constant: "))
            result = multiply_matrix_by_const(m1, const)
            result_matrix(result)
        elif choice == 5 and rows1 == cols1:
            print("The result is:")
            print(calc_det(m1))
            print()
        elif choice == 6:
            result = inverse_matrix(m1, rows1, cols1)
            result_matrix(result)
    elif choice == 4:
        print("1. Main diagonal",
              "2. Side diagonal",
              "3. Vertical line",
              "4. Horizontal line",
              sep='\n')
        mode = int(input("Your choice: "))
        m, _, _ = create_matrix("Enter matrix size: ", "Enter matrix:")
        if mode == 1:
            result = transpose_matrix(m, mode="main diagonal")
        elif mode == 2:
            result = transpose_matrix(m, mode="side diagonal")
        elif mode == 3:
            result = transpose_matrix(m, mode="vertical line")
        elif mode == 4:
            result = transpose_matrix(m, mode="horizontal line")
        result_matrix(result)
    elif choice == 0:
        exit()
    else:
        print("The operation cannot be performed.\n")


def main():
    while True:
        menu()


if __name__ == "__main__":
    main()
