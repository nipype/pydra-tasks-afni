from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.t_cat import TCat
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_tcat_1():
    task = TCat()
    task.in_files = [Nifti1.sample(seed=0)]
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tcat_2():
    task = TCat()
    task.in_files = [Nifti1.sample(seed=0)]
    task.rlt = "+"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
