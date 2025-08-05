from fileformats.generic import File
from fileformats.medimage_afni import OneD
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.utils.eval import Eval
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_eval_1():
    task = Eval()
    task.in_file_a = OneD.sample(seed=0)
    task.in_file_b = File.sample(seed=1)
    task.in_file_c = File.sample(seed=2)
    task.other = File.sample(seed=9)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_eval_2():
    task = Eval()
    task.in_file_a = OneD.sample(seed=0)
    task.out_file = "data_calc.1D"
    task.expr = "a*b"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
