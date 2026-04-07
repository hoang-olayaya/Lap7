import pandas as pd

df = pd.read_csv("diem_sinhvien.csv")

# Tính điểm trung bình theo trọng số
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

print(df[["MaSV", "HoTen", "DiemTB"]].head())