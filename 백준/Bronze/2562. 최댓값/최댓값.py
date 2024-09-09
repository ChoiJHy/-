num_list =[]

for i in range(9):
    input_value = int(input())
    num_list.append(input_value)
    
max_value = max(num_list)
idx = num_list.index(max_value)

print(max_value)
print(idx + 1)