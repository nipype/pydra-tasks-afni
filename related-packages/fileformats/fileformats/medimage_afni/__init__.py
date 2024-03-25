from ._version import __version__  # noqa: F401
from fileformats.generic import File


class OneD(File):
    ext = ".1d"
    binary = True


class Dset(File):
    ext = ".dset"
    binary = True


class Head(File):
    ext = ".HEAD"
    binary = True


class All1(File):
    ext = ".all1"
    binary = True


class R1(File):
    ext = ".r1"
    binary = True


class NCorr(File):
    ext = ".ncorr"
    binary = True


class ThreeD(File):
    ext = ".3D"
    binary = True
    alternate_exts = (".3d",)
