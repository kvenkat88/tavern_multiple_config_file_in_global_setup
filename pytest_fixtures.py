# -*- coding: cp1252 -*-
import pytest
import unittest

## http://pythontesting.net/framework/pytest/pytest-fixtures-nuts-bolts/#bare

############################################################################
#Returning some data from a fixture.

@pytest.fixture()
def some_data():
    data = {'foo':1, 'bar':2}
    return data

def test_foo(some_data):
    assert some_data['foo'] == 1

############################################################################
#Returning some data from a fixture and fixture have a name and then use it in test
@pytest.fixture(name='demo')
def some_data_to_send():
    data = {'foo':1, 'bar':2, 'bar': 3}
    return data

@pytest.mark.usefixtures(name='demo')
def test_foo1(demo):
    assert demo['foo'] == 1

############################################################################

#Retrieving a data by using "usingfixtures" option available in pytest fixture functionality
# The next example puts the fixture function into a separate conftest.py file so that tests from
# multiple test modules in the directory can access the fixture function

### Not fully implemented

@pytest.fixture(name='use_fixtures',scope='module')
def pytest_using_fixtures_option():
    data = {'zoo':1, 'car':2, 'bat': 3}
    return data

@pytest.mark.usefixtures(name="use_fixtures")
def test_retriev_data(use_fixtures):
    print use_fixtures['zoo']
    return use_fixtures['zoo']

############################################################################
#Sample Returning a database object
@pytest.fixture()
def cheese_db(request):
    print('\n[setup] cheese_db, connect to db')
    # code to connect to your db
    a_dictionary_for_now = {'Brie': 'No.', 'Camenbert': 'Ah! We have Camenbert, yessir.'}
    def fin():
        print('\n[teardown] cheese_db finalizer, disconnect from db')
    request.addfinalizer(fin)
    return a_dictionary_for_now

def test_cheese_database1(cheese_db):
    for variety in cheese_db.keys():
        print "%" * 30
        print('%s : %s' % (variety, cheese_db[variety]))
        print "%" * 30

def test_cheese_database(cheese_db):
    for variety in cheese_db.keys():
        print('%s : %s' % (variety, cheese_db[variety]))
    
def test_brie(cheese_db):
    print('in test_brie()')
    assert cheese_db['Brie'] == 'No.' 
 
def test_camenbert(cheese_db):
    print('in test_camenbert()')
    assert cheese_db['Camenbert'] != 'No.'


######################################Scope of PyTest Fixture#################################################
#Function - Run once per test # default scope
#Class - Run once per Class of tests (Second highest)
#module - Run once per module (Third)
#session - Run once per session (last)
    
############################################################################

#Pytest Fixtures with passing params as parameters
@pytest.fixture(params=[1,2,3,4])
def test_data(request):
    return request.param

def test_not_2(test_data):
    print('test_data: %s' % test_data)
    assert test_data != 2
############################################################################
#Pytest RealWorld Example
'''
from markdown_adapter import run_markdown

@pytest.fixture(params=[
    ('regular text'   , 'regular text</p>'),
    ('*em tags*'      , '<p><em>em tags</em></p>'),
    ('**strong tags**', '<p><strong>strong tags</strong></p>')
    ])

def test_data1(request):
    return request.param

def test_markdown(test_data1):
    (the_input, the_expected_output) = test_data
    the_output = run_markdown(the_input)
    print('\ntest_markdown():')
    print('  input   : %s' % the_input)
    print('  output  : %s' % the_output)
    print('  expected: %s' % the_expected_output)
    assert the_output == the_expected_output'''

'''
@pytest.fixture(scope="module", autouse=True)
def mod_header(request):
    print('\n-----------------')
    print('user        : %s' % getpass.getuser())
    print('module      : %s' % request.module.__name__)
    print('-----------------')
 
@pytest.fixture(scope="function", autouse=True)
def func_header(request):
    print('\n-----------------')
    print('function    : %s' % request.function.__name__)
    print('time        : %s' % time.asctime())
    print('-----------------')
 
def test_one():
    print('in test_one()')
 
def test_two():
    print('in test_two()')'''

#######################################################################################################
## Working with Multiple fixtures

@pytest.fixture(scope='module')
def foo(request):
    print('\nfoo setup - module fixture')
    def fin():
        print('foo teardown - module fixture')
    request.addfinalizer(fin)

@pytest.fixture()
def bar(request):
    print('bar setup - function fixture')
    def fin():
        print('bar teardown - function fixture')
    request.addfinalizer(fin)
 
@pytest.fixture()
def baz(request):
    print('baz setup - function fixture')
    def fin():
        print('baz teardown - function fixture')
    request.addfinalizer(fin)

def test_one(foo, bar, baz):
    print('in test_one()')
 
def test_two(foo, bar, baz):
    print('in test_two()')
#############################################################################################################
#Defining a fixture with pytest.yield_fixture option

