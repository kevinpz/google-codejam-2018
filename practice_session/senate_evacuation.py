class Senator():
    def __init__(self, idx, number, total):
        self.total = total
        self.number = number
        self.evacuated = 0
        self.all_evacuated = False
        self.evacuated_percent = self.evacuated / self.total * 100
        self.letter = chr(65 + idx)

    def evacuate(self):
        self.evacuated += 1
        if self.evacuated == self.number:
            self.all_evacuated = True
        self.evacuated_percent = self.evacuated / self.total * 100

    def __str__(self):
        return "Letter: {} Number: {} Evacuated: {} Remaining: {} Percent: {} All evacuated: {}".format(self.letter, self.number, self.evacuated, self.remaining, self.evacuated_percent, self.all_evacuated) 

def write_output(case_nb, data):
    for i in range(case_nb):
        print("Case #{}: {}".format(i + 1, data[i]))

def read_data(case_nb):
    input_list = []
    for i in range(case_nb):
        party_nb = int(input())
        sen_nb = [int(s) for s in input().split(" ")]
        input_list.append([party_nb, sen_nb])
    return input_list

def find_best_party(sen_list):
    sen_list.sort(key=lambda x: x.evacuated_percent)
    for s in sen_list:
        if not s.all_evacuated:
            s.evacuate()
            return s.letter
    return ""

def evacuate(party_nb, data_list):
    res_tab = []
    total_sen = sum(data_list)
    evacuate_nb = 0
    sen_list = []

    for i in range(party_nb):
        sen_list.append(Senator(i, data_list[i], total_sen))

    while evacuate_nb < total_sen:
        ev = find_best_party(sen_list)
        ev += find_best_party(sen_list)
        res_tab.append(ev)
        evacuate_nb += 2

    res_tab = list(reversed(res_tab))
    res = " ".join(res_tab)

    return res

def answer(case_nb):
    out_list = []
    senate_list = read_data(case_nb)

    for party_nb, data_list in senate_list:
        out_list.append(evacuate(party_nb, data_list))

    write_output(case_nb, out_list)

case_nb = int(input())
answer(case_nb)