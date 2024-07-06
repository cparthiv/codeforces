num_problems = int(input())
problems = 0
for i in range(num_problems):
    line = input()
    chars = line.split(' ')
    if chars.count('1') >= 2:
        problems += 1
print(problems)
