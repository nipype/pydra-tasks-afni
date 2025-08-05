import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.t_cat_sub_brick import TCatSubBrick
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_tcatsubbrick_1():
    task = TCatSubBrick()
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tcatsubbrick_2():
    task = TCatSubBrick()
    task.in_files = [("functional.nii", "'{2..$}'"), ("functional2.nii", "'{2..$}'")]
    task.rlt = "+"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
