import json

import pytest

from binary_number import app

def test_is_binary_number():
    assert app.is_binary_number(3) == '11'