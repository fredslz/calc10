import pytest
from app import soma


@pytest.mark.parametrize('a,b,expected', [(5, 4, 9), (-5, 4, -1), (-5, -4, -9), (-5.4, -4.2, -9.6)])
def test_soma(a,b, expected):
    assert soma(a,b) == expected
