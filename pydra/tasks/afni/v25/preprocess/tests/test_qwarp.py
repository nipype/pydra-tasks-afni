from fileformats.generic import File
from fileformats.medimage import Nifti1, NiftiGz
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.preprocess.qwarp import Qwarp
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_qwarp_1():
    task = Qwarp()
    task.in_file = Nifti1.sample(seed=0)
    task.base_file = NiftiGz.sample(seed=1)
    task.weight = File.sample(seed=13)
    task.emask = File.sample(seed=20)
    task.iniwarp = [File.sample(seed=24)]
    task.gridlist = File.sample(seed=28)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_qwarp_2():
    task = Qwarp()
    task.in_file = Nifti1.sample(seed=0)
    task.base_file = NiftiGz.sample(seed=1)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_qwarp_3():
    task = Qwarp()
    task.in_file = Nifti1.sample(seed=0)
    task.resample = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_qwarp_4():
    task = Qwarp()
    task.in_file = Nifti1.sample(seed=0)
    task.out_file = "anatSSQ.nii.gz"
    task.iwarp = True
    task.lpc = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_qwarp_5():
    task = Qwarp()
    task.in_file = Nifti1.sample(seed=0)
    task.duplo = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_qwarp_6():
    task = Qwarp()
    task.in_file = Nifti1.sample(seed=0)
    task.blur = [0, 3]
    task.duplo = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_qwarp_7():
    task = Qwarp()
    task.in_file = Nifti1.sample(seed=0)
    task.blur = [0, 2]
    task.inilev = 7
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_qwarp_8():
    task = Qwarp()
    task.in_file = Nifti1.sample(seed=0)
    task.allineate = True
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
