import pandas as pd
import xlrd
from src.util.file_util import get_all_files_in_a_folder, get_input_file_path, normalize_daily_date


def parse_excel_file(file_name):
    print(f"now processing {file_name} ")
    book = xlrd.open_workbook(file_name)
    sh = book.sheet_by_index(0)
    all_rows = []
    for i in range(4, sh.nrows):
        new_row = []
        for j in range(0, sh.ncols):
            new_row.append(normalize_daily_date(sh.cell_value(i, j)) if j == 1 else sh.cell_value(i, j))
        all_rows.append(new_row)
    return all_rows


def read_all_daily_files():
    all_rows = []
    for file in get_all_files_in_a_folder(get_input_file_path()):
        rows = parse_excel_file(file)
        all_rows.extend(rows)
    rows_to_insert = [tuple(t) for t in all_rows]
    return rows_to_insert


def convert_rows_to_dataframe(rows):
    print(f"length of rows {len(rows)}")
    df = pd.DataFrame(rows[1:], columns=rows[0])
    print(f"length of df: {len(df)}")
    return df

