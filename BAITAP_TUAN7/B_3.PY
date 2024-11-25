#cauA#
A = [1, 2, 3, 1, 2, 5, 6, 7, 8]
B = []
for i in A:
  if i not in B:
    B.append(i)
print(B)

#cauB#
A = [1, 2, 3, 1, 2, 5, 6, 7, 8]
B = list(dict.fromkeys(A))
print(B)