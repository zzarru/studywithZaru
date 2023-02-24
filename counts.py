num_list = [0,4,1,3,1,2,4,1]
sort_list = [0] * len(num_list)

max = max(num_list)
counts = [0] * (max + 1)

for i in range(len(num_list)):
    #print(num_list[i])
    counts[num_list[i]] += 1


#print(counts)
for i in range(1, len(counts)):
    counts[i] += counts[i - 1]

#print(counts)

for i in range(len(num_list) - 1, -1, -1):
    #print(num_list[i])
    #print(counts[num_list[i]])
    #print(sort_list[counts[num_list[i]]])
    counts[num_list[i]] -= 1
    sort_list[counts[num_list[i]]] = num_list[i]

print(sort_list)