from sievetools import *
import pytest

def test_slow_inits():
    assert sieve_slow(10) == [2, 3, 5, 7]

def test_slow_edge():
    assert sieve_slow(1) == []

def test_negative_numbers():
    with pytest.raises(ValueError):
        sieve_slow(-3)

def test_nonintegers():
    with pytest.raises(ValueError):
        sieve_slow(-0.5)

def test_getprimes_init():
    assert get_primes(10, 'slow') == get_primes(10, 'fast')

def test_getprimes_init():
    assert get_primes(10, 'slow') == [2, 3, 5, 7]

def test_getprimes_neg():
    with pytest.raises(ValueError):
        get_primes(-3, 'slow')

def test_bad_method():
    with pytest.raises(NotImplementedError):
        get_primes(-3, 'bad_input')