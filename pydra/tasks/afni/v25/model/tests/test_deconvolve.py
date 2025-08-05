from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.model.deconvolve import Deconvolve
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_deconvolve_1():
    task = Deconvolve()
    task.in_files = [Nifti1.sample(seed=0)]
    task.input1D = File.sample(seed=5)
    task.mask = File.sample(seed=19)
    task.STATmask = File.sample(seed=21)
    task.censor = File.sample(seed=22)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_deconvolve_2():
    task = Deconvolve()
    task.in_files = [Nifti1.sample(seed=0)]
    task.x1D = "output.1D"
    task.stim_times = stim_times
    task.gltsym = ["SYM: +Houses"]
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
