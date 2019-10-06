k = int(input())
rn = list(map(int,input().split()))

s = set(rn)

sum_all = sum(rn)

sum_groups = sum([k*i for i in s])

captain_k = sum_groups - sum_all

captain_room = captain_k/(k-1)
print(captain_room)

# hash = {}
# for i in rn:
#     hash[i] = hash.get(i, 0) + 1
#
# for key, val in hash.items():
#     if val == 1:
#         print(key)
#         break
