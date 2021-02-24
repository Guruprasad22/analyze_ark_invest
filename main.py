from src.util.Dbutil import Dbutil
from src.util.csv_reader import parse_master_records
from src.util.excel_reader import read_all_daily_files
from src.util.file_util import get_master_folder_path

if __name__ == '__main__':
    print("choose from the following options : ")
    print("1: upload daily sheet and check for new buys")
    print("2: upload ETF master sheets ")
    print("3: truncate daily table")
    print("4: truncate master table")
    print("5: exit")
    choice = int(input("make your choice : "))
    if choice == 1:
        Dbutil.create_daily_table()
        Dbutil.truncate_table('ark_daily_staging')
        rows = read_all_daily_files()
        Dbutil.insert_into_daily_table(rows)
        new_buys = Dbutil.check_for_new_buys()
        Dbutil.update_master_with_daily_transactions(rows, new_buys)
        Dbutil.delete_positions_with_zero_records()
    elif choice == 2:
        Dbutil.create_master_table()
        rows = parse_master_records(get_master_folder_path())
        Dbutil.insert_into_master_table(rows)
    elif choice == 3:
        Dbutil.truncate_table('ark_portfolio_daily')
    elif choice == 4:
        Dbutil.truncate_table('ark_master')
    else:
        exit(0)
