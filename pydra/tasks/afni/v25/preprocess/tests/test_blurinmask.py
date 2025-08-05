from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.preprocess.blur_in_mask import BlurInMask
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_blurinmask_1():
    task = BlurInMask()
    task.in_file = Nifti1.sample(seed=0)
    task.mask = File.sample(seed=2)
    task.multimask = File.sample(seed=3)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_blurinmask_2():
    task = BlurInMask()
    task.in_file = Nifti1.sample(seed=0)
    task.fwhm = 5.0
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
