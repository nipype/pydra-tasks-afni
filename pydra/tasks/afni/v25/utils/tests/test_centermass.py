from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.center_mass import CenterMass
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_centermass_1():
    task = CenterMass()
    task.in_file = Nifti1.sample(seed=0)
    task.mask_file = File.sample(seed=2)
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_centermass_2():
    task = CenterMass()
    task.in_file = Nifti1.sample(seed=0)
    task.roi_vals = [2, 10]
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
