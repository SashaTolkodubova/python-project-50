from gendiff.scripts.gendiff import generate_diff
from tests.fixtures.gendiff_unswer import unswer
import json

def test_generate_diff():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'

    assert  generate_diff(file_path1, file_path2) == unswer
