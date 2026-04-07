import pandas as pd

df = pd.read_csv("diem_sinhvien.csv")

bang_cheo = pd.crosstab(df["Lop"], df["GioiTinh"])
print(bang_cheo)