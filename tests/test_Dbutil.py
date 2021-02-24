from src.util.file_util import get_db_path, get_master_folder_path
from src.util.Dbutil import Dbutil
from src.util.csv_reader import parse_daily_db_records, parse_master_records
import sqlite3
import pytest


def test_table_exists():
    Dbutil.create_daily_table()
    conn = sqlite3.connect(get_db_path())
    assert conn
    curr = conn.cursor()
    curr.execute(''' SELECT name FROM sqlite_master WHERE type='table' AND name='ark_daily_rolling' ''')
    result = curr.fetchone()
    assert result[0] == 'ark_daily_rolling'
    Dbutil.create_master_table()
    curr.execute(''' SELECT name FROM sqlite_master WHERE type='table' AND name='ark_master' ''')
    result = curr.fetchone()
    assert result[0] == 'ark_master'


def test_insert_into_daily_table():
    records = parse_daily_db_records()
    Dbutil.insert_into_daily_table(records)
    conn = sqlite3.connect(get_db_path())
    assert conn
    curr = conn.cursor()
    curr.execute(''' SELECT count(*) FROM ark_daily_rolling''')
    record_count = curr.fetchone()
    assert record_count[0] > 0


def test_insert_into_master_table():
    records = parse_master_records(get_master_folder_path())
    Dbutil.insert_into_master_table(records)
    conn = sqlite3.connect(get_db_path())
    assert conn
    curr = conn.cursor()
    curr.execute('select count(*) from ark_master')
    record_count = curr.fetchone()
    assert record_count[0] > 15


def test_check_for_new_buys():
    Dbutil.check_for_new_buys()


@pytest.mark.skip
def test_truncate_table():
    Dbutil.truncate_table('ark_portfolio_daily')
    Dbutil.truncate_table('ark_master')