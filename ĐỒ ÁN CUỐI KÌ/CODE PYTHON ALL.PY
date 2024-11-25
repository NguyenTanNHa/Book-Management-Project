import pyodbc
from prettytable import prettytable

server = 'Admin'  
database = 'QUANLI_SACH'
username = 'TN'
password = '1407'

mydb = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

class THELOAI: #LỚP THỂ LOẠI
    def __init__(self, MA_THELOAI, TEN_THELOAI, server, database, username, password):
        self.connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        self.mycursor = self.connection.cursor()
        self.MA_THELOAI = MA_THELOAI
        self.TEN_THELOAI = TEN_THELOAI
    
    def display_table(self):
        self.mycursor.execute("SELECT * FROM THELOAI")
        rows = self.mycursor.fetchall()
        table = prettytable.PrettyTable(["MA_THELOAI", "TEN_THELOAI"])
        for row in rows:
            table.add_row(row)
        print(table)

class Sach: #LỚP SÁCH
    def __init__(self, ma_sach, ten_sach, so_luong, nam_xuat_ban, ma_theloai, gia):
        self.connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        self.mycursor = self.connection.cursor()
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.so_luong = so_luong
        self.nam_xuat_ban = nam_xuat_ban
        self.ma_theloai = ma_theloai
        self.gia = gia
    
    def them_sach(self):
        sql = "INSERT INTO SACH (MASACH, TEN, SOLUONG, NAM_XUATBAN, THELOAI, GIA) VALUES (?, ?, ?, ?, ?, ?)"
        values = (self.ma_sach, self.ten_sach, self.so_luong, self.nam_xuat_ban, self.ma_theloai, self.gia)
        self.mycursor.execute(sql, values)
        self.connection.commit()
        print(f"Thêm sách {self.ten_sach} thành công!")

    def xoa_sach(self):
        ma_sach = input("Nhập mã sách cần xóa: ")
        sql = "DELETE FROM SACH WHERE MASACH = ?"
        values = (ma_sach,)
        self.mycursor.execute(sql, values)
        self.connection.commit()
        print(f"Đã xóa sách có mã {ma_sach} thành công!")

    def hien_thi_sach(self):
        sql = "SELECT * FROM SACH"
        self.mycursor.execute(sql)
        rows = self.mycursor.fetchall()
        table = prettytable.PrettyTable(["MASACH", "TEN", "SOLUONG", "NAM_XUATBAN", "THELOAI", "GIA"])
        for row in rows:
            table.add_row(row)
        print(table)

    def tim_sach_theo_ma(self):
        ma_sach = input("Nhập mã sách: ")
        sql = "SELECT * FROM SACH WHERE MASACH = ?"
        values = (ma_sach, )
        self.mycursor.execute(sql, values)
        result = self.mycursor.fetchall()
        if len(result) == 0:
            print("Không tìm thấy thông tin sách với mã sách này.")
        else:
            print("{:<15} {:<20} {:<10} {:<15} {:<10} {:<10}".format("Mã sách", "Tên sách", "Số lượng", "Năm xuất bản", "Thể loại", "Giá"))
        for row in result:
            print("{:<15} {:<20} {:<10} {:<15} {:<10} {:<10}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

    def cap_nhat_gia_sach(self):
        gia_moi = input("Nhập giá mới cho sách: ")
        sql = "UPDATE SACH SET GIA = ? WHERE MASACH = ?"
        values = (gia_moi, self.ma_sach)
        self.mycursor.execute(sql, values)
        self.connection.commit()
        print(f"Đã cập nhật giá mới {gia_moi} cho sách có mã {self.ma_sach}!")

class NHANVIEN: #BẢNG NHÂN VIÊN
    def __init__(self, MaNV, HoTen, NgaySinh, SoDienThoai):
        self.connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        self.mycursor = self.connection.cursor()
        self.MaNV = MaNV
        self.HoTen = HoTen
        self.NgaySinh = NgaySinh
        self.SoDienThoai = SoDienThoai

    def them_nhanvien(self):
        sql = "INSERT INTO NHANVIEN (MaNV, HoTen, NgaySinh, SoDienThoai) VALUES (?, ?, ?, ?)"
        values = (self.MaNV, self.HoTen, self.NgaySinh, self.SoDienThoai)
        self.mycursor.execute(sql, values)
        self.connection.commit()
        print(f"Thêm nhân viên {self.HoTen} thành công!")

    def sua_nhanvien(self, field, new_value):
        sql = f"UPDATE NHANVIEN SET {field} = ? WHERE MaNV = ?"
        values = (new_value, self.MaNV)
        self.mycursor.execute(sql, values)
        self.connection.commit()
        print(f"Cập nhật thông tin nhân viên {self.HoTen} thành công!")

    def xoa_nhanvien(self):
        sql = "DELETE FROM NHANVIEN WHERE MaNV = ?"
        values = (self.MaNV,)
        self.mycursor.execute(sql, values)
        self.connection.commit()
        print(f"Xóa nhân viên {self.HoTen} thành công!")

    def hien_thi_nhanvien(self):
        # Hiển thị tất cả nhân viên trong bảng NHANVIEN
        sql = "SELECT * FROM NHANVIEN"
        self.mycursor.execute(sql)
        result = self.mycursor.fetchall()
        for row in result:
            print(row)


class NHAP_SACH: #BẢNG NHẬP SÁCH
    def __init__(self, MASACH, TEN_SACH, NGAY_NHAP, SOLUONG):
        self.connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        self.mycursor = self.connection.cursor()
        self.MASACH = MASACH
        self.TEN_SACH = TEN_SACH
        self.NGAY_NHAP = NGAY_NHAP
        self.SOLUONG = SOLUONG
        
    def nhap_sach_moi(self):
        self.MASACH = input("Nhập mã sách mới: ")
        self.TEN = input("Nhập tên sách mới: ")
        self.SOLUONG = int(input("Nhập số lượng sách mới: "))
        self.NAM_XUATBAN = int(input("Nhập năm xuất bản sách mới: "))
        self.THELOAI = int(input("Nhập thể loại sách mới: "))
        self.GIA = int(input("Nhập giá sách mới: "))
        
        sql = f"INSERT INTO SACH (MASACH, TEN, SOLUONG, NAM_XUATBAN, THELOAI, GIA) VALUES (?, ?, ?, ?, ?, ?)"
        values = (self.MASACH, self.TEN, self. SOLUONG, self.NAM_XUATBAN, self.THELOAI, self.GIA)

        try:
            self.mycursor.execute(sql, values)
            self.connection.commit()
            print("Thêm sách mới thành công!")
        except:
            self.connection.rollback()
            print("Thêm sách mới thất bại!")
        
    def hien_thi_sach(self):
        sql = "SELECT * FROM SACH"
        self.mycursor.execute(sql)
        result = self.mycursor.fetchall()
        
        print("{:<15} {:<20} {:<10} {:<15} {:<10} {:<10}".format("Mã sách", "Tên sách", "Số lượng", "Năm xuất bản", "Thể loại", "Giá"))
        for row in result:
            print("{:<15} {:<20} {:<10} {:<15} {:<10} {:<10}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
        
        self.mycursor.close()
        self.connection.close()


class NGUOIDOC: #BẢNG NGƯỜI ĐỌC
    def __init__(self, ma_nguoidoc, ten, gioi_tinh, ngay_sinh, masach):
        self.connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        self.mycursor = self.connection.cursor()
        self.ma_nguoidoc = ma_nguoidoc
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.ngay_sinh = ngay_sinh
        self.masach = masach
        
    def insert(self):
        query = "INSERT INTO NGUOIDOC (MA_NGUOIDOC, TEN, GIOI_TINH, NGAY_SINH, MASACH) VALUES (?, ?, ?, ?, ?)"
        values = (self.ma_nguoidoc, self.ten, self.gioi_tinh, self.ngay_sinh, self.masach)
        self.mycursor.execute(query, values)
        self.connection.commit()
        print(self.mycursor.rowcount, "record inserted.")
        
    def update(self):
        query = "UPDATE NGUOIDOC SET TEN = ?, GIOI_TINH = ?, NGAY_SINH = ?, MASACH = ? WHERE MA_NGUOIDOC = ?"
        values = (self.ten, self.gioi_tinh, self.ngay_sinh, self.masach, self.ma_nguoidoc)
        self.mycursor.execute(query, values)
        self.connection.commit()
        print(self.mycursor.rowcount, "record(s) affected.")
        
    def delete(self):
        query = "DELETE FROM NGUOIDOC WHERE MA_NGUOIDOC = ?"
        values = (self.ma_nguoidoc,)
        self.mycursor.execute(query, values)
        self.connection.commit()
        print(self.mycursor.rowcount, "record(s) deleted.")
        
    def get_all():
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        mycursor = connection.cursor()
        query = "SELECT * FROM NGUOIDOC"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        nguoidocs = []
        for row in rows:
            nguoidoc = NGUOIDOC(row[0], row[1], row[2], row[3], row[4])
            nguoidocs.append(nguoidoc)
        return nguoidocs


class PHIEUMUONSACH: #BẢNG MƯỢN SÁCH
    def __init__(self, MA_NGUOIMUON, TEN_NGUOIMUON, SOLUONG, MASACH, NGAY_MUON, NGAY_TRA, MaNV):
        self.connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        self.mycursor = self.connection.cursor()
        self.MA_NGUOIMUON = MA_NGUOIMUON
        self.TEN_NGUOIMUON = TEN_NGUOIMUON
        self.SOLUONG = SOLUONG
        self.MASACH = MASACH
        self.NGAY_MUON = NGAY_MUON
        self.NGAY_TRA = NGAY_TRA
        self.MaNV = MaNV

    def save(self):
        query = f"INSERT INTO PHIEUMUONSACH (MA_NGUOIMUON, TEN_NGUOIMUON, SOLUONG, MASACH, NGAY_MUON, NGAY_TRA, MaNV) VALUES (?, ?, ?, ?, ?, ?, ?)"
        values = (self.MA_NGUOIMUON, self.TEN_NGUOIMUON, self.SOLUONG, self.MASACH, self.NGAY_MUON, self.NGAY_TRA, self.MaNV)
        self.mycursor.execute(query, values)
        self.connection.commit()

    def get_all():
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        mycursor = connection.cursor()
        query = "SELECT * FROM PHIEUMUONSACH"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        phieumuonsachs = []
        for row in rows:
            phieumuonsach = PHIEUMUONSACH(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            phieumuonsachs.append(phieumuonsach)
        return phieumuonsachs

#Tạo Menu
cursor = mydb.cursor()

while True:
    print("=======================================")
    print("                 MENU                  ")
    print("=======================================")
    print("1. Hiển Thị Danh Sách")
    print("2. Cập Nhật Thêm Sách")
    print("3. Tìm Kiếm Thông Tin Sách Theo Mã Sách")
    print("4. Cập Nhật Đơn Giá Sách Theo Mã Sách")
    print("5. Xóa Một Sản Phẩm Theo Mã Sách")
    print("6. Thoát Chương Trình")
    print("=======================================")


    # prompt user for choice
    choice = int(input("Nhập lựa chọn của bạn: "))
    
    if choice == 1:
        sach = Sach('', '', 0, 0, '', 0)
        sach.hien_thi_sach()
        
    elif choice == 2:
        nhap_sach = NHAP_SACH('', '', '', 0)
        nhap_sach.nhap_sach_moi()

    elif choice == 3:
        ma_sach = input("Nhập mã sách cần tìm: ")
        sach = Sach(ma_sach, None, None, None, None, None)
        sach.tim_sach_theo_ma()

    elif choice == 4:
        ma_sach = input("Nhập mã sách cần cập nhật giá: ")
        sach = Sach('', '', 0, '', '', 0)
        sach.ma_sach = ma_sach
        sach.cap_nhat_gia_sach()


    elif choice == 5:
        ma_sach = input("Nhập mã sách cần xóa: ")
        sach = Sach(ma_sach, "", 0, 0, "", 0) 
        sach.xoa_sach()

    elif choice == 6:
        print("Chào tạm biệt, chúc bạn một ngày tốt lành !")
        break
 



    


