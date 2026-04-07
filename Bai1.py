import pandas as pd
import numpy as np

df = pd.read_csv("diem_sinhvien.csv")

print("--- 5 DÒNG ĐẦU ---")
print(df.head())

print("\n--- 5 DÒNG CUỐI ---")
print(df.tail())

print("\n--- THÔNG TIN CẤU TRÚC ---")
df.info()

print("\n--- THỐNG KÊ MÔ TẢ ---")
print(df.describe())