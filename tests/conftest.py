#Refer the below mentioned link for goog docstring implementation
# https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

import pytest
import logging
import time
import json


#https://stackoverflow.com/questions/18011902/py-test-pass-a-parameter-to-a-fixture-function
#https://github.com/pytest-dev/pytest/issues/1694
#https://alysivji.github.io/pytest-fixures-with-function-arguments.html
#https://realpython.com/python-cli-testing/
#https://medium.com/ideas-at-igenius/fixtures-and-parameters-testing-code-with-pytest-d8603abb390a
#https://stackoverflow.com/questions/38795482/passing-a-command-line-argument-to-a-py-test-fixture-as-a-parameter
#https://stackoverflow.com/questions/46368468/run-a-test-with-two-different-pytest-fixtures
#http://pythontesting.net/framework/pytest/pytest-fixtures-nuts-bolts/#bare
'''
# Currently there's no way to pass parameters to fixtures from within a test function or other fixtures, 
  by that point the fixture function has already been called.

# Usually the solution to this is to make a fixture return an object or function which you can call from within a 
  test function and does what you need.

@pytest.fixture(scope='session')
def fixture_1(request):
    def do_it(param):
        # do something
    return do_it
'''

'''

Fixture functions can be parametrized in which case they will be called multiple times, each time executing the set of 
dependent tests, i. e. the tests that depend on this fixture. Test functions do usually not need to be aware of their 
re-running. Fixture parametrization helps to write exhaustive functional tests for components which themselves can be 
configured in multiple ways.

@pytest.fixture(params=range(1, 11, 2))
def odd(request):
    return request.param
@pytest.fixture(params=range(0, 10, 2))
def even(request):
    return request.param
def test_sum_odd_even_returns_odd(odd, even):
    assert is_odd(odd + even)

'''




#fixture with passing arguments
@pytest.fixture()
def concat_name(request):
    def foo(first_name,last_name):
        return '{},{}'.format(first_name,last_name)
    return foo

def test_concat(concat_name):
    concat_nam = concat_name("Venkatesh","Krishnan")
    #print concat_nam
    assert concat_nam == "Venkatesh,Krishnan"


@pytest.fixture()
def provide_post_id():
    return 3

@pytest.fixture(name="time_request")
def fix_time_request():
    t0= time.time()
    yield
    t1 = time.time()
    logging.info("Test took %s seconds", t1 - t0)

@pytest.fixture
def json_loader():
    """Loads data from JSON file"""

    def _loader(filename):
        with open(filename, 'r') as f:
            print(filename)
            data = json.load(f)
        return data

    return _loader

@pytest.fixture()
def custom_argument_passer():
    def _foo(*args, **kwargs):
        return (args, kwargs)

    return _foo

'''
def test_example(argument_printer):
    first_case = argument_printer('a', 'b')
    assert first_case == (('a', 'b'), {})
'''

@pytest.fixture(name="json_val")
def get_json_val():
    return "abc123"

