import pytest

def fizzBuzz(value):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    if isMultiple(value, 5):
        if isMultiple(value, 3):
            return "FizzBuzz"
        return "Buzz"
    return str(value)

def isMultiple(value, mod):
    return (value % mod) ==0

def test_returns1WithPassedIn():
    checkFizzBuzz(1, "1")
def test_returns2WithPassedIn():
    checkFizzBuzz(2, "2")
#create a utility function that does the same thing as the previous 2
def checkFizzBuzz(value, expectedRetVal):
    retVal=fizzBuzz(value)
    assert retVal==expectedRetVal


def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, "Fizz")
    
def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(5, "Buzz")
    
def test_returnsFizzWith6PassedIn():
    checkFizzBuzz(6, "Fizz")
    
def test_returnsWith10PassedIn():
    checkFizzBuzz(10, "Buzz")
    
def test_returnsFizzBuzzwith15PassedIn():
    checkFizzBuzz(15, "FizzBuzz")