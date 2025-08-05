from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.brick_stat import BrickStat
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_brickstat_1():
    task = BrickStat()
    task.in_file = Nifti1.sample(seed=0)
    task.mask = File.sample(seed=1)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_brickstat_2():
    task = BrickStat()
    task.in_file = Nifti1.sample(seed=0)
    task.min = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
