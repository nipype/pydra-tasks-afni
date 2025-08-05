from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.zeropad import Zeropad
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_zeropad_1():
    task = Zeropad()
    task.in_files = Nifti1.sample(seed=0)
    task.master = File.sample(seed=13)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_zeropad_2():
    task = Zeropad()
    task.in_files = Nifti1.sample(seed=0)
    task.I = 10
    task.A = 10
    task.R = 10
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
