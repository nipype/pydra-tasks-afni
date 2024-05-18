from pathlib import Path
import typing as ty
from random import Random
from fileformats.core import FileSet
from fileformats.medimage_afni import (
    Oned,
    Dset,
    Nii[0],
    Threed,
    Head,
    Ncorr,
    R1,
    All1,
    Oned,
    Unit errts+tlrc,
    Gii,
)
from ._version import __version__




@FileSet.generate_sample_data.register
def gen_sample_oned_data(oned: Oned, dest_dir: Path, seed: ty.Union[int, Random], stem: ty.Optional[str]):
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_dset_data(dset: Dset, dest_dir: Path, seed: ty.Union[int, Random], stem: ty.Optional[str]):
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_nii[0]_data(nii[0]: Nii[0], dest_dir: Path, seed: ty.Union[int, Random], stem: ty.Optional[str]):
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_threed_data(threed: Threed, dest_dir: Path, seed: ty.Union[int, Random], stem: ty.Optional[str]):
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_head_data(head: Head, dest_dir: Path, seed: ty.Union[int, Random], stem: ty.Optional[str]):
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_ncorr_data(ncorr: Ncorr, dest_dir: Path, seed: ty.Union[int, Random], stem: ty.Optional[str]):
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_r1_data(r1: R1, dest_dir: Path, seed: ty.Union[int, Random], stem: ty.Optional[str]):
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_all1_data(all1: All1, dest_dir: Path, seed: ty.Union[int, Random], stem: ty.Optional[str]):
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_oned_data(oned: Oned, dest_dir: Path, seed: ty.Union[int, Random], stem: ty.Optional[str]):
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_unit errts+tlrc_data(unit errts+tlrc: Unit errts+tlrc, dest_dir: Path, seed: ty.Union[int, Random], stem: ty.Optional[str]):
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_gii_data(gii: Gii, dest_dir: Path, seed: ty.Union[int, Random], stem: ty.Optional[str]):
    raise NotImplementedError
