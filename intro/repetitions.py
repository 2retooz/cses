string = input()
answer, count, last_char = 1, 0, string[0]

for i in string:
    if i == last_char:
        count += 1
        answer = max(answer, count)
    else:
        last_char = i
        count = 1

print(answer)
