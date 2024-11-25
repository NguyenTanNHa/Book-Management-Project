﻿USE master
GO
CREATE DATABASE QUANLI_SACH
GO
USE QUANLI_SACH
GO
CREATE TABLE THELOAI (
  MA_THELOAI INTEGER PRIMARY KEY,
  TEN_THELOAI NVARCHAR(100) NOT NULL
);
GO
CREATE TABLE SACH (
  MASACH INTEGER PRIMARY KEY,
  TEN NVARCHAR(100) NOT NULL,
  SOLUONG INT,
  NAM_XUATBAN INTEGER,
  THELOAI INTEGER,
  GIA INTEGER NOT NULL,
  FOREIGN KEY (THELOAI) REFERENCES THELOAI (MA_THELOAI)
);
GO
CREATE TABLE NHANVIEN (
  MaNV INT PRIMARY KEY,
  HoTen NVARCHAR(100) NOT NULL,
  NgaySinh DATE NOT NULL,
  SoDienThoai VARCHAR(20) NOT NULL
);
GO
CREATE TABLE NHAP_SACH (
  MASACH INTEGER,
  TEN_SACH NVARCHAR(100) NOT NULL,
  NGAY_NHAP DATE,
  SOLUONG INTEGER,
  PRIMARY KEY (MASACH, NGAY_NHAP),
  FOREIGN KEY (MASACH) REFERENCES SACH(MASACH)
);
GO
CREATE TABLE NGUOIDOC (
  MA_NGUOIDOC INTEGER PRIMARY KEY,
  TEN NVARCHAR(100) NOT NULL,
  GIOI_TINH INT,
  NGAY_SINH DATE,
  MASACH INTEGER,
  FOREIGN KEY (MASACH) REFERENCES SACH(MASACH)
);
GO
CREATE TABLE PHIEUMUONSACH (
  MA_NGUOIMUON INTEGER PRIMARY KEY,
  TEN_NGUOIMUON NVARCHAR(100) NOT NULL,
  SOLUONG INT,
  MASACH INTEGER,
  NGAY_MUON DATE,
  NGAY_TRA DATE,
  MaNV INT,
  FOREIGN KEY (MASACH) REFERENCES SACH(MASACH),
  FOREIGN KEY (MaNV) REFERENCES NHANVIEN (MaNV)
);
GO

---chen du lieu vao bang----
INSERT INTO THELOAI (MA_THELOAI,TEN_THELOAI ) VALUES 
(1, N'Khoa học kỹ thuật'),
(2, N'Văn học nghệ thuật'),
(3, N'Lịch sử xã hội'),
(4, N'Giáo dục');
GO
INSERT INTO SACH (MASACH, TEN, SOLUONG, NAM_XUATBAN, THELOAI, GIA) VALUES 
(1, N'Tiểu thuyết Người lớn lên', 100, 2021, 2, 50000),
(2, N'Sách về Lịch sử Việt Nam', 50, 2018, 2, 120000),
(3, N'Văn học Nhật Bản', 30, 2020, 2, 85000),
(4, N'Sách Tiếng Việt 1', 50, 2010, 4, 20000),
(5, N'Muôn kiếp nhân sinh', 20, 2019, 1, 380000),
(6, N'Sách Toán lớp 10', 100, 2021, 4, 150000),
(7, N'Sách Tiếng Anh lớp 10', 120, 2021, 4, 100000),
(8, N'Sách Lịch sử lớp 10', 90, 2021, 4, 130000);
GO
INSERT INTO NHAP_SACH (MASACH, TEN_SACH, NGAY_NHAP, SOLUONG) VALUES 
(1, N'Sách toán', '2022-01-01', 50),
(2, N'Sách văn', '2022-02-02', 30),
(3, N'Sách lịch sử', '2022-03-03', 20),
(4, N'Sách khoa học', '2022-04-04', 40);
GO
INSERT INTO NGUOIDOC (MA_NGUOIDOC, TEN, GIOI_TINH, NGAY_SINH, MASACH) VALUES 
(1, N'Nguyễn Phương Nga', 0, '1990-01-01', 2),
(2, N'Cao Sơn Thạch', 1, '1998-01-20', 5),
(3, N'Nguyễn Văn Ka', 1, '2000-01-20', 5),
(4, N'Hoàng Kiều Anh', 0, '1994-07-16', 3),
(5, N'Lê Thị Thu Dung', 0, '1980-09-17', 3),
(6, N'Phan Hồng Hạnh', 0, '1991-04-04', 5),
(7, N'Đỗ Quang Lý', 1, '1956-12-28', 1);
GO
INSERT INTO PHIEUMUONSACH (MA_NGUOIMUON, TEN_NGUOIMUON, SOLUONG, MASACH, NGAY_MUON, NGAY_TRA) VALUES 
(1, N'Phạm Thanh Tuyền', 5, 1, '2022-03-01', '2022-03-08'),
(2, N'Lê Phương Anh', 2, 1, '2022-05-01', '2022-05-05'),
(3, N'Nguyễn Anh Sơn', 3,2, '2022-06-01', '2022-06-08');
GO
INSERT INTO NHANVIEN (MaNV, HoTen, NgaySinh, SoDienThoai) VALUES 
(700401, N'Nguyễn Thị Bích Quyên', '1993-07-17', '0937219976'),
(700402, N'Bùi Tấn Hảo', '1998-08-12', '0935564520');
GO
---FOREIGN KEY----
ALTER TABLE SACH ADD CONSTRAINT FK_SACH_THELOAI
  FOREIGN KEY (THELOAI) REFERENCES THELOAI (MA_THELOAI);

ALTER TABLE NHAP_SACH ADD CONSTRAINT FK_NHAP_SACH_SACH
  FOREIGN KEY (MASACH) REFERENCES SACH(MASACH);

ALTER TABLE NGUOIDOC ADD CONSTRAINT FK_NGUOIDOC_SACH
  FOREIGN KEY (MASACH) REFERENCES SACH(MASACH);

ALTER TABLE PHIEUMUONSACH ADD CONSTRAINT FK_PHIEUMUONSACH_SACH
  FOREIGN KEY (MASACH) REFERENCES SACH(MASACH);
GO

select * from THELOAI
select * from NGUOIDOC
select * from NHANVIEN
select * from PHIEUMUONSACH
select * from NGUOIDOC
select * from SACH