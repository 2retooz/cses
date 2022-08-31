n = int(input())
array = list(map(int, input().split()))
answer, t = 0, array[0]

for i in array:
    t = max(t, i)
    answer += t - i

print(answer)
