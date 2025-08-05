from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.preprocess.t_correlate import TCorrelate
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_tcorrelate_1():
    task = TCorrelate()
    task.xset = Nifti1.sample(seed=0)
    task.yset = File.sample(seed=1)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tcorrelate_2():
    task = TCorrelate()
    task.xset = Nifti1.sample(seed=0)
    task.out_file = "functional_tcorrelate.nii.gz"
    task.pearson = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
