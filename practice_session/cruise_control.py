def read_input():
    case_nb = int(input())
    input_data = []

    for _ in range(case_nb):
        dist, horse_nb = map(int, input().split(" "))
        horse_list = [[int(v) for v in input().split(" ")] for _ in range(horse_nb)]
        input_data.append([dist, horse_nb, horse_list])

    return case_nb, input_data

def write_output(case_nb, res_list):
    for i in range(case_nb):
        print("Case #{}: {:.6f}".format(i + 1, res_list[i]))

def solve(dist, horse_list):
    horse_list.sort(key=lambda x: x[0], reverse=True)

    finish_time = 0
    for start, speed in horse_list:
        rem_dist = dist - start
        time_to_finish = rem_dist / speed
        finish_time = max(finish_time, time_to_finish)

    my_speed = dist / finish_time
    return my_speed

def answer():
    case_nb, input_data = read_input()
    res_list = []
    for dist, horse_nb, horse_list in input_data:
        res_list.append(solve(dist, horse_list))

    write_output(case_nb, res_list)

answer()