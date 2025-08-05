from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.utils.z_cut_up import ZCutUp
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_zcutup_1():
    task = ZCutUp()
    task.in_file = Nifti1.sample(seed=0)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_zcutup_2():
    task = ZCutUp()
    task.in_file = Nifti1.sample(seed=0)
    task.keep = "0 10"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
