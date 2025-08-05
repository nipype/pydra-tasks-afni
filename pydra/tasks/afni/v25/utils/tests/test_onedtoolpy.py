from fileformats.generic import File
from fileformats.medimage_afni import OneD
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.utils.one_d_tool_py import OneDToolPy
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_onedtoolpy_1():
    task = OneDToolPy()
    task.in_file = OneD.sample(seed=0)
    task.show_cormat_warnings = File.sample(seed=9)
    task.py27_path = "python2"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_onedtoolpy_2():
    task = OneDToolPy()
    task.in_file = OneD.sample(seed=0)
    task.demean = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
