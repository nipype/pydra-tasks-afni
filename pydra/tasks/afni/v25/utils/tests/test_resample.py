from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.resample import Resample
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_resample_1():
    task = Resample()
    task.in_file = Nifti1.sample(seed=0)
    task.master = File.sample(seed=5)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_resample_2():
    task = Resample()
    task.in_file = Nifti1.sample(seed=0)
    task.outputtype = "NIFTI"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
