from sys import stdout, exit
from math import sqrt, ceil

def write_output(i, j):
    print("{} {}".format(i, j))
    stdout.flush()

def read_input():
    values = input()
    if values == "-1 -1":
        exit()

    return values

def read_coord():
    i, j = [int(s) for s in read_input().split()]
    return i, j

def need_to_update(i, j, tab):
    cpt = 0
    for a in range(-1, 2):
        for b in range(-1, 2):
            if tab[i + a][j + b] == 2:
                cpt += 1
    return cpt

def find_pos(start_pos, row_nb, col_nb, tab):
    res_list = []
    grid_size = len(tab)
    for i in range(start_pos[0] + 1, start_pos[0] + row_nb - 1):
        for j in range(start_pos[1] + 1, start_pos[0] + col_nb - 1):
            score = need_to_update(i, j, tab)
            res_list.append([score, i, j])

    res_list.sort(key=lambda x: x[0], reverse=True)
    i, j = res_list[0][1], res_list[0][2]
    return i, j                


def answer(case_nb):
    grid_size = 1000

    for _ in range(case_nb):
        tab = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        size = int(read_input())
        row_nb = int(sqrt(size))
        col_nb = ceil(size / row_nb)

        start_pos = [10, 10]

        for i in range(row_nb):
            for j in range(col_nb):
                tab[start_pos[0] + i][start_pos[1] + j] = 2

        for _ in range(1000):
            i, j = find_pos(start_pos, row_nb, col_nb, tab)
            write_output(i, j)
            k, l = read_coord()
            if k == 0 and l == 0:
                break

            tab[k][l] = 1

case_nb = int(read_input())
answer(case_nb)