@pytest.yield_fixture(scope='module')
def yogurt_db():
    print('\n[setup] yogurt_db, connect to db')
    a_dictionary_for_now = {'Brie': 'No.', 'Camenbert': 'Ah! We have Camenbert, yessir.'}
    yield a_dictionary_for_now
    print('\n[teardown] cheese_db finalizer, disconnect from db')

def test_brie(yogurt_db):
    print('in test_brie()')
    assert yogurt_db['Brie'] == 'No.' 
 
def test_camenbert(yogurt_db):
    print('in test_camenbert()')
    assert yogurt_db['Camenbert'] != 'No.'
#############################################################################################################
##Simple example of session scope fixtures
'''
I’ve got 4 files:

conftest.py
    2 fixtures
    my_own_session_run_at_beginning, an autouse fixture with session scope
    some_resource, a normal non-autouse fixture with session scope
    
test_alpha.py
    2 simple test functions
    test_alpha_1, has no named fixtures
    test_alpha_2, has one named fixture, some_resource
    
test_beta.py
    similar to test_alpha.py, but with unittest based tests
    test_gamma.py
    similar to test_alpha.py, but with class based tests
'''

@pytest.fixture(scope='session',autouse=True)
def my_own_session_run_at_beginning(request):
    print('\nIn my_own_session_run_at_beginning()')

    def my_own_session_run_at_end():
            print('In my_own_session_run_at_end()')
    request.addfinalizer(my_own_session_run_at_end)

@pytest.fixture(scope="session")
def some_resource(request):
    print('\nIn some_resource()')

    def some_resource_fin():
            print('\nIn some_resource_fin()')
    request.addfinalizer(some_resource_fin)
    
def test_alpha_1():
    print('\nIn test_alpha_1()')
 
def test_alpha_2(some_resource):
    print('\nIn test_alpha_2()')

#############################################################################################################
    
class BetaTest(unittest.TestCase):
    def test_unit_beta_1(self):
        print('\nIn test_unit_beta_1()')

    @pytest.mark.usefixtures('some_resource')    
    def test_unit_beta_2(self):
        print('\nIn test_unit_beta_2()')

#############################################################################################################
        
class TestGamma:
    def test_gamma_1(self):
        print('\nIn test_gamma_1()')
 
    def test_gamma_2(self, some_resource):
        print('\nIn test_gamma_2()')
        
#############################################################################################################
##Mixing function, module, and session scope    

# a function scope fixture ‘resource_c’
# that uses a module scoped fixture ‘fixture_b’
# that uses a session scoped fixture ‘fixture_a’
# This all works fine.
# Also in this example, I’ve added a few autouse fixtures just for fun.
'''
@pytest.fixture(scope="session")
def resource_a(request):
    print('In resource_a()')
 
    def resource_a_fin():
            print('\nIn resource_a_fin()')
    request.addfinalizer(resource_a_fin)
 
@pytest.fixture(scope="module")
def resource_b(request, resource_a):
    print('In resource_b()')
 
    def resource_b_fin():
            print('\nIn resource_b_fin()')
    request.addfinalizer(resource_b_fin)
 
@pytest.fixture(scope="function")
def resource_c(request, resource_b):
    print('In resource_c()')
 
    def resource_c_fin():
            print('\nIn resource_c_fin()')
    request.addfinalizer(resource_c_fin)'''

#############################################################################################################
#Try this in separate file for better results
# these are just some fun dividiers to make the output pretty
# completely unnecessary, I was just playing with autouse fixtures
'''
@pytest.fixture(scope="function", autouse=True)
def divider_function(request):
    print('\n        --- function %s() start ---' % request.function.__name__)
    def fin():
            print('        --- function %s() done ---' % request.function.__name__)
    request.addfinalizer(fin)
 
@pytest.fixture(scope="module", autouse=True)
def divider_module(request):
    print('\n    ------- module %s start ---------' % request.module.__name__)
    def fin():
            print('    ------- module %s done ---------' % request.module.__name__)
    request.addfinalizer(fin)
 
@pytest.fixture(scope="session", autouse=True)
def divider_session(request):
    print('\n----------- session start ---------------')
    def fin():
            print('----------- session done ---------------')
    request.addfinalizer(fin)

def test_one11(resource_c):
    print('In test_one()')
 
def test_two11(resource_c):
    print('\nIn test_two()')


def test_three11(resource_c):
    print('\nIn test_three()')
 
def test_four11(resource_c):
    print('\nIn test_four()')
'''
#############################################################################################################
#https://docs.pytest.org/en/latest/example/special.html

'''
import smtplib
import pytest


@pytest.fixture(scope="module")
def smtp_connection(request):
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

    def fin():
        print("teardown smtp_connection")
        smtp_connection.close()

    request.addfinalizer(fin)
    return smtp_connection  # provide the fixture value

'''




















