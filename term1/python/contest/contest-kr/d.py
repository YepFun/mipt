k = int(input())
v = list(map(int, input().split()))
v.sort()
#print(*v)
supporters = 0
number_of_parties = len(v)//2 + 1
#print(number_of_parties)
for i in range(number_of_parties):
    #print(i, v[i]//2 + 1)
    supporters += (v[i]//2 + 1)
print(supporters)