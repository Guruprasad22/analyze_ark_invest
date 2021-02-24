from src.util.csv_reader import parse_daily_db_records, parse_master_records
from src.util.file_util import get_test_master_folder_path
import pytest


@pytest.mark.skip
def test_parse_daily_db_records():
    records = parse_daily_db_records()
    assert records is not None


def test_parse_master_records():
    records = parse_master_records(get_test_master_folder_path())
    print(f'type of record is {type(records)}')
    for item in records:
        print(item)
