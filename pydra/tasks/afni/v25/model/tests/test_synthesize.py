from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25.model.synthesize import Synthesize
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_synthesize_1():
    task = Synthesize()
    task.cbucket = Nifti1.sample(seed=0)
    task.matrix = File.sample(seed=1)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_synthesize_2():
    task = Synthesize()
    task.cbucket = Nifti1.sample(seed=0)
    task.select = ["baseline"]
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
