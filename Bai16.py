import pandas as pd

df = pd.read_csv("diem_sinhvien.csv")
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["XepLoai"] = df["DiemTB"].apply(lambda x: "A" if x>=8.5 else ("B" if x>=7 else ("C" if x>=5.5 else ("D" if x>=4 else "F"))))

# Tính tổng số sinh viên và điểm trung bình
tong_hop_cn = df.groupby("ChuyenNganh").agg(
    SoSinhVien=("MaSV", "count"),
    DiemTrungBinh=("DiemTB", "mean")
)

# Lọc và đếm sinh viên loại A, B
tyle_ab = df[df["XepLoai"].isin(["A", "B"])].groupby("ChuyenNganh")["MaSV"].count()

# Gộp kết quả
tong_hop_cn["SoDatAB"] = tyle_ab
tong_hop_cn["SoDatAB"] = tong_hop_cn["SoDatAB"].fillna(0)

# Tính tỷ lệ
tong_hop_cn["TyLeDatAB"] = (tong_hop_cn["SoDatAB"] / tong_hop_cn["SoSinhVien"]) * 100

print(tong_hop_cn.round(2))