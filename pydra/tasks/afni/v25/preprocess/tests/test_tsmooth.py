from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.preprocess.t_smooth import TSmooth
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_tsmooth_1():
    task = TSmooth()
    task.in_file = Nifti1.sample(seed=0)
    task.custom = File.sample(seed=9)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tsmooth_2():
    task = TSmooth()
    task.in_file = Nifti1.sample(seed=0)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
