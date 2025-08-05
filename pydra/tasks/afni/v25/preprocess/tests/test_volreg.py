from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.preprocess.volreg import Volreg
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_volreg_1():
    task = Volreg()
    task.in_file = Nifti1.sample(seed=0)
    task.basefile = Nifti1.sample(seed=3)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_volreg_2():
    task = Volreg()
    task.in_file = Nifti1.sample(seed=0)
    task.zpad = 4
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_volreg_3():
    task = Volreg()
    task.in_file = Nifti1.sample(seed=0)
    task.basefile = Nifti1.sample(seed=3)
    task.oned_file = "dfile.r1.1D"
    task.verbose = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
