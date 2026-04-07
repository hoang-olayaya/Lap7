import pandas as pd

df = pd.read_csv("diem_sinhvien.csv")
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

print("Điểm trung bình:", df["DiemTB"].mean())
print("Điểm lớn nhất:", df["DiemTB"].max())
print("Điểm nhỏ nhất:", df["DiemTB"].min())
print("Độ lệch chuẩn:", df["DiemTB"].std())