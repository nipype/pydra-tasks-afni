from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.preprocess.t_project import TProject
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_tproject_1():
    task = TProject()
    task.in_file = Nifti1.sample(seed=0)
    task.censor = File.sample(seed=2)
    task.concat = File.sample(seed=5)
    task.ort = File.sample(seed=7)
    task.dsort = [File.sample(seed=9)]
    task.mask = File.sample(seed=13)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tproject_2():
    task = TProject()
    task.in_file = Nifti1.sample(seed=0)
    task.out_file = "projected.nii.gz"
    task.polort = 3
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
