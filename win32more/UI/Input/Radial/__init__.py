from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.WinRT
import win32more.UI.Input.Radial
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
class IRadialControllerConfigurationInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('787cdaac-3186-476d-87-e4-b9-37-4a-7b-99-70')
    @commethod(6)
    def GetForWindow(hwnd: win32more.Foundation.HWND, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IRadialControllerIndependentInputSourceInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('3d577eff-4cee-11e6-b5-35-00-1b-dc-06-ab-3b')
    @commethod(6)
    def CreateForWindow(hwnd: win32more.Foundation.HWND, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IRadialControllerInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('1b0535c9-57ad-45c1-9d-79-ad-5c-34-36-05-13')
    @commethod(6)
    def CreateForWindow(hwnd: win32more.Foundation.HWND, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'IRadialControllerConfigurationInterop')
make_head(_module, 'IRadialControllerIndependentInputSourceInterop')
make_head(_module, 'IRadialControllerInterop')
__all__ = [
    "IRadialControllerConfigurationInterop",
    "IRadialControllerIndependentInputSourceInterop",
    "IRadialControllerInterop",
]
_arch_optional = [
]
