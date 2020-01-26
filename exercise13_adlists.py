friends ={"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
nonlocal_friends = abroad.difference(friends)
joined_friends = friends.union(abroad)
both = friends.intersection(abroad)

print(local_friends)
print(nonlocal_friends)
print(joined_friends)
print(both)