from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.utils.mask_tool import MaskTool
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_masktool_1():
    task = MaskTool()
    task.in_file = [Nifti1.sample(seed=0)]
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_masktool_2():
    task = MaskTool()
    task.in_file = [Nifti1.sample(seed=0)]
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
