from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.utils.undump import Undump
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_undump_1():
    task = Undump()
    task.in_file = Nifti1.sample(seed=0)
    task.mask_file = File.sample(seed=2)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_undump_2():
    task = Undump()
    task.in_file = Nifti1.sample(seed=0)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
