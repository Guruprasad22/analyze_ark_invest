from src.util.file_util import get_all_files_in_a_folder, get_input_file_path, normalize_master_date
import csv


def parse_daily_db_records():
    rows = []
    for file in get_all_files_in_a_folder(get_input_file_path()):
        print(f'processing... {file}')
        with open(file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = [(row['FUND'], row['Date'], row['Direction'], row['Ticker'], row['CUSIP'], row['Name'],
                     row['Shares'], row['% of ETF']) for row in reader]
    return rows


def parse_master_records(folder_path):
    rows = []
    for file in get_all_files_in_a_folder(folder_path):
        print(f'processing... {file}')
        with open(file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            rows.extend([(normalize_master_date(row['date']), row['fund'], row['company'], row['ticker'], row['cusip'],
                    row['shares'], row['market value($)'], row['weight(%)']) for row in reader if '/' in row['date']])
    return rows
