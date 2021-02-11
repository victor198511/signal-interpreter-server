import os
from subprocess import call
from invoke import task

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.join(CURR_DIR, "signal_interpreter_server")
UNIT_TEST_DIR = os.path.join(CURR_DIR, "tests", "unit")
INTEGRATION_TEST_DIR = os.path.join(CURR_DIR, "tests", "integration")
COV_PATH = os.path.join(CURR_DIR, ".coveragerc")


@task
def style(_):
    call(f"pycodestyle {SRC_DIR} --ignore=E501", shell=True)


@task
def lint(_):
    call(f"pylint {SRC_DIR}", shell=True)


@task
def unit_test(_):
    cmd = f"pytest {UNIT_TEST_DIR} --cov {SRC_DIR} --cov-config={COV_PATH}"
    call(cmd, shell=True)


@task
def test_application(_):
    call(f"pytest {INTEGRATION_TEST_DIR}", shell=True)