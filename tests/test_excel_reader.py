from src.util.excel_reader import convert_rows_to_dataframe, parse_excel_file
from src.util.file_util import get_test_input_file_path, get_test_resources_folder, get_test_master_folder_path,\
    get_all_files_in_a_folder


def test_parse_excel_file():
    for file in get_all_files_in_a_folder(get_test_input_file_path()):
        print('check1')
        rows = parse_excel_file(file)
        assert len(rows) > 0


def test_convert_rows_to_df():
    file = get_all_files_in_a_folder(get_test_input_file_path())[0]
    rows = parse_excel_file(file)
    df = convert_rows_to_dataframe(rows)
    assert len(df) > 0
    assert 'Buy' in df.columns.values
    print(df)

