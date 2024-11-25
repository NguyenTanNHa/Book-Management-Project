#CauA#
A = [1,1,1,1,2,2,2,2,3,3,4,5,5]
B = {}
for i in A:
  if i in B:
    B[i] += 1
  else:
    B[i] = 1
for key, value in B.items():
  print(f"{key}: {value}")

#CauB#
A = [1,1,1,1,2,2,2,2,3,3,4,5,5]
B = {}
for i in A:
  B[i] = A.count(i)
for key, value in B.items():
  print(f"{key}: {value}")