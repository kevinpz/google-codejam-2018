def read_input():
    case_nb = int(input())
    input_data = []

    for _ in range(case_nb):
        nb = int(input())
        item_list = [int(s) for s in input().split(" ")]
        input_data.append([nb, item_list])

    return case_nb, input_data

def write_output(case_nb, res_list):
    for i in range(case_nb):
        print("Case #{}: {}".format(i + 1, res_list[i]))

def trouble_sort(nb, item_list):

    odd_list = [nb for idx, nb in enumerate(item_list) if idx % 2 == 1 ]
    even_list = [nb for idx, nb in enumerate(item_list) if idx % 2 == 0 ]

    odd_list.sort()
    even_list.sort()

    for i in range(nb - 1):
        if i % 2 == 0 and even_list[i // 2] > odd_list[i // 2]:
            return i
        elif i % 2 == 1 and odd_list[i // 2] > even_list[i // 2 + 1]:
            return i

    return "OK"

def answer():
    case_nb, input_data = read_input()
    res_list = []
    for nb, item_list in input_data:
        res_list.append(trouble_sort(nb, item_list))

    write_output(case_nb, res_list)

answer()