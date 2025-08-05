from fileformats.generic import File
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.utils.dot import Dot
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_dot_1():
    task = Dot()
    task.in_files = [File.sample(seed=0)]
    task.mask = File.sample(seed=2)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_dot_2():
    task = Dot()
    task.in_files = [File.sample(seed=0)]
    task.out_file = "out.mask_ae_dice.txt"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
