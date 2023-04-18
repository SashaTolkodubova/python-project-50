from gendiff.formatters.to_json import to_json
from gendiff.gendiff.gendiff import diff
from gendiff.scripts.Parsing import parsing
import json


def test_to_json():
    file1_path = 'tests/fixtures/file1.json'
    file2_path = 'tests/fixtures/file2.json'
    file1, file2 = parsing(file1_path, file2_path)
    answer_path = 'tests/fixtures/json_unswer.json'
    test_answer = to_json(diff(file1, file2))
    with open(answer_path, 'r') as file1_json:
        answer = json.load(file1_json)
    test_answer = json.loads(test_answer)
    assert test_answer == answer
