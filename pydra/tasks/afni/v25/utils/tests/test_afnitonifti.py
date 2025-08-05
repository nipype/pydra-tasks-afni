from fileformats.medimage_afni import ThreeD
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.afn_ito_nifti import AFNItoNIFTI
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_afnitonifti_1():
    task = AFNItoNIFTI()
    task.in_file = ThreeD.sample(seed=0)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_afnitonifti_2():
    task = AFNItoNIFTI()
    task.in_file = ThreeD.sample(seed=0)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
