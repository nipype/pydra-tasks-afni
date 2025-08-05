from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.preprocess.warp import Warp
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_warp_1():
    task = Warp()
    task.in_file = Nifti1.sample(seed=0)
    task.matparent = File.sample(seed=4)
    task.oblique_parent = File.sample(seed=5)
    task.gridset = File.sample(seed=8)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_warp_2():
    task = Warp()
    task.in_file = Nifti1.sample(seed=0)
    task.out_file = "trans.nii.gz"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_warp_3():
    task = Warp()
    task.in_file = Nifti1.sample(seed=0)
    task.out_file = "trans.nii.gz"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
