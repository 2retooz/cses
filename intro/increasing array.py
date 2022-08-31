n = int(input())
array = list(map(int, input().split()))
answer, max_ = 0, array[0]

for i in array:
    max_ = max(max_, i)
    answer += max_ - i

print(answer)
