from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.utils.a_boverlap import ABoverlap
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_aboverlap_1():
    task = ABoverlap()
    task.in_file_a = Nifti1.sample(seed=0)
    task.in_file_b = File.sample(seed=1)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_aboverlap_2():
    task = ABoverlap()
    task.in_file_a = Nifti1.sample(seed=0)
    task.out_file = "out.mask_ae_overlap.txt"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
