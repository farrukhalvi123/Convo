import os
import pytest
from behave.__main__ import main as behave_main

# Define the parameterization of the browser to be run for each test
@pytest.mark.parametrize("browser_name", ["chrome", "firefox"])
def test_parallel_browsers(browser_name):
    """
    This function triggers Behave tests with a specified browser.
    We use pytest's parameterization to run the tests on both Firefox and Chrome in parallel.
    """
    # Set the environment variable for the current browser_name
    os.environ['BROWSER_NAME'] = browser_name

    # Run Behave tests (this triggers the actual feature files execution)
    behave_main()
