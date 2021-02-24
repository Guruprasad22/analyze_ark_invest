from src.util.file_util import get_resources_folder, get_db_path, get_archive_folder_path, get_input_file_path,\
                            get_all_files_in_a_folder, move_files_in_folder, get_master_folder_path,\
                            get_test_resources_folder, get_test_input_file_path,get_test_master_folder_path
import pytest


def test_resources_folder():
    assert 'resources' in get_resources_folder()
    assert 'src' in get_resources_folder()


def test_get_db_path():
    assert 'ark.db' in get_db_path()
    assert 'resources' in get_db_path()


def test_get_input_file_path():
    assert 'input' in get_input_file_path()


def test_get_master_folder_path():
    assert 'master' in get_master_folder_path()


def test_get_archive_folder_path():
    assert 'archive' in get_archive_folder_path()


def test_get_all_files_in_folder():
    files = get_all_files_in_a_folder(get_input_file_path())
    assert files is not None
    for file in files:
        print(file)


# @pytest.mark.skip(reason="no need to test his every time")
def test_move_files_in_folder(tmp_path):
    d = tmp_path / "src"
    d.mkdir()  # create a subdirectory
    p = d / "hello.txt"
    p.write_text("hello hello hello")
    assert p.read_text() == "hello hello hello"
    assert len(list(tmp_path.iterdir())) == 1
    d1 = tmp_path / "dest"
    d1.mkdir()
    assert len(list(tmp_path.iterdir())) == 2
    p1 = d1 / "hello.txt"
    with pytest.raises(FileNotFoundError):
        p1.read_text()
    move_files_in_folder(d, d1)
    assert p1.read_text() == "hello hello hello"


def test_resources_folder_structure_for_unit_tests():
    assert 'resources' in get_test_resources_folder()
    assert 'tests' in get_test_resources_folder()
    assert 'tests' in get_test_resources_folder()
    assert 'tests' in get_test_input_file_path()
    assert 'master' in get_test_master_folder_path()
    assert 'tests' in get_test_master_folder_path()


