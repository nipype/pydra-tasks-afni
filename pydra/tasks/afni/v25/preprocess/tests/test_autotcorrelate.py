from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.preprocess.auto_tcorrelate import AutoTcorrelate
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_autotcorrelate_1():
    task = AutoTcorrelate()
    task.in_file = Nifti1.sample(seed=0)
    task.mask = File.sample(seed=3)
    task.mask_source = File.sample(seed=5)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_autotcorrelate_2():
    task = AutoTcorrelate()
    task.in_file = Nifti1.sample(seed=0)
    task.eta2 = True
    task.mask_only_targets = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
