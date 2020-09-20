def print_matrix(high, arr):
    for index_print in range(high):
        print(arr[index_print])
    print()
    return


def ref_matrix(high, len, arr):
    for index_x in range(high):
        for index_y in range(len):
            if arr[index_x][index_y] == ".":
                arr[index_x][index_y] = int(0)
            elif arr[index_x][index_y] == "#":
                arr[index_x][index_y] = int(-1)
            else:
                stupid_warning()
    return


def stupid_warning():
    print("ERROR")
    print("Ah shit, here we go again!")
    print("Are U dumb, stupid or dumb, huh! ©6IX9INE")
    exit(1)
    return


def dfs(arr, a, b, high, len):
    global ans
    if a == high - 1 and b == len - 1:
        ans += 1
    else:
        if a + 1 < high and arr[a + 1][b] == 0:
            dfs(arr, a + 1, b, high, len)
        if b + 1 < len and arr[a][b + 1] == 0:
            dfs(arr, a, b + 1, high, len)
    return


def check_way(ix, iy, arr):
    if arr[ix - 1][iy - 1] > 0:
        print("Easy-peasy, lemon squeezy!")
        print("Shortest way takes: ", arr[ix - 1][iy - 1])
        print()
    else:
        print("ERROR")
        print("Ah shit, here we go again!")
        print("No way!!! Dude... No way!!!")
        exit(1)
    return


with open("task.txt", "r") as f:
    x, y = next(f).split()
    x = int(x)
    y = int(y)
    print(x, y)
    print()
    matrix = []
    for i in range(x):
        matrix.append([-9] * y)
    for index, line in enumerate(f):
        if y != len(line.rstrip('\r\n')):
            print("Incorrect matrix")
            stupid_warning()
        matrix[index] = list(line.rstrip('\r\n'))
    print_matrix(x, matrix)
    ref_matrix(x, y, matrix)
    print_matrix(x, matrix)
    ans = 0
    dfs(matrix, 0, 0, x, y)
    print(ans)
