from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.preprocess.net_corr import NetCorr
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_netcorr_1():
    task = NetCorr()
    task.in_file = Nifti1.sample(seed=0)
    task.in_rois = Nifti1.sample(seed=1)
    task.mask = File.sample(seed=2)
    task.weight_ts = File.sample(seed=3)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_netcorr_2():
    task = NetCorr()
    task.in_file = Nifti1.sample(seed=0)
    task.in_rois = Nifti1.sample(seed=1)
    task.ts_wb_Z = True
    task.out_file = "sub0.tp1.ncorr"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
