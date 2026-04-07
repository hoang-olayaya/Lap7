import pandas as pd

df = pd.read_csv("diem_sinhvien.csv")
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

# Hàm xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return "A"
    elif diem >= 7.0:
        return "B"
    elif diem >= 5.5:
        return "C"
    elif diem >= 4.0:
        return "D"
    else:
        return "F"

# Áp dụng hàm xếp loại
df["XepLoai"] = df["DiemTB"].apply(xep_loai)

print(df[["HoTen", "DiemTB", "XepLoai"]].head())