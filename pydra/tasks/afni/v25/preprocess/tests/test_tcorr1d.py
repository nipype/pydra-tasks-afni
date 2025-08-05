from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.preprocess.t_corr_1d import TCorr1D
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_tcorr1d_1():
    task = TCorr1D()
    task.xset = Nifti1.sample(seed=0)
    task.y_1d = File.sample(seed=1)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tcorr1d_2():
    task = TCorr1D()
    task.xset = Nifti1.sample(seed=0)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
