from fileformats.generic import File
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.utils.cat import Cat
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_cat_1():
    task = Cat()
    task.in_files = [File.sample(seed=0)]
    task.out_file = "catout.1d"
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_cat_2():
    task = Cat()
    task.out_file = "catout.1d"
    task.sel = "'[0,2]'"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
