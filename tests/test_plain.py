from gendiff.formatters.plain import plain
from gendiff.gendiff.gendiff import diff
from gendiff.scripts.Parsing import parsing
from tests.fixtures.plain_unswer import unswer


def test_plain():
    file1_path = 'tests/fixtures/file1.json'
    file2_path = 'tests/fixtures/file2.json'
    file1, file2 = parsing(file1_path, file2_path)
    assert plain(diff(file1, file2)) == unswer
