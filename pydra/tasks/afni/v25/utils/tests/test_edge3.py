from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.edge_3 import Edge3
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_edge3_1():
    task = Edge3()
    task.in_file = Nifti1.sample(seed=0)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_edge3_2():
    task = Edge3()
    task.in_file = Nifti1.sample(seed=0)
    task.datum = "byte"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
