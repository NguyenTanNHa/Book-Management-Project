my_list = [12,24,35,70,88,120,155] 

result = [num for index, num in enumerate(my_list) if index+1 not in [1,2,3,6]] 

print(result)