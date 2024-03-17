from ._version import __version__  # noqa: F401
from pathlib import Path
import typing as ty
from random import Random
from fileformats.core import FileSet
from fileformats.medimage_afni import (
    OneD,
    Head,
    All1,
    R1,
    ThreeD,
    Dset,
)


@FileSet.generate_sample_data.register
def gen_sample_oned_data(
    oned: OneD,
    dest_dir: Path,
    seed: ty.Union[int, Random] = 0,
    stem: ty.Optional[str] = None,
) -> ty.Iterable[Path]:
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_head_data(
    head: Head,
    dest_dir: Path,
    seed: ty.Union[int, Random] = 0,
    stem: ty.Optional[str] = None,
) -> ty.Iterable[Path]:
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_all1_data(
    all1: All1,
    dest_dir: Path,
    seed: ty.Union[int, Random] = 0,
    stem: ty.Optional[str] = None,
) -> ty.Iterable[Path]:
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_r1_data(
    r1: R1,
    dest_dir: Path,
    seed: ty.Union[int, Random] = 0,
    stem: ty.Optional[str] = None,
) -> ty.Iterable[Path]:
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_threed_data(
    threed: ThreeD,
    dest_dir: Path,
    seed: ty.Union[int, Random] = 0,
    stem: ty.Optional[str] = None,
) -> ty.Iterable[Path]:
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_dset_data(
    dset: Dset,
    dest_dir: Path,
    seed: ty.Union[int, Random] = 0,
    stem: ty.Optional[str] = None,
) -> ty.Iterable[Path]:
    raise NotImplementedError
