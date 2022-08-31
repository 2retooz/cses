n = int(input())
string = map(int, input().split())

given_sum = sum(list(string))
total_sum = n * (n + 1) // 2

print(total_sum - given_sum)
