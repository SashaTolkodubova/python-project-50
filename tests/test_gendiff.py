from gendiff.scripts.gendiff import generate_diff
from tests.fixtures.gendiff_unswer import unswer


def test_generate_diff_json():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'

    assert  generate_diff(file_path1, file_path2) == unswer


def test_generate_diff_yml():
    file_path1 = 'tests/fixtures/file1yml.yml'
    file_path2 = 'tests/fixtures/file2yml.yml'

    assert  generate_diff(file_path1, file_path2) == unswer
