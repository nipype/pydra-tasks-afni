from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.preprocess.lfcd import LFCD
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_lfcd_1():
    task = LFCD()
    task.in_file = Nifti1.sample(seed=0)
    task.mask = File.sample(seed=1)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_lfcd_2():
    task = LFCD()
    task.in_file = Nifti1.sample(seed=0)
    task.thresh = 0.8  # keep all connections with corr >= 0.8
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
