from fileformats.medimage import Gifti
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.convert_dset import ConvertDset
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_convertdset_1():
    task = ConvertDset()
    task.in_file = Gifti.sample(seed=0)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_convertdset_2():
    task = ConvertDset()
    task.in_file = Gifti.sample(seed=0)
    task.out_file = "lh.pial_converted.niml.dset"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
