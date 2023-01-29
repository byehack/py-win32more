from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Direct2D
import win32more.Graphics.Direct2D.Common
import win32more.Graphics.Dxgi
import win32more.System.Com
import win32more.System.WinRT.Pdf
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
@winfunctype('Windows.Data.Pdf.dll')
def PdfCreateRenderer(pDevice: win32more.Graphics.Dxgi.IDXGIDevice_head, ppRenderer: POINTER(win32more.System.WinRT.Pdf.IPdfRendererNative_head)) -> win32more.Foundation.HRESULT: ...
class IPdfRendererNative(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7d9dcd91-d277-4947-85-27-07-a0-da-ed-a9-4a')
    @commethod(3)
    def RenderPageToSurface(pdfPage: win32more.System.Com.IUnknown_head, pSurface: win32more.Graphics.Dxgi.IDXGISurface_head, offset: win32more.Foundation.POINT, pRenderParams: POINTER(win32more.System.WinRT.Pdf.PDF_RENDER_PARAMS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RenderPageToDeviceContext(pdfPage: win32more.System.Com.IUnknown_head, pD2DDeviceContext: win32more.Graphics.Direct2D.ID2D1DeviceContext_head, pRenderParams: POINTER(win32more.System.WinRT.Pdf.PDF_RENDER_PARAMS_head)) -> win32more.Foundation.HRESULT: ...
class PDF_RENDER_PARAMS(Structure):
    SourceRect: win32more.Graphics.Direct2D.Common.D2D_RECT_F
    DestinationWidth: UInt32
    DestinationHeight: UInt32
    BackgroundColor: win32more.Graphics.Direct2D.Common.D2D_COLOR_F
    IgnoreHighContrast: win32more.Foundation.BOOLEAN
@winfunctype_pointer
def PFN_PDF_CREATE_RENDERER(param0: win32more.Graphics.Dxgi.IDXGIDevice_head, param1: POINTER(win32more.System.WinRT.Pdf.IPdfRendererNative_head)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'IPdfRendererNative')
make_head(_module, 'PDF_RENDER_PARAMS')
make_head(_module, 'PFN_PDF_CREATE_RENDERER')
__all__ = [
    "IPdfRendererNative",
    "PDF_RENDER_PARAMS",
    "PFN_PDF_CREATE_RENDERER",
    "PdfCreateRenderer",
]
_arch_optional = [
]
