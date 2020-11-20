import pytest
import cowsay
import json


def test_basic(capsys, tmp_path):
    print(tmp_path)
    cowsay.cow("hello")
    captured = capsys.readouterr()
    # print(captured.out)
    assert 1 == 1


def test_tmp_path(tmp_path):
    print(f'tmp_path: {tmp_path}')
