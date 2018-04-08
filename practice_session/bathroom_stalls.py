def read_input():
    case_nb = int(input())
    input_data = []

    for _ in range(case_nb):
        size, people = [int(s) for s in input().split(" ")]
        input_data.append([size, people])

    return case_nb, input_data

def write_output(case_nb, res_list):
    for i in range(case_nb):
        print("Case #{}: {} {}".format(i + 1, res_list[i][0], res_list[i][1]))

def solve(size, people):
    power_two = 1
    while power_two * 2 <= people:
        power_two *= 2
    next_power_two = power_two * 2

    mid = (next_power_two + power_two) / 2

    if people < mid:
        res = size // power_two
    else:
        res = (size - 1) // power_two

    if people % 2 == 1:
        res -= 1



    left_el = res // 2
    right_el = max((res - 1) // 2, 0)

    return [max(left_el, right_el), min(left_el, right_el)]

def answer():
    case_nb, input_data = read_input()
    res_list = []
    for size, people in input_data:
        res_list.append(solve(size, people))

    write_output(case_nb, res_list)

answer()