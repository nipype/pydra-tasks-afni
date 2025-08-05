from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.preprocess.outlier_count import OutlierCount
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_outliercount_1():
    task = OutlierCount()
    task.in_file = Nifti1.sample(seed=0)
    task.mask = File.sample(seed=1)
    task.qthr = 0.001
    task.autoclip = False
    task.automask = False
    task.fraction = False
    task.interval = False
    task.save_outliers = False
    task.legendre = False
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_outliercount_2():
    task = OutlierCount()
    task.in_file = Nifti1.sample(seed=0)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
