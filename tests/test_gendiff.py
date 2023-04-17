from gendiff.gendiff_p.gendiff import diff
from tests.fixtures.gendiff_unswer import unswer
from gendiff.formatters.stylish import stylish
from gendiff.scripts.Parsing import parsing


def test_generate_diff_json():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    file1, file2 = parsing(file_path1, file_path2)

    assert stylish(diff(file1, file2)) == unswer


def test_generate_diff_yml():
    file_path1 = 'tests/fixtures/file1yml.yml'
    file_path2 = 'tests/fixtures/file2yml.yml'
    file1, file2 = parsing(file_path1, file_path2)
    assert stylish(diff(file1, file2)) == unswer
