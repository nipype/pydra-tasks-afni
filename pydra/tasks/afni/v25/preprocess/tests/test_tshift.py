from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.preprocess.t_shift import TShift
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_tshift_1():
    task = TShift()
    task.in_file = Nifti1.sample(seed=0)
    task.slice_encoding_direction = "k"
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tshift_2():
    task = TShift()
    task.in_file = Nifti1.sample(seed=0)
    task.tr = "%.1fs" % TR
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tshift_3():
    task = TShift()
    task.slice_encoding_direction = "k-"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tshift_4():
    task = TShift()
    task.in_file = Nifti1.sample(seed=0)
    task.tr = "%.1fs" % TR
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tshift_5():
    task = TShift()
    task.in_file = Nifti1.sample(seed=0)
    task.tr = "%.1fs" % TR
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_tshift_6():
    task = TShift()
    task.in_file = Nifti1.sample(seed=0)
    task.tr = "%.1fs" % TR
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
