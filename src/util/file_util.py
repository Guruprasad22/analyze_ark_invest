import datetime
import glob
import os
import shutil


def get_resources_folder():
    project_root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
    resource_path = os.path.join(project_root_dir, "src", "resources")
    return resource_path


def get_db_path():
    db_path = os.path.join(get_resources_folder(), "database", "ark.db")
    return db_path


def get_input_file_path():
    file_path = os.path.join(get_resources_folder(), 'input', 'daily')
    return file_path


def get_master_folder_path():
    file_path = os.path.join(get_resources_folder(), 'input', 'master')
    return file_path


def get_archive_folder_path():
    file_path = os.path.join(get_resources_folder(), 'archive')
    return file_path


def get_all_files_in_a_folder(dir_path):
    files = glob.glob(os.path.join(dir_path, "*.*"))
    return files


def move_files_in_folder(source_dir, target_dir):
    files_to_move = get_all_files_in_a_folder(source_dir)
    for file in files_to_move:
        shutil.move(file, target_dir)


def get_test_resources_folder():
    project_root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)[0]
    resource_path = os.path.join(project_root_dir, "tests", "resources")
    return resource_path


def get_test_input_file_path():
    file_path = os.path.join(get_test_resources_folder(), 'daily')
    return file_path


def get_test_master_folder_path():
    file_path = os.path.join(get_test_resources_folder(), 'master')
    return file_path


def normalize_daily_date(date_str):
    formatted_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').strftime('%m-%d-%Y')
    return formatted_date


def normalize_master_date(date_str):
    formatted_date = datetime.datetime.strptime(date_str, '%m/%d/%Y').strftime('%m-%d-%Y')
    return formatted_date
