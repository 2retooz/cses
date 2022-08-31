n = int(input())
seq = map(int, input().split())

given_sum = sum(list(seq))
total_sum = n * (n + 1) // 2

print(total_sum - given_sum)
