from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Storage.Compression
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
COMPRESS_ALGORITHM_INVALID: UInt32 = 0
COMPRESS_ALGORITHM_NULL: UInt32 = 1
COMPRESS_ALGORITHM_MAX: UInt32 = 6
COMPRESS_RAW: UInt32 = 536870912
@winfunctype('Cabinet.dll')
def CreateCompressor(Algorithm: win32more.Storage.Compression.COMPRESS_ALGORITHM, AllocationRoutines: POINTER(win32more.Storage.Compression.COMPRESS_ALLOCATION_ROUTINES_head), CompressorHandle: POINTER(IntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def SetCompressorInformation(CompressorHandle: win32more.Storage.Compression.COMPRESSOR_HANDLE, CompressInformationClass: win32more.Storage.Compression.COMPRESS_INFORMATION_CLASS, CompressInformation: c_void_p, CompressInformationSize: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def QueryCompressorInformation(CompressorHandle: win32more.Storage.Compression.COMPRESSOR_HANDLE, CompressInformationClass: win32more.Storage.Compression.COMPRESS_INFORMATION_CLASS, CompressInformation: c_void_p, CompressInformationSize: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def Compress(CompressorHandle: win32more.Storage.Compression.COMPRESSOR_HANDLE, UncompressedData: c_void_p, UncompressedDataSize: UIntPtr, CompressedBuffer: c_void_p, CompressedBufferSize: UIntPtr, CompressedDataSize: POINTER(UIntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def ResetCompressor(CompressorHandle: win32more.Storage.Compression.COMPRESSOR_HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def CloseCompressor(CompressorHandle: win32more.Storage.Compression.COMPRESSOR_HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def CreateDecompressor(Algorithm: win32more.Storage.Compression.COMPRESS_ALGORITHM, AllocationRoutines: POINTER(win32more.Storage.Compression.COMPRESS_ALLOCATION_ROUTINES_head), DecompressorHandle: POINTER(IntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def SetDecompressorInformation(DecompressorHandle: IntPtr, CompressInformationClass: win32more.Storage.Compression.COMPRESS_INFORMATION_CLASS, CompressInformation: c_void_p, CompressInformationSize: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def QueryDecompressorInformation(DecompressorHandle: IntPtr, CompressInformationClass: win32more.Storage.Compression.COMPRESS_INFORMATION_CLASS, CompressInformation: c_void_p, CompressInformationSize: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def Decompress(DecompressorHandle: IntPtr, CompressedData: c_void_p, CompressedDataSize: UIntPtr, UncompressedBuffer: c_void_p, UncompressedBufferSize: UIntPtr, UncompressedDataSize: POINTER(UIntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def ResetDecompressor(DecompressorHandle: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('Cabinet.dll')
def CloseDecompressor(DecompressorHandle: IntPtr) -> win32more.Foundation.BOOL: ...
COMPRESS_ALGORITHM = UInt32
COMPRESS_ALGORITHM_MSZIP: COMPRESS_ALGORITHM = 2
COMPRESS_ALGORITHM_XPRESS: COMPRESS_ALGORITHM = 3
COMPRESS_ALGORITHM_XPRESS_HUFF: COMPRESS_ALGORITHM = 4
COMPRESS_ALGORITHM_LZMS: COMPRESS_ALGORITHM = 5
class COMPRESS_ALLOCATION_ROUTINES(Structure):
    Allocate: win32more.Storage.Compression.PFN_COMPRESS_ALLOCATE
    Free: win32more.Storage.Compression.PFN_COMPRESS_FREE
    UserContext: c_void_p
COMPRESS_INFORMATION_CLASS = Int32
COMPRESS_INFORMATION_CLASS_INVALID: COMPRESS_INFORMATION_CLASS = 0
COMPRESS_INFORMATION_CLASS_BLOCK_SIZE: COMPRESS_INFORMATION_CLASS = 1
COMPRESS_INFORMATION_CLASS_LEVEL: COMPRESS_INFORMATION_CLASS = 2
COMPRESSOR_HANDLE = IntPtr
@cfunctype_pointer
def PFN_COMPRESS_ALLOCATE(UserContext: c_void_p, Size: UIntPtr) -> c_void_p: ...
@cfunctype_pointer
def PFN_COMPRESS_FREE(UserContext: c_void_p, Memory: c_void_p) -> Void: ...
make_head(_module, 'COMPRESS_ALLOCATION_ROUTINES')
make_head(_module, 'PFN_COMPRESS_ALLOCATE')
make_head(_module, 'PFN_COMPRESS_FREE')
__all__ = [
    "COMPRESSOR_HANDLE",
    "COMPRESS_ALGORITHM",
    "COMPRESS_ALGORITHM_INVALID",
    "COMPRESS_ALGORITHM_LZMS",
    "COMPRESS_ALGORITHM_MAX",
    "COMPRESS_ALGORITHM_MSZIP",
    "COMPRESS_ALGORITHM_NULL",
    "COMPRESS_ALGORITHM_XPRESS",
    "COMPRESS_ALGORITHM_XPRESS_HUFF",
    "COMPRESS_ALLOCATION_ROUTINES",
    "COMPRESS_INFORMATION_CLASS",
    "COMPRESS_INFORMATION_CLASS_BLOCK_SIZE",
    "COMPRESS_INFORMATION_CLASS_INVALID",
    "COMPRESS_INFORMATION_CLASS_LEVEL",
    "COMPRESS_RAW",
    "CloseCompressor",
    "CloseDecompressor",
    "Compress",
    "CreateCompressor",
    "CreateDecompressor",
    "Decompress",
    "PFN_COMPRESS_ALLOCATE",
    "PFN_COMPRESS_FREE",
    "QueryCompressorInformation",
    "QueryDecompressorInformation",
    "ResetCompressor",
    "ResetDecompressor",
    "SetCompressorInformation",
    "SetDecompressorInformation",
]
_arch_optional = [
]
