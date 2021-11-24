import json

import cowsay


def test_basic(capsys):
    cowsay.cow("hello")
    captured = capsys.readouterr()
    assert isinstance(captured.out, str)


def test_tmp_path(tmp_path):
    print(f'tmp_path: {tmp_path}')
    assert True, True
