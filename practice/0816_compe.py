a,b = map(int, input().split())

plus = a+b
minus = a-b
multipiled_by = a*b
ans = max([plus, minus, multipiled_by])
print(ans)