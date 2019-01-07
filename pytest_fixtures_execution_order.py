# -*- coding: cp1252 -*-
import pytest
import unittest


@pytest.fixture(scope='function')
def function_based_fixture(request):
    print("Setting Up of function scoped fixture")
    def fin():
        print("teardown of function scoped fixture")
    request.addfinalizer(fin)


@pytest.fixture(scope='module')
def module_based_fixture(request):
    print("Setting Up of module scoped fixture")

    def fin():
        print("teardown of module scoped fixture")
    request.addfinalizer(fin)    

@pytest.fixture(scope='session')
def session_based_fixture(request):
    print("Setting Up of session scoped fixture")

    def fin():
        print("teardown of session scoped fixture")
    request.addfinalizer(fin)

@pytest.fixture(scope='function')
def function_based_fixture111(request):
    print("Setting Up of function scoped fixture111")

    def fin():
        print("teardown of function scoped fixture111")
    request.addfinalizer(fin)

@pytest.fixture(scope='class')
def class_based_fixture(request):
    print("Setting Up of class scoped fixture")

    def fin():
        print("teardown of class scoped fixture")
    request.addfinalizer(fin) 

'''
################### 
##Combination1:::
###################    
def test_fucntion_scope(function_based_fixture):
    print "Hi Buddy you are in function scoped fixture"

def test_session_scope(session_based_fixture):
    print "Hi Buddy you are in session scoped fixture"    
    
def test_module_scope(module_based_fixture):
    print "Hi Buddy you are in module scoped fixture"

Output::

pytest_fixtures_execution_order.py::test_fucntion_scope Setting Up of function scoped fixture
Hi Buddy you are in function scoped fixture
PASSEDteardown of function scoped fixture

pytest_fixtures_execution_order.py::test_session_scope Setting Up of session scoped fixture
Hi Buddy you are in session scoped fixture
PASSED

pytest_fixtures_execution_order.py::test_module_scope Setting Up of module scoped fixture
Hi Buddy you are in module scoped fixture
PASSEDteardown of module scoped fixture
teardown of session scoped fixture
'''

'''
################### 
##Combination2:::
###################

def test_session_scope(session_based_fixture):
    print "Hi Buddy you are in session scoped fixture"

def test_fucntion_scope(function_based_fixture):
    print "Hi Buddy you are in function scoped fixture"
    
def test_module_scope(module_based_fixture):
    print "Hi Buddy you are in module scoped fixture"

OUTPUT::

pytest_fixtures_execution_order.py::test_session_scope Setting Up of session scoped fixture
Hi Buddy you are in session scoped fixture
PASSED
pytest_fixtures_execution_order.py::test_fucntion_scope Setting Up of function scoped fixture
Hi Buddy you are in function scoped fixture
PASSEDteardown of function scoped fixture

pytest_fixtures_execution_order.py::test_module_scope Setting Up of module scoped fixture
Hi Buddy you are in module scoped fixture
PASSEDteardown of module scoped fixture
teardown of session scoped fixture
'''
'''
################### 
##Combination3:::
###################

def test_module_scope(module_based_fixture):
    print "Hi Buddy you are in module scoped fixture"
    
def test_fucntion_scope(function_based_fixture):
    print "Hi Buddy you are in function scoped fixture"

def test_session_scope(session_based_fixture):
    print "Hi Buddy you are in session scoped fixture"    

Output::
pytest_fixtures_execution_order.py::test_module_scope Setting Up of module scoped fixture
Hi Buddy you are in module scoped fixture
PASSED
pytest_fixtures_execution_order.py::test_fucntion_scope Setting Up of function scoped fixture
Hi Buddy you are in function scoped fixture
PASSEDteardown of function scoped fixture

pytest_fixtures_execution_order.py::test_session_scope Setting Up of session scoped fixture
Hi Buddy you are in session scoped fixture
PASSEDteardown of module scoped fixture
teardown of session scoped fixture
'''

'''
def pytest_addoption(parser):
    """Implement hook that defines custom command line options to be passed to pytest."""
    diabetes_disease_group = parser.getgroup('Diabetes Diseases Type User Options')
    #have to optimize the default value of first option in group
    diabetes_disease_group.addoption(
        "--bulk", action="store", default="all",help="Use this option to bulk test execution for all users"
    )
    #nargs='*' - allowed additional arguments will be accepted, and any other additional
    # arguments will be rejected with an appropriately specific error message.

    diabetes_disease_group.addoption(
        "--user", default='type2_diabetes', const='type2_diabetes',action="store", nargs='?',choices=['type2_diabetes','type1_diabetes','prediabetes_and_alcoholism'],
                help="Use this option to select the users to cover all test scenarios"
    )

@pytest.fixture(name='user_input')
def user_test(request):
    return request.config.getoption("--user")
    #return request.config.getoption("--user")

def test_dummy(user_input):
    print "Hi Hello"
'''

@pytest.fixture(scope='session')
def first_fixture(request):
    dict_to = {'userinfo':{"type2_diabetes":{'username': 'JaneDoe-EMAUser','user_model_name': 'JaneDoeEMAUserModel','session_id': 'JaneDoeEMAUserSession'}}}
    def fin():
        print "Teardown of first_fixture()"
    request.addfinalizer(fin)
    return dict_to

@pytest.fixture()
def second_fixture(first_fixture):
    print " \n using the first fixture info for tests"
    print first_fixture['userinfo']


def test_fisture_above(second_fixture):
    print "Im executing the second fixture to get first fixture dict values"

