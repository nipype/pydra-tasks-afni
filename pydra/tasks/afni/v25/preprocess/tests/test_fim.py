from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.preprocess.fim import Fim
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_fim_1():
    task = Fim()
    task.in_file = Nifti1.sample(seed=0)
    task.ideal_file = File.sample(seed=2)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_fim_2():
    task = Fim()
    task.in_file = Nifti1.sample(seed=0)
    task.out_file = "functional_corr.nii"
    task.fim_thr = 0.0009
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
