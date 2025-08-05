from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.utils.local_bistat import LocalBistat
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_localbistat_1():
    task = LocalBistat()
    task.in_file1 = Nifti1.sample(seed=0)
    task.in_file2 = File.sample(seed=1)
    task.mask_file = File.sample(seed=4)
    task.weight_file = File.sample(seed=6)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_localbistat_2():
    task = LocalBistat()
    task.in_file1 = Nifti1.sample(seed=0)
    task.neighborhood = ("SPHERE", 1.2)
    task.outputtype = "NIFTI"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
