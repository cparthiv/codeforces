args = input().split(' ')
scores = input().split(' ')
parts = 0
k = int(args[1])-1
for i in range(int(args[0])):
    if int(scores[i]) == int(scores[k]) or int(scores[i]) > int(scores[k]):
        if int(scores[i]) > 0:
            parts += 1
print(parts)
