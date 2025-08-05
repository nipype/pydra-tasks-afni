from fileformats.generic import File
from fileformats.medimage import NiftiGz
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.preprocess.qwarp_plus_minus import QwarpPlusMinus
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_qwarpplusminus_1():
    task = QwarpPlusMinus()
    task.source_file = File.sample(seed=0)
    task.out_file = "Qwarp.nii.gz"
    task.plusminus = True
    task.in_file = NiftiGz.sample(seed=3)
    task.base_file = NiftiGz.sample(seed=4)
    task.weight = File.sample(seed=15)
    task.emask = File.sample(seed=22)
    task.iniwarp = [File.sample(seed=26)]
    task.gridlist = File.sample(seed=30)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_qwarpplusminus_2():
    task = QwarpPlusMinus()
    task.in_file = NiftiGz.sample(seed=3)
    task.base_file = NiftiGz.sample(seed=4)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
