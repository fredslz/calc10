import pytest
from app import soma


@pytest.mark.parametrize('a,b,expected', [(5, 4, 9), (-5, 4, -1), (-5, -4, -9), (7.5, 5.4,12.9), (-1.0, -2.0,-3.0)])
def test_soma(a,b, expected):
    assert soma(a,b) == expected
