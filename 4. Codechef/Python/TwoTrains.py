t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    k = sum(l)+max(l)
    print(k)
