import matplotlib.pyplot as plt
import numpy as np
import pyodbc

server = 'Admin'
database = 'QUANLI_SACH'
username = 'TN'
password = '1407'

mydb = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = mydb.cursor()
cursor.execute("""
    SELECT S.TEN, COUNT(*) AS DOC, SUM(P.SOLUONG) AS MUON
    FROM SACH AS S
    LEFT JOIN PHIEUMUONSACH AS P ON S.MASACH = P.MASACH
    GROUP BY S.TEN
    ORDER BY MUON DESC, DOC DESC
    """)
result = cursor.fetchall()

books = [row[0] for row in result]
reads = [row[1] for row in result]
borrows = [row[2] if row[2] is not None else 0 for row in result]

fig, ax = plt.subplots()
ax.bar(books, borrows, color='tab:blue', label='Mượn')
ax.bar(books, reads, color='tab:orange', label='Đọc')
ax.set_xlabel('Tên sách')
ax.set_ylabel('Số lần')
ax.set_title('Tỉ lệ sách được đọc và mượn nhiều nhất')
ax.legend()
plt.xticks(rotation=90)
plt.tight_layout()

# Tính tổng số lượt mượn và đọc sách
total_borrows = sum(borrows)
total_reads = sum(reads)

# Vẽ biểu đồ tròn
labels = ['Đọc', 'Mượn']
sizes = [total_reads, total_borrows]
colors = ['tab:orange', 'tab:blue']
fig2, ax2 = plt.subplots()
ax2.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
ax2.set_title('Tỉ lệ sách được đọc và mượn nhiều nhất')
plt.show()
