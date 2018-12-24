#Refer the below mentioned link for goog docstring implementation
# https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

import pytest
import logging
import time

@pytest.mark.welcome
def test_send_welcome():
    yield "Welcome"

@pytest.fixture(name="time_request")
def fix_time_request():
    t0= time.time()
    yield
    t1 = time.time()
    logging.info("Test took %s seconds", t1 - t0)