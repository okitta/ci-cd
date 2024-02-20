# tests/test_fizzbuzz.py

from ..main import fizzbuzz

def test_fizzbuzz_divisible_by_3():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"

def test_fizzbuzz_divisible_by_5():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"

def test_fizzbuzz_divisible_by_3_and_5():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"

def test_fizzbuzz_not_divisible_by_3_or_5():
    assert fizzbuzz(2) == 2
    assert fizzbuzz(7) == 7
    assert fizzbuzz(11) == 11
