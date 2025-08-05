import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.cat_matvec import CatMatvec
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_catmatvec_1():
    task = CatMatvec()
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_catmatvec_2():
    task = CatMatvec()
    task.in_file = [("structural.BRIK::WARP_DATA", "I")]
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
