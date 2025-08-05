from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.preprocess.bandpass import Bandpass
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_bandpass_1():
    task = Bandpass()
    task.in_file = Nifti1.sample(seed=0)
    task.mask = File.sample(seed=4)
    task.orthogonalize_file = [File.sample(seed=6)]
    task.orthogonalize_dset = File.sample(seed=7)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_bandpass_2():
    task = Bandpass()
    task.in_file = Nifti1.sample(seed=0)
    task.lowpass = 0.1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
