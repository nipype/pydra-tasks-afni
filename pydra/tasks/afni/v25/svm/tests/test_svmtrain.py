from fileformats.generic import File
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.svm.svm_train import SVMTrain
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_svmtrain_1():
    task = SVMTrain()
    task.in_file = File.sample(seed=1)
    task.mask = File.sample(seed=5)
    task.trainlabels = File.sample(seed=7)
    task.censor = File.sample(seed=8)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
