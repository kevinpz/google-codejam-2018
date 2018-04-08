from math import cos, sin, radians, sqrt, acos

def read_input():
    case_nb = int(input())
    input_data = []

    for _ in range(case_nb):
        input_data.append(float(input()))

    return case_nb, input_data

def write_output(case_nb, res_list):
    for i in range(case_nb):
        print("Case #{}:".format(i + 1))
        print("{} {} {}".format(res_list[i][0][0], res_list[i][0][1], res_list[i][0][2]))
        print("{} {} {}".format(res_list[i][1][0], res_list[i][1][1], res_list[i][1][2]))
        print("{} {} {}".format(res_list[i][2][0], res_list[i][2][1], res_list[i][2][2]))

def solve_eq(shadow_size):
    res_x = (2 * shadow_size + sqrt(-4 * shadow_size * shadow_size + 8)) / 4
    res_y = shadow_size - res_x
    return res_x / 2, res_y / 2

def solve(shadow_size):

    original_pos_x = [0.5, 0, 0]
    original_pos_y = [0, 0.5, 0]
    original_pos_z = [0, 0, 0.5]
    val_x, val_y = solve_eq(shadow_size)

    original_pos_x[0] = val_x
    original_pos_x[1] = val_y

    original_pos_y[0] = - val_y
    original_pos_y[1] = val_x

    return [original_pos_x, original_pos_y, original_pos_z]

def answer():
    case_nb, input_data = read_input()
    res_list = []
    for shadow_size in input_data:
        res_list.append(solve(shadow_size))

    write_output(case_nb, res_list)

answer()