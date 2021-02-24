import sqlite3

from rich.console import Console

from src.util.file_util import get_db_path, move_files_in_folder, get_input_file_path, get_archive_folder_path, \
    get_master_folder_path

console = Console()


class Dbutil:

    @staticmethod
    def create_daily_table():
        conn = sqlite3.connect(get_db_path())
        curr = conn.cursor()
        # create daily staging table
        curr.execute("""CREATE TABLE IF NOT EXISTS ark_daily_staging
                    (fund TEXT ,
                    date TEXT,
                    direction TEXT,
                    ticker TEXT,
                    cusip TEXT,
                    name TEXT,
                    shares INT,
                    '% of ETF' REAL)""")
        conn.commit()
        # create daily rolling table
        curr.execute("""CREATE TABLE IF NOT EXISTS ark_daily_rolling
                            (fund TEXT NOT NULL,
                            date TEXT NOT NULL,
                            direction TEXT NOT NULL,
                            ticker TEXT,
                            cusip TEXT NOT NULL,
                            name TEXT,
                            shares INT,
                            '% of ETF' REAL)""")
        conn.commit()
        conn.close()

    @staticmethod
    def create_master_table():
        conn = sqlite3.connect(get_db_path())
        curr = conn.cursor()
        # create daily staging table
        curr.execute("""CREATE TABLE IF NOT EXISTS ark_master
                    (date TEXT,
                    fund TEXT,
                    company TEXT,
                    ticker TEXT,
                    cusip TEXT,
                    shares INT,
                    'market value($)' REAL, 
                   'weight(%)' REAL)""")
        conn.commit()
        conn.close()

    @staticmethod
    def insert_into_daily_table(rows):
        conn = sqlite3.connect(get_db_path())
        curr = conn.cursor()
        curr.executemany('''INSERT INTO ark_daily_staging 
        ('FUND', 'Date', 'Direction', 'Ticker', 'CUSIP', 'Name', 'Shares', '% of ETF') 
        values(?, ?, ?, ?, ?, ?, ?, ?);''', rows)
        curr.executemany('''INSERT INTO ark_daily_rolling 
               ('FUND', 'Date', 'Direction', 'Ticker', 'CUSIP', 'Name', 'Shares', '% of ETF') 
               values(?, ?, ?, ?, ?, ?, ?, ?);''', rows)
        conn.commit()
        conn.close()
        move_files_in_folder(get_input_file_path(), get_archive_folder_path())

    @staticmethod
    def insert_into_master_table(rows):
        conn = sqlite3.connect(get_db_path())
        curr = conn.cursor()
        curr.executemany('''INSERT INTO ark_master 
            ('date', 'fund', 'company', 'ticker', 'cusip', 'shares', 'market value($)', 'weight(%)') 
            values(?, ?, ?, ?, ?, ?, ?, ?);''', rows)
        conn.commit()
        conn.close()
        move_files_in_folder(get_master_folder_path(), get_archive_folder_path())

    @staticmethod
    def check_for_new_buys():
        conn = sqlite3.connect(get_db_path())
        curr = conn.cursor()
        curr.execute('''SELECT Date, FUND, Ticker, Ticker, CUSIP, Shares, Shares, Shares FROM ark_daily_staging
            WHERE Ticker NOT IN (
            SELECT DISTINCT ticker FROM ark_master)''')
        rows = curr.fetchall()
        new_buys = []
        if rows is None or len(rows) == 0:
            console.print("no new BUYS today", style="bold green")
        else:
            console.print('these are the new buys....', style="bold red")
            for row in rows:
                console.print(row[2], style="bold green")
                new_buys.append(row[4])
            print('adding the new tickers to master table')
            Dbutil.insert_into_master_table(rows)
            Dbutil.truncate_table('ark_daily_staging')
        return new_buys

    @staticmethod
    def update_master_with_daily_transactions(rows, new_buys):
        conn = sqlite3.connect(get_db_path())
        curr = conn.cursor()
        for row in rows:
            if row[2] == 'Buy' and row[4] not in new_buys:
                # print('--------BUY-------------------')
                # print(f'row[6] : {row[6]}')
                # print(f'row [4] : {row[4]}')
                # print(f'row[0]: {row[0]}')
                curr.execute('''UPDATE ark_master set shares = shares + ?
                    WHERE cusip = ? AND fund = ?''', (row[6], row[4], row[0],))
            elif row[2] == 'Sell' and row[4] not in new_buys:
                # print('--------SELL-------------------')
                # print(f'row[6] : {row[6]}')
                # print(f'row [4] : {row[4]}')
                # print(f'row[0]: {row[0]}')
                curr.execute('''UPDATE ark_master set shares = shares - ?
                                    WHERE cusip = ? AND fund = ?''', (row[6], row[4], row[0],))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_positions_with_zero_records():
        conn = sqlite3.connect(get_db_path())
        curr = conn.cursor()
        curr.execute('''DELETE FROM ark_master WHERE
                       shares = 0''')
        conn.commit()
        conn.close()

    @staticmethod
    def truncate_table(name):
        conn = sqlite3.connect(get_db_path())
        curr = conn.cursor()
        curr.execute(f'DELETE FROM {name}')
        conn.commit()
        conn.close()