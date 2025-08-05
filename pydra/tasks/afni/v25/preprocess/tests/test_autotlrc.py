from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.preprocess.auto_tlrc import AutoTLRC
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_autotlrc_1():
    task = AutoTLRC()
    task.in_file = Nifti1.sample(seed=1)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_autotlrc_2():
    task = AutoTLRC()
    task.in_file = Nifti1.sample(seed=1)
    task.base = "TT_N27+tlrc"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
