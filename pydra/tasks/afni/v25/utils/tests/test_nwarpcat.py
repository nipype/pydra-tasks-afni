import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.utils.nwarp_cat import NwarpCat
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_nwarpcat_1():
    task = NwarpCat()
    task.interp = "wsinc5"
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_nwarpcat_2():
    task = NwarpCat()
    task.in_files = ["Q25_warp+tlrc.HEAD", ("IDENT", "structural.nii")]
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
