def stringCompare(data): 
  return sorted(data) 

def integerCompare(data): 
  return sorted(data, key = int) 
  
A = ['3', '27', '5', '123', '9', '1']
print("String compare: ", stringCompare(A)) 
print("Integer compare: ", integerCompare(A))