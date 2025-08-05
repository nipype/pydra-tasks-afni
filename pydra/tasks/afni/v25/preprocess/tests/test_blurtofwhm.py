from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.preprocess.blur_to_fwhm import BlurToFWHM
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_blurtofwhm_1():
    task = BlurToFWHM()
    task.in_file = Nifti1.sample(seed=0)
    task.blurmaster = File.sample(seed=4)
    task.mask = File.sample(seed=5)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_blurtofwhm_2():
    task = BlurToFWHM()
    task.in_file = Nifti1.sample(seed=0)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
