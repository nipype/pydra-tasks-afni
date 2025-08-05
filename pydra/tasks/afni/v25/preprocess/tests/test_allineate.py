from fileformats.datascience import TextMatrix
from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.preprocess.allineate import Allineate
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_allineate_1():
    task = Allineate()
    task.in_file = Nifti1.sample(seed=0)
    task.reference = File.sample(seed=1)
    task.in_param_file = File.sample(seed=4)
    task.in_matrix = TextMatrix.sample(seed=6)
    task.weight_file = File.sample(seed=29)
    task.source_mask = File.sample(seed=32)
    task.master = File.sample(seed=43)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_allineate_2():
    task = Allineate()
    task.in_file = Nifti1.sample(seed=0)
    task.in_matrix = TextMatrix.sample(seed=6)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_allineate_3():
    task = Allineate()
    task.in_file = Nifti1.sample(seed=0)
    task.allcostx = "out.allcostX.txt"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_allineate_4():
    task = Allineate()
    task.in_file = Nifti1.sample(seed=0)
    task.nwarp_fixmot = ["X", "Y"]
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
