import pytest
from app import soma


@pytest.mark.parametrize('a,b,expected', [(5, 4, 9)])
def test_soma(a,b, expected):
    assert soma(a,b) == expected
