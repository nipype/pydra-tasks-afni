from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.preprocess.fourier import Fourier
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_fourier_1():
    task = Fourier()
    task.in_file = Nifti1.sample(seed=0)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_fourier_2():
    task = Fourier()
    task.in_file = Nifti1.sample(seed=0)
    task.highpass = 0.005
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
