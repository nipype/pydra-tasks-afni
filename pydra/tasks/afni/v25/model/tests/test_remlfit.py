from fileformats.generic import File
from fileformats.medimage import Nifti1
from fileformats.medimage_afni import OneD
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.model.remlfit import Remlfit
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_remlfit_1():
    task = Remlfit()
    task.in_files = [Nifti1.sample(seed=0)]
    task.matrix = OneD.sample(seed=1)
    task.matim = File.sample(seed=3)
    task.mask = File.sample(seed=4)
    task.automask = False
    task.STATmask = File.sample(seed=6)
    task.addbase = [File.sample(seed=7)]
    task.slibase = [File.sample(seed=8)]
    task.slibase_sm = [File.sample(seed=9)]
    task.dsort = File.sample(seed=12)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_remlfit_2():
    task = Remlfit()
    task.in_files = [Nifti1.sample(seed=0)]
    task.matrix = OneD.sample(seed=1)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
