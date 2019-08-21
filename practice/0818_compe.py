a = int(input())
s = input()

if a >= 3200:
    print(s)
else:
    print('red')

# A - Harmony
c,d = map(int,input().split())

if (c+d)%2 == 0:
    print((c+d)//2)
else:
    print('IMPOSSIBLE')


