import pytest
from pathlib import Path, PosixPath
from collections import namedtuple
import uuid


def test_str_from_bytes():
    assert str(b'abc', encoding='utf-8') == 'abc'


def test_pathlib():
    p = Path('.')
    print(f'p.absolute: {p.absolute()}')
    assert isinstance(p.absolute(), PosixPath)


def test_dict():
    user = {'id': 1, 'email': 'first.last@example.com'}
    assert len(user.keys()) == 2
    assert len(user.values()) == 2
    assert user.get('id') == 1
    assert user.get('email') == 'first.last@example.com'


def test_namedtuple():
    User = namedtuple('User', [
        'Id',
        'Email',
        'FirstName',
        'LastName'
    ])
    user1 = User(
        Id=1,
        Email='first.last@example.com',
        FirstName='John',
        LastName='Doe'
    )
    assert user1.Id == 1
    assert user1.Email == 'first.last@example.com'

    user1_expected_str = "User(Id=1, Email='first.last@example.com', FirstName='John', LastName='Doe')"
    user1_actual_str = str(user1)
    assert user1_actual_str == user1_expected_str


def test_uuid():
    id = uuid.uuid4()
    id_str = str(id)
    assert len(id_str) == 36
