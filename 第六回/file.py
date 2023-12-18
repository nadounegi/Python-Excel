from ctypes import wstring_at
from traceback import walk_stack
import openpyxl
import glob  # ファイル一覧を取得するためのモジュール
import os  # ファイルパスを操作するためのモジュール

wb = openpyxl.Workbook()
ws = wb.active
# ファイル一覧を取得する
fpath = os.path.abspath(".")
ws["A1"].value = fpath  # ファイル一覧を取得するディレクトリ
bfiles = glob.glob("./*")
for i, pname in enumerate(bfiles):
    fname = os.path.basename(pname)
    line = [i + 1, fname]
    ws.append(line)
wb.save("ファイル一覧.xlsx")
