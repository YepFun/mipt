n = int(input())
from_me = set(input() for _ in range(n))
m = int(input())
to_me = set(input() for _ in range(m))
friends = from_me
mutual_friends = from_me & to_me
also_friends = to_me - from_me
friends = list(friends)
mutual_friends = list(mutual_friends)
also_friends = list(also_friends)
friends.sort()
mutual_friends.sort()
also_friends.sort()
print("Friends:", ", ".join(friends))
print("Mutual Friends:", ", ".join(mutual_friends))
print("Also Friend of:", ", ".join(also_friends))

