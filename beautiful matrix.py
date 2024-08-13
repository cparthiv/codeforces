moves = 0
for i in range(1, 6):
    line = input().split(' ')
    for j in range(5):
        if line[j] == '1':
            moves = (abs(2 - j) + abs(3 - i))
print(moves)
