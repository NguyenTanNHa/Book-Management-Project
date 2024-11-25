str = input()
print("string is: " , str)

res = str[0]
mid = int ( (len(str)/2))
res = res + str[mid]
last = len(str) -1
res = res + str[last]

print("New string: " , res)