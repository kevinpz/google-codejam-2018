from sys import stdout, exit

def write_output(data):
    print(data)
    stdout.flush()

def read_input():
    data = input()
    if data == "WRONG_ANSWER":
        exit()
    return data

def guess(start, end):
    return (start + end) // 2

def init_game():
    A, B = [int(s) for s in read_input().split(" ")]
    guess_nb = int(read_input())
    return A + 1, B, guess_nb

def answer(case_nb):
    for _ in range(case_nb):
        start, end, guess_nb = init_game()

        for _ in range(guess_nb):
            res = guess(start, end)
            write_output(res)
            ret = read_input()

            if ret == "CORRECT":
                break
            if ret == "TOO_SMALL":
                start = res + 1
            if ret == "TOO_BIG":
                end = res - 1

case_nb = int(read_input())
answer(case_nb)
