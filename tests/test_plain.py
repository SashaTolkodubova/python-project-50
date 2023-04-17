from gendiff.formatters.plain import plain
from gendiff.gendiff.gendiff import diff
from gendiff.scripts.Parsing import parsing
from tests.fixtures.plain_unswer import unswer


def test_plain_json():
    file1_path = 'tests/fixtures/file1.json'
    file2_path = 'tests/fixtures/file2.json'
    file1, file2 = parsing(file1_path, file2_path)
    assert plain(diff(file1, file2)) == unswer


def test_plain_yaml():
    file_path1 = 'tests/fixtures/file1yml.yml'
    file_path2 = 'tests/fixtures/file2yml.yml'
    file1, file2 = parsing(file_path1, file_path2)
    assert plain(diff(file1, file2)) == unswer