from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.preprocess.maskave import Maskave
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_maskave_1():
    task = Maskave()
    task.in_file = Nifti1.sample(seed=0)
    task.mask = File.sample(seed=2)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_maskave_2():
    task = Maskave()
    task.in_file = Nifti1.sample(seed=0)
    task.quiet = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
