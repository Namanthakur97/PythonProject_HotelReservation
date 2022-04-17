# test_with_pytest.py
import pytest
from src.Hotel import*
obj = Home()
def test_Home():
    assert obj.Home()==0
    
def test_Booking():
    assert obj.Booking()==0

def test_ROOMsinfo():
    assert obj.ROOMsinfo()==0

def test_Payment():
    assert obj.Payment()==5000

def test_record():
    assert obj.record()==0