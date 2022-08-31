n = int(input())
seq = list(map(int, input().split()))

given_sum = sum(seq)
total_sum = n * (n + 1) // 2

print(total_sum - given_sum)
