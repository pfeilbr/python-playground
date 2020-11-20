import pytest
import requests
import json


def test_basic():
    r = requests.get('https://api.github.com/events')
    # print(json.dumps(r.json(), indent=2, sort_keys=True))

    assert isinstance(r.url, str)
    assert isinstance(r.text, str)
    assert isinstance(r.json(), list)
    assert isinstance(r.json()[0], dict)
    assert 1 == 1
