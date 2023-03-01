def write(result):
    with open('res.txt', 'r') as file:
        s = file.readlines()
    with open('res.txt', 'w') as file:
        s.append(str(result) + '\n')
        file.write(''.join(s))
