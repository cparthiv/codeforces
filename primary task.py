num_integers = int(input())
output_lines = []
for _ in range(num_integers):
    input_line = input()
    if input_line[:2] != '10':
        output_lines.append('NO')
        continue
    num_exponent = int(input_line[2:])
    if num_exponent < 2:
        output_lines.append('NO')
        continue
    if str(num_exponent) != input_line[2:]:
        output_lines.append('NO')
        continue
    output_lines.append('YES')
[print(x) for x in output_lines]
