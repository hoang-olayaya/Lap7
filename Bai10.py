import pandas as pd

df = pd.read_csv("diem_sinhvien.csv")
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["XepLoai"] = df["DiemTB"].apply(lambda x: "A" if x>=8.5 else ("B" if x>=7 else ("C" if x>=5.5 else ("D" if x>=4 else "F"))))

pivot1 = pd.pivot_table(
    df,
    index="Lop",
    columns="XepLoai",
    values="MaSV",
    aggfunc="count",
    fill_value=0
)
print(pivot1)