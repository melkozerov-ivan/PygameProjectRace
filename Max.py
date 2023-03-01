def maximum():
    with open('res.txt', 'r') as file:
        a = list(map(int, file.readlines()))
    return max(a)
