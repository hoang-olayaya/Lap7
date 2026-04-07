import pandas as pd

df = pd.read_csv("diem_sinhvien.csv")
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["XepLoai"] = df["DiemTB"].apply(lambda x: "A" if x>=8.5 else ("B" if x>=7 else ("C" if x>=5.5 else ("D" if x>=4 else "F"))))

print("--- THỐNG KÊ THEO GIỚI TÍNH ---")
print(df["GioiTinh"].value_counts())

print("\n--- THỐNG KÊ THEO LỚP ---")
print(df["Lop"].value_counts())

print("\n--- THỐNG KÊ THEO CHUYÊN NGÀNH ---")
print(df["ChuyenNganh"].value_counts())

print("\n--- THỐNG KÊ THEO XẾP LOẠI ---")
print(df["XepLoai"].value_counts())