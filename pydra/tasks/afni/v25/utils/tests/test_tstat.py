from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.t_stat import TStat
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_tstat_1():
    task = TStat()
    task.in_file = Nifti1.sample(seed=0)
    task.mask = File.sample(seed=2)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tstat_2():
    task = TStat()
    task.in_file = Nifti1.sample(seed=0)
    task.out_file = "stats"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
