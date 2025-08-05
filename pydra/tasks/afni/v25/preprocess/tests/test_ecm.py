from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.preprocess.ecm import ECM
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_ecm_1():
    task = ECM()
    task.in_file = Nifti1.sample(seed=0)
    task.mask = File.sample(seed=9)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_ecm_2():
    task = ECM()
    task.in_file = Nifti1.sample(seed=0)
    task.sparsity = 0.1  # keep top 0.1% of connections
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
