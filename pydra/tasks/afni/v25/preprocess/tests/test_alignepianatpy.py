from fileformats.generic import File
from fileformats.medimage import Nifti1
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.preprocess.align_epi_anat_py import AlignEpiAnatPy
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_alignepianatpy_1():
    task = AlignEpiAnatPy()
    task.in_file = File.sample(seed=0)
    task.anat = Nifti1.sample(seed=1)
    task.suffix = "_al"
    task.volreg = "on"
    task.tshift = "on"
    task.py27_path = "python2"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_alignepianatpy_2():
    task = AlignEpiAnatPy()
    task.anat = Nifti1.sample(seed=1)
    task.epi_base = 0
    task.save_skullstrip = True
    task.volreg = "off"
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
