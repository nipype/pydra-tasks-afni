from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.localstat import Localstat
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_localstat_1():
    task = Localstat()
    task.in_file = Nifti1.sample(seed=0)
    task.mask_file = File.sample(seed=3)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_localstat_2():
    task = Localstat()
    task.in_file = Nifti1.sample(seed=0)
    task.neighborhood = ("SPHERE", 45)
    task.nonmask = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
