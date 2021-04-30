import pytest
from sample import determinant

def test_matrice_determinant():
    assert determinant([[6,1,1], [4, -2, 5], [2,8,7]]) == pytest.approx(-306.0)