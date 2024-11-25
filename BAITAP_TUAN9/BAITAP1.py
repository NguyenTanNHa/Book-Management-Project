import numpy as np
import matplotlib.pyplot as plt

#bieudocot
plt.bar([1,3,5,7,9], [100,200,300,400,500], label="Le", color="y")
plt.bar([2,4,6,8,10], [50,60,20,50,60], label="Chan", color="c")
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title('Ve hai bieu do')
plt.show()

#bieudobanh(pie chart)
D = {'CNTT':500, 'Toan':310 , 'Hoa': 150, 'Sinh': 280, 'Giao Duc':340}
plt.pie(D.values(), labels= D.keys(), autopct='%1.1f%%', shadow=True,  startangle=90)
plt.axis('equal')
plt.show()

#chia thành biểu đồ con
np.random.seed(19680801)
data = np.random.randn(2,100)
fig, axs = plt.subplots(2,2 ,figsize=(5,5))
axs[0,0].hist(data[0])
axs[1,0].scatter(data[0],data[1])
axs[0,1].plot(data[0],data[1])
axs[1,1].hist2d(data[0],data[1])
plt.show()

