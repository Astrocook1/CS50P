import pytest
from seasons import sing
import sys

def test_dateFormat():
    with pytest.raises(SystemExit):
        sing("November 10, 2025")
    assert sing("2025-11-10") == "Two hundred ten thousand, two hundred forty minutes"

def test_dateValidity():
    with pytest.raises(SystemExit):
        sing("2025-13-10")
    with pytest.raises(SystemExit):
        sing("2025-11-31")
    with pytest.raises(SystemExit):
        sing("20251120")
