from fileformats.generic import File
from fileformats.medimage import NiftiGz
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.nwarp_adjust import NwarpAdjust
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_nwarpadjust_1():
    task = NwarpAdjust()
    task.warps = [NiftiGz.sample(seed=0)]
    task.in_files = [File.sample(seed=1)]
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_nwarpadjust_2():
    task = NwarpAdjust()
    task.warps = [NiftiGz.sample(seed=0)]
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
