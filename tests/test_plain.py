from gendiff.formatters.plain import plain
from gendiff.scripts.gendiff import diff
from gendiff.scripts.Parsing import parsing
from fixtures.plain_unswer import unswer


def test_plain():
    file1_path = '/Users/konstantin/python2023/' \
                 'Hexlet/python-project-50/tests/fixtures/file1.json'
    file2_path = '/Users/konstantin/python2023/' \
                 'Hexlet/python-project-50/tests/fixtures/file2.json'
    file1, file2 = parsing(file1_path, file2_path)
    assert plain(diff(file1, file2)) == unswer
