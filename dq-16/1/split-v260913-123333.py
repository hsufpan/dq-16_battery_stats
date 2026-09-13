import pandas as pd
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

# 创建隐藏的 Tk 窗口
root = tk.Tk()
root.withdraw()

# 选择 CSV 文件
input_path = filedialog.askopenfilename(
    title="Select a CSV File",
    filetypes=[
        ("CSV 文件", "*.csv")
    ]
)

if not input_path:
    exit()

input_file = Path(input_path)

# 选择保存位置
output_dir = filedialog.askdirectory(
    title="Select a Path to Save"
)

if not output_dir:
    exit()

output_dir = Path(output_dir)

# 以字符串形式读取，保持 CSV 原始内容
df = pd.read_csv(
    input_file,
    dtype=str,
    keep_default_na=False
)

# 仅创建一个用于拆分的临时日期字段
date_column = pd.to_datetime(
    df["date-time"],
    format="%Y-%m-%d %H:%M"
).dt.date

# 按日期拆分
for date, group in df.groupby(date_column):
    output_file = output_dir / f"{date.strftime('%y%m%d')}.csv"

    # 写出时保持所有字段为字符串
    group.to_csv(
        output_file,
        index=False,
        lineterminator="\n"
    )

# 完成提示
messagebox.showinfo(
    "Completed",
    f"Total {date_column.nunique()} File(s)\n\n"
    f"Saved to \n{output_dir}"
)