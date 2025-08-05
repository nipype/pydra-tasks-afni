from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.re_ho import ReHo
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_reho_1():
    task = ReHo()
    task.in_file = Nifti1.sample(seed=0)
    task.mask_file = File.sample(seed=3)
    task.label_set = File.sample(seed=7)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_reho_2():
    task = ReHo()
    task.in_file = Nifti1.sample(seed=0)
    task.neighborhood = "vertices"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
