from fileformats.generic import Directory
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.utils.to_3d import To3D
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_to3d_1():
    task = To3D()
    task.in_folder = Directory.sample(seed=1)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_to3d_2():
    task = To3D()
    task.out_file = "dicomdir.nii"
    task.datatype = "float"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
