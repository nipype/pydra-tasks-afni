from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.preprocess.quality_index import QualityIndex
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_qualityindex_1():
    task = QualityIndex()
    task.in_file = Nifti1.sample(seed=0)
    task.mask = File.sample(seed=1)
    task.spearman = False
    task.quadrant = False
    task.autoclip = False
    task.automask = False
    task.interval = False
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_qualityindex_2():
    task = QualityIndex()
    task.in_file = Nifti1.sample(seed=0)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
