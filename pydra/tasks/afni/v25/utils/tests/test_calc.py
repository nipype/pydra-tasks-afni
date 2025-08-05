from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.calc import Calc
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_calc_1():
    task = Calc()
    task.in_file_a = Nifti1.sample(seed=0)
    task.in_file_b = File.sample(seed=1)
    task.in_file_c = File.sample(seed=2)
    task.other = File.sample(seed=9)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_calc_2():
    task = Calc()
    task.in_file_a = Nifti1.sample(seed=0)
    task.expr = "a*b"
    task.outputtype = "NIFTI"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_calc_3():
    task = Calc()
    task.in_file_a = Nifti1.sample(seed=0)
    task.out_file = "rm.epi.all1"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
