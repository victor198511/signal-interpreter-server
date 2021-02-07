import os
from subprocess import call
from invoke import task

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.join(CURR_DIR, "signal_interpreter_server")


@task
def style(_):
    call(f"pycodestyle {SRC_DIR} --ignore=E501", shell=True)


@task
def lint(_):
    call(f"pylint {SRC_DIR}", shell=True)
