num_lines = int(input())
x = 0
for i in range(num_lines):
    line = input()
    for c in line:
        if c == '+':
            x += 0.5
        if c == '-':
            x -= 0.5
print(int(x))
