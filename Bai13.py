import pandas as pd

df = pd.read_csv("diem_sinhvien.csv")
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

df["XepHangTrongLop"] = df.groupby("Lop")["DiemTB"].rank(ascending=False, method="dense")

ket_qua = df[["HoTen", "Lop", "DiemTB", "XepHangTrongLop"]].sort_values(["Lop", "XepHangTrongLop"])
print(ket_qua)