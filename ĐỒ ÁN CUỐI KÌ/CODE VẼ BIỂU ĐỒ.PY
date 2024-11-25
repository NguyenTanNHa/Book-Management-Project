import matplotlib.pyplot as plt
import numpy as np
import pyodbc

server = 'Admin'  
database = 'QUANLI_SACH'
username = 'TN'
password = '1407'

mydb = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = mydb.cursor()
query = "SELECT MASACH, TEN, SOLUONG, NAM_XUATBAN, THELOAI, GIA  FROM SACH"
cursor.execute(query)
rows = cursor.fetchall()

# extract data from query result
TEN = [row[1] for row in rows]
GIA = [row[5] for row in rows]

# plot the bar chart
x_pos = np.arange(len(TEN))
plt.bar(x_pos, GIA, align='center', alpha=0.5)
plt.xticks(x_pos, TEN, rotation=90)
plt.ylabel('Giá sách')
plt.title('Biểu đồ giá sách theo tên sách')

plt.show()

