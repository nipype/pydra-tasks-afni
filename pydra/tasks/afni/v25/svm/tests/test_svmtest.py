from fileformats.generic import File
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.svm.svm_test import SVMTest
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_svmtest_1():
    task = SVMTest()
    task.in_file = File.sample(seed=1)
    task.testlabels = File.sample(seed=3)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
