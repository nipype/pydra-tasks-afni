from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.preprocess.roi_stats import ROIStats
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_roistats_1():
    task = ROIStats()
    task.in_file = Nifti1.sample(seed=0)
    task.mask = File.sample(seed=1)
    task.mask_file = File.sample(seed=2)
    task.roisel = File.sample(seed=6)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_roistats_2():
    task = ROIStats()
    task.in_file = Nifti1.sample(seed=0)
    task.stat = ["mean", "median", "voxels"]
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
