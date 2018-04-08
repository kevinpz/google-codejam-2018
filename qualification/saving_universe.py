def read_input():
    case_nb = int(input())
    input_data = []

    for _ in range(case_nb):
        values = input().split(" ")
        damage, action = int(values[0]), values[1]
        input_data.append([damage, action])

    return case_nb, input_data

def write_output(case_nb, res_list):
    for i in range(case_nb):
        print("Case #{}: {}".format(i + 1, res_list[i]))

def calc_score(action):
    dmg = 1
    total = 0
    for s in action:
        if s == "S":
            total += dmg
        else:
            dmg *= 2

    return total

def solve(damage, action):

    act = 0
    size = len(action)

    while calc_score(action) > damage:
        rev_act = action[::-1]
        rev_idx = rev_act.find('SC')
        if rev_idx == -1:
            break
        idx = size - rev_idx - 2
        lst_act = list(action)
        lst_act[idx], lst_act[idx + 1] = lst_act[idx + 1], lst_act[idx]
        action = ''.join(lst_act)
        act += 1

    if calc_score(action) > damage:
        return "IMPOSSIBLE"

    return act

def answer():
    case_nb, input_data = read_input()
    res_list = []
    for damage, action in input_data:
        res_list.append(solve(damage, action))

    write_output(case_nb, res_list)

answer()