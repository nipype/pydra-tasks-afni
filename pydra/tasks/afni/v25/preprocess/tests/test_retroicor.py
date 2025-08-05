from fileformats.generic import File
from fileformats.medimage import Nifti1
from fileformats.medimage_afni import OneD
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.preprocess.retroicor import Retroicor
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_retroicor_1():
    task = Retroicor()
    task.in_file = Nifti1.sample(seed=0)
    task.card = File.sample(seed=2)
    task.resp = OneD.sample(seed=3)
    task.cardphase = File.sample(seed=6)
    task.respphase = File.sample(seed=7)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_retroicor_2():
    task = Retroicor()
    task.in_file = Nifti1.sample(seed=0)
    task.resp = OneD.sample(seed=3)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
