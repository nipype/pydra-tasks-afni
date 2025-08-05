from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.preprocess.t_corr_map import TCorrMap
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_tcorrmap_1():
    task = TCorrMap()
    task.in_file = Nifti1.sample(seed=0)
    task.seeds = File.sample(seed=1)
    task.mask = File.sample(seed=2)
    task.regress_out_timeseries = File.sample(seed=6)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tcorrmap_2():
    task = TCorrMap()
    task.in_file = Nifti1.sample(seed=0)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
