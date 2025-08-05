from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.preprocess.means import Means
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_means_1():
    task = Means()
    task.in_file_a = Nifti1.sample(seed=0)
    task.in_file_b = File.sample(seed=1)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_means_2():
    task = Means()
    task.in_file_a = Nifti1.sample(seed=0)
    task.out_file = "output.nii"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_means_3():
    task = Means()
    task.in_file_a = Nifti1.sample(seed=0)
    task.datum = "short"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
