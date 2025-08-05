from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.preprocess.degree_centrality import DegreeCentrality
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_degreecentrality_1():
    task = DegreeCentrality()
    task.in_file = Nifti1.sample(seed=0)
    task.mask = File.sample(seed=3)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_degreecentrality_2():
    task = DegreeCentrality()
    task.in_file = Nifti1.sample(seed=0)
    task.sparsity = 1  # keep the top one percent of connections
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
