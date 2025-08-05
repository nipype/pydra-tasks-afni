from fileformats.medimage_afni import Head
import logging
from nipype2pydra.testing import PassAfterTimeoutWorker
from pydra.tasks.afni.v25_2_06.utils.notes import Notes
import pytest


logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_notes_1():
    task = Notes()
    task.in_file = Head.sample(seed=0)
    task.num_threads = 1
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)


@pytest.mark.xfail
def test_notes_2():
    task = Notes()
    task.in_file = Head.sample(seed=0)
    task.add_history = "This note is added to history."
    print(f"CMDLINE: {task.cmdline}\n\n")
    res = task(worker=PassAfterTimeoutWorker)
    print("RESULT: ", res)
