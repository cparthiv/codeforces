alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
first = list(input())
second = list(input())
equal = True
for i in range(len(first)):
    if alphabet.index(first[i].lower()) > alphabet.index(second[i].lower()):
        print(1)
        equal = False
        break
    if alphabet.index(first[i].lower()) < alphabet.index(second[i].lower()):
        print(-1)
        equal = False
        break
if equal:
    print(0)
