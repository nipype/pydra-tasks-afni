import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.bucket import Bucket
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_bucket_1():
    task = Bucket()
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_bucket_2():
    task = Bucket()
    task.in_file = [("functional.nii", "{2..$}"), ("functional.nii", "{1}")]
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
