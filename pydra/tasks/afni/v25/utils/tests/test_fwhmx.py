from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.fwh_mx import FWHMx
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_fwhmx_1():
    task = FWHMx()
    task.in_file = Nifti1.sample(seed=0)
    task.mask = File.sample(seed=3)
    task.automask = False
    task.detrend = False
    task.acf = False
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_fwhmx_2():
    task = FWHMx()
    task.in_file = Nifti1.sample(seed=0)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
