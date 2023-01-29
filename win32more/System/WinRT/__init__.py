from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.Com.Marshal
import win32more.System.WinRT
import win32more.UI.Shell.PropertiesSystem
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
class _RO_REGISTRATION_COOKIE(Structure):
    pass
ACTIVATIONTYPE = Int32
ACTIVATIONTYPE_UNCATEGORIZED: ACTIVATIONTYPE = 0
ACTIVATIONTYPE_FROM_MONIKER: ACTIVATIONTYPE = 1
ACTIVATIONTYPE_FROM_DATA: ACTIVATIONTYPE = 2
ACTIVATIONTYPE_FROM_STORAGE: ACTIVATIONTYPE = 4
ACTIVATIONTYPE_FROM_STREAM: ACTIVATIONTYPE = 8
ACTIVATIONTYPE_FROM_FILE: ACTIVATIONTYPE = 16
AgileReferenceOptions = Int32
AGILEREFERENCE_DEFAULT: AgileReferenceOptions = 0
AGILEREFERENCE_DELAYEDMARSHAL: AgileReferenceOptions = 1
APARTMENT_SHUTDOWN_REGISTRATION_COOKIE = IntPtr
MAX_ERROR_MESSAGE_CHARS: UInt32 = 512
CastingSourceInfo_Property_PreferredSourceUriScheme: String = 'PreferredSourceUriScheme'
CastingSourceInfo_Property_CastingTypes: String = 'CastingTypes'
CastingSourceInfo_Property_ProtectedMedia: String = 'ProtectedMedia'
@winfunctype('OLE32.dll')
def CoDecodeProxy(dwClientPid: UInt32, ui64ProxyAddress: UInt64, pServerInformation: POINTER(win32more.System.WinRT.ServerInformation_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def RoGetAgileReference(options: win32more.System.WinRT.AgileReferenceOptions, riid: POINTER(Guid), pUnk: win32more.System.Com.IUnknown_head, ppAgileReference: POINTER(win32more.System.WinRT.IAgileReference_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(win32more.System.WinRT.HSTRING)) -> UInt32: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserMarshal(param0: POINTER(UInt32), param1: c_char_p_no, param2: POINTER(win32more.System.WinRT.HSTRING)) -> c_char_p_no: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserUnmarshal(param0: POINTER(UInt32), param1: c_char_p_no, param2: POINTER(win32more.System.WinRT.HSTRING)) -> c_char_p_no: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserFree(param0: POINTER(UInt32), param1: POINTER(win32more.System.WinRT.HSTRING)) -> Void: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(win32more.System.WinRT.HSTRING)) -> UInt32: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserMarshal64(param0: POINTER(UInt32), param1: c_char_p_no, param2: POINTER(win32more.System.WinRT.HSTRING)) -> c_char_p_no: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserUnmarshal64(param0: POINTER(UInt32), param1: c_char_p_no, param2: POINTER(win32more.System.WinRT.HSTRING)) -> c_char_p_no: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserFree64(param0: POINTER(UInt32), param1: POINTER(win32more.System.WinRT.HSTRING)) -> Void: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsCreateString(sourceString: win32more.Foundation.PWSTR, length: UInt32, string: POINTER(win32more.System.WinRT.HSTRING)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsCreateStringReference(sourceString: win32more.Foundation.PWSTR, length: UInt32, hstringHeader: POINTER(win32more.System.WinRT.HSTRING_HEADER_head), string: POINTER(win32more.System.WinRT.HSTRING)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsDeleteString(string: win32more.System.WinRT.HSTRING) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsDuplicateString(string: win32more.System.WinRT.HSTRING, newString: POINTER(win32more.System.WinRT.HSTRING)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsGetStringLen(string: win32more.System.WinRT.HSTRING) -> UInt32: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsGetStringRawBuffer(string: win32more.System.WinRT.HSTRING, length: POINTER(UInt32)) -> win32more.Foundation.PWSTR: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsIsStringEmpty(string: win32more.System.WinRT.HSTRING) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsStringHasEmbeddedNull(string: win32more.System.WinRT.HSTRING, hasEmbedNull: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsCompareStringOrdinal(string1: win32more.System.WinRT.HSTRING, string2: win32more.System.WinRT.HSTRING, result: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsSubstring(string: win32more.System.WinRT.HSTRING, startIndex: UInt32, newString: POINTER(win32more.System.WinRT.HSTRING)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsSubstringWithSpecifiedLength(string: win32more.System.WinRT.HSTRING, startIndex: UInt32, length: UInt32, newString: POINTER(win32more.System.WinRT.HSTRING)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsConcatString(string1: win32more.System.WinRT.HSTRING, string2: win32more.System.WinRT.HSTRING, newString: POINTER(win32more.System.WinRT.HSTRING)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsReplaceString(string: win32more.System.WinRT.HSTRING, stringReplaced: win32more.System.WinRT.HSTRING, stringReplaceWith: win32more.System.WinRT.HSTRING, newString: POINTER(win32more.System.WinRT.HSTRING)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsTrimStringStart(string: win32more.System.WinRT.HSTRING, trimString: win32more.System.WinRT.HSTRING, newString: POINTER(win32more.System.WinRT.HSTRING)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsTrimStringEnd(string: win32more.System.WinRT.HSTRING, trimString: win32more.System.WinRT.HSTRING, newString: POINTER(win32more.System.WinRT.HSTRING)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsPreallocateStringBuffer(length: UInt32, charBuffer: POINTER(POINTER(UInt16)), bufferHandle: POINTER(win32more.System.WinRT.HSTRING_BUFFER)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsPromoteStringBuffer(bufferHandle: win32more.System.WinRT.HSTRING_BUFFER, string: POINTER(win32more.System.WinRT.HSTRING)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsDeleteStringBuffer(bufferHandle: win32more.System.WinRT.HSTRING_BUFFER) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsInspectString(targetHString: UIntPtr, machine: UInt16, callback: win32more.System.WinRT.PINSPECT_HSTRING_CALLBACK, context: c_void_p, length: POINTER(UInt32), targetStringAddress: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-1.dll')
def WindowsInspectString2(targetHString: UInt64, machine: UInt16, callback: win32more.System.WinRT.PINSPECT_HSTRING_CALLBACK2, context: c_void_p, length: POINTER(UInt32), targetStringAddress: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('CoreMessaging.dll')
def CreateDispatcherQueueController(options: win32more.System.WinRT.DispatcherQueueOptions, dispatcherQueueController: POINTER(MissingType)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoInitialize(initType: win32more.System.WinRT.RO_INIT_TYPE) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoUninitialize() -> Void: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoActivateInstance(activatableClassId: win32more.System.WinRT.HSTRING, instance: POINTER(win32more.System.WinRT.IInspectable_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoRegisterActivationFactories(activatableClassIds: POINTER(win32more.System.WinRT.HSTRING), activationFactoryCallbacks: POINTER(IntPtr), count: UInt32, cookie: POINTER(IntPtr)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoRevokeActivationFactories(cookie: IntPtr) -> Void: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoGetActivationFactory(activatableClassId: win32more.System.WinRT.HSTRING, iid: POINTER(Guid), factory: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoRegisterForApartmentShutdown(callbackObject: win32more.System.WinRT.IApartmentShutdown_head, apartmentIdentifier: POINTER(UInt64), regCookie: POINTER(win32more.System.WinRT.APARTMENT_SHUTDOWN_REGISTRATION_COOKIE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoUnregisterForApartmentShutdown(regCookie: win32more.System.WinRT.APARTMENT_SHUTDOWN_REGISTRATION_COOKIE) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoGetApartmentIdentifier(apartmentIdentifier: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-robuffer-l1-1-0.dll')
def RoGetBufferMarshaler(bufferMarshaler: POINTER(win32more.System.Com.Marshal.IMarshal_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoGetErrorReportingFlags(pflags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoSetErrorReportingFlags(flags: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoResolveRestrictedErrorInfoReference(reference: win32more.Foundation.PWSTR, ppRestrictedErrorInfo: POINTER(win32more.System.WinRT.IRestrictedErrorInfo_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def SetRestrictedErrorInfo(pRestrictedErrorInfo: win32more.System.WinRT.IRestrictedErrorInfo_head) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def GetRestrictedErrorInfo(ppRestrictedErrorInfo: POINTER(win32more.System.WinRT.IRestrictedErrorInfo_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoOriginateErrorW(error: win32more.Foundation.HRESULT, cchMax: UInt32, message: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoOriginateError(error: win32more.Foundation.HRESULT, message: win32more.System.WinRT.HSTRING) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoTransformErrorW(oldError: win32more.Foundation.HRESULT, newError: win32more.Foundation.HRESULT, cchMax: UInt32, message: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoTransformError(oldError: win32more.Foundation.HRESULT, newError: win32more.Foundation.HRESULT, message: win32more.System.WinRT.HSTRING) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoCaptureErrorContext(hr: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoFailFastWithErrorContext(hrError: win32more.Foundation.HRESULT) -> Void: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoOriginateLanguageException(error: win32more.Foundation.HRESULT, message: win32more.System.WinRT.HSTRING, languageException: win32more.System.Com.IUnknown_head) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoClearError() -> Void: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoReportUnhandledError(pRestrictedErrorInfo: win32more.System.WinRT.IRestrictedErrorInfo_head) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoInspectThreadErrorInfo(targetTebAddress: UIntPtr, machine: UInt16, readMemoryCallback: win32more.System.WinRT.PINSPECT_MEMORY_CALLBACK, context: c_void_p, targetErrorInfoAddress: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoInspectCapturedStackBackTrace(targetErrorInfoAddress: UIntPtr, machine: UInt16, readMemoryCallback: win32more.System.WinRT.PINSPECT_MEMORY_CALLBACK, context: c_void_p, frameCount: POINTER(UInt32), targetBackTraceAddress: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoGetMatchingRestrictedErrorInfo(hrIn: win32more.Foundation.HRESULT, ppRestrictedErrorInfo: POINTER(win32more.System.WinRT.IRestrictedErrorInfo_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoReportFailedDelegate(punkDelegate: win32more.System.Com.IUnknown_head, pRestrictedErrorInfo: win32more.System.WinRT.IRestrictedErrorInfo_head) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def IsErrorPropagationEnabled() -> win32more.Foundation.BOOL: ...
@winfunctype('RoMetadata.dll')
def MetaDataGetDispenser(rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll')
def RoGetParameterizedTypeInstanceIID(nameElementCount: UInt32, nameElements: POINTER(win32more.Foundation.PWSTR), metaDataLocator: win32more.System.WinRT.IRoMetaDataLocator_head, iid: POINTER(Guid), pExtra: POINTER(win32more.System.WinRT.ROPARAMIIDHANDLE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll')
def RoFreeParameterizedTypeExtra(extra: win32more.System.WinRT.ROPARAMIIDHANDLE) -> Void: ...
@winfunctype('api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll')
def RoParameterizedTypeExtraGetTypeSignature(extra: win32more.System.WinRT.ROPARAMIIDHANDLE) -> win32more.Foundation.PSTR: ...
@winfunctype('api-ms-win-core-winrt-registration-l1-1-0.dll')
def RoGetServerActivatableClasses(serverName: win32more.System.WinRT.HSTRING, activatableClassIds: POINTER(POINTER(win32more.System.WinRT.HSTRING)), count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-stream-winrt-l1-1-0.dll')
def CreateRandomAccessStreamOnFile(filePath: win32more.Foundation.PWSTR, accessMode: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-stream-winrt-l1-1-0.dll')
def CreateRandomAccessStreamOverStream(stream: win32more.System.Com.IStream_head, options: win32more.System.WinRT.BSOS_OPTIONS, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-stream-winrt-l1-1-0.dll')
def CreateStreamOverRandomAccessStream(randomAccessStream: win32more.System.Com.IUnknown_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@cfunctype('Windows.UI.dll')
def CreateControlInput(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@cfunctype('Windows.UI.dll')
def CreateControlInputEx(pCoreWindow: win32more.System.Com.IUnknown_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
BSOS_OPTIONS = Int32
BSOS_DEFAULT: BSOS_OPTIONS = 0
BSOS_PREFERDESTINATIONSTREAM: BSOS_OPTIONS = 1
CASTING_CONNECTION_ERROR_STATUS = Int32
CASTING_CONNECTION_ERROR_STATUS_SUCCEEDED: CASTING_CONNECTION_ERROR_STATUS = 0
CASTING_CONNECTION_ERROR_STATUS_DEVICE_DID_NOT_RESPOND: CASTING_CONNECTION_ERROR_STATUS = 1
CASTING_CONNECTION_ERROR_STATUS_DEVICE_ERROR: CASTING_CONNECTION_ERROR_STATUS = 2
CASTING_CONNECTION_ERROR_STATUS_DEVICE_LOCKED: CASTING_CONNECTION_ERROR_STATUS = 3
CASTING_CONNECTION_ERROR_STATUS_PROTECTED_PLAYBACK_FAILED: CASTING_CONNECTION_ERROR_STATUS = 4
CASTING_CONNECTION_ERROR_STATUS_INVALID_CASTING_SOURCE: CASTING_CONNECTION_ERROR_STATUS = 5
CASTING_CONNECTION_ERROR_STATUS_UNKNOWN: CASTING_CONNECTION_ERROR_STATUS = 6
CASTING_CONNECTION_STATE = Int32
CASTING_CONNECTION_STATE_DISCONNECTED: CASTING_CONNECTION_STATE = 0
CASTING_CONNECTION_STATE_CONNECTED: CASTING_CONNECTION_STATE = 1
CASTING_CONNECTION_STATE_RENDERING: CASTING_CONNECTION_STATE = 2
CASTING_CONNECTION_STATE_DISCONNECTING: CASTING_CONNECTION_STATE = 3
CASTING_CONNECTION_STATE_CONNECTING: CASTING_CONNECTION_STATE = 4
DISPATCHERQUEUE_THREAD_APARTMENTTYPE = Int32
DQTAT_COM_NONE: DISPATCHERQUEUE_THREAD_APARTMENTTYPE = 0
DQTAT_COM_ASTA: DISPATCHERQUEUE_THREAD_APARTMENTTYPE = 1
DQTAT_COM_STA: DISPATCHERQUEUE_THREAD_APARTMENTTYPE = 2
DISPATCHERQUEUE_THREAD_TYPE = Int32
DQTYPE_THREAD_DEDICATED: DISPATCHERQUEUE_THREAD_TYPE = 1
DQTYPE_THREAD_CURRENT: DISPATCHERQUEUE_THREAD_TYPE = 2
class DispatcherQueueOptions(Structure):
    dwSize: UInt32
    threadType: win32more.System.WinRT.DISPATCHERQUEUE_THREAD_TYPE
    apartmentType: win32more.System.WinRT.DISPATCHERQUEUE_THREAD_APARTMENTTYPE
class EventRegistrationToken(Structure):
    value: Int64
HSTRING = IntPtr
HSTRING_BUFFER = IntPtr
class HSTRING_HEADER(Structure):
    flags: UInt32
    length: UInt32
    padding1: UInt32
    padding2: UInt32
    data: IntPtr
class IAccountsSettingsPaneInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('d3ee12ad-3865-4362-97-46-b7-5a-68-2d-f0-e6')
    @commethod(6)
    def GetForWindow(appWindow: win32more.Foundation.HWND, riid: POINTER(Guid), accountsSettingsPane: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ShowManageAccountsForWindowAsync(appWindow: win32more.Foundation.HWND, riid: POINTER(Guid), asyncAction: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ShowAddAccountForWindowAsync(appWindow: win32more.Foundation.HWND, riid: POINTER(Guid), asyncAction: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IActivationFactory(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('00000035-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(6)
    def ActivateInstance(instance: POINTER(win32more.System.WinRT.IInspectable_head)) -> win32more.Foundation.HRESULT: ...
class IAgileReference(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c03f6a43-65a4-9818-98-7e-e0-b8-10-d2-a6-f2')
    @commethod(3)
    def Resolve(riid: POINTER(Guid), ppvObjectReference: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IApartmentShutdown(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a2f05a09-27a2-42b5-bc-0e-ac-16-3e-f4-9d-9b')
    @commethod(3)
    def OnUninitialize(ui64ApartmentIdentifier: UInt64) -> Void: ...
class IAppServiceConnectionExtendedExecution(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('65219584-f9cb-4ae3-81-f9-a2-8a-6c-a4-50-d9')
    @commethod(3)
    def OpenForExtendedExecutionAsync(riid: POINTER(Guid), operation: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IBufferByteAccess(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('905a0fef-bc53-11df-8c-49-00-1e-4f-c6-86-da')
    @commethod(3)
    def Buffer(value: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
class ICastingController(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f0a56423-a664-4fbd-8b-43-40-9a-45-e8-d9-a1')
    @commethod(3)
    def Initialize(castingEngine: win32more.System.Com.IUnknown_head, castingSource: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Connect() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Disconnect() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Advise(eventHandler: win32more.System.WinRT.ICastingEventHandler_head, cookie: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def UnAdvise(cookie: UInt32) -> win32more.Foundation.HRESULT: ...
class ICastingEventHandler(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c79a6cb7-bebd-47a6-a2-ad-4d-45-ad-79-c7-bc')
    @commethod(3)
    def OnStateChanged(newState: win32more.System.WinRT.CASTING_CONNECTION_STATE) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnError(errorStatus: win32more.System.WinRT.CASTING_CONNECTION_ERROR_STATUS, errorMessage: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class ICastingSourceInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('45101ab7-7c3a-4bce-95-00-12-c0-90-24-b2-98')
    @commethod(3)
    def GetController(controller: POINTER(win32more.System.WinRT.ICastingController_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperties(props: POINTER(win32more.UI.Shell.PropertiesSystem.INamedPropertyStore_head)) -> win32more.Foundation.HRESULT: ...
class ICoreInputInterop(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('40bfe3e3-b75a-4479-ac-96-47-53-65-74-9b-b8')
    @commethod(3)
    def SetInputSource(value: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_MessageHandled(value: Byte) -> win32more.Foundation.HRESULT: ...
class ICoreWindowAdapterInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('7a5b6fd1-cd73-4b6c-9c-f4-2e-86-9e-af-47-0a')
    @commethod(6)
    def get_AppActivationClientAdapter(value: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_ApplicationViewClientAdapter(value: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_CoreApplicationViewClientAdapter(value: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_HoloViewClientAdapter(value: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_PositionerClientAdapter(value: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_SystemNavigationClientAdapter(value: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_TitleBarClientAdapter(value: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetWindowClientAdapter(value: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class ICoreWindowComponentInterop(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0576ab31-a310-4c40-ba-31-fd-37-e0-29-8d-fa')
    @commethod(3)
    def ConfigureComponentInput(hostViewInstanceId: UInt32, hwndHost: win32more.Foundation.HWND, inputSourceVisual: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetViewInstanceId(componentViewInstanceId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ICoreWindowInterop(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('45d64a29-a63e-4cb6-b4-98-57-81-d2-98-cb-4f')
    @commethod(3)
    def get_WindowHandle(hwnd: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_MessageHandled(value: Byte) -> win32more.Foundation.HRESULT: ...
class ICorrelationVectorInformation(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('83c78b3c-d88b-4950-aa-6e-22-b8-d2-2a-ab-d3')
    @commethod(6)
    def get_LastCorrelationVectorForThread(cv: POINTER(win32more.System.WinRT.HSTRING)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_NextCorrelationVectorForThread(cv: POINTER(win32more.System.WinRT.HSTRING)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_NextCorrelationVectorForThread(cv: win32more.System.WinRT.HSTRING) -> win32more.Foundation.HRESULT: ...
class ICorrelationVectorSource(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('152b8a3b-b9b9-4685-b5-6e-97-48-47-bc-75-45')
    @commethod(3)
    def get_CorrelationVector(cv: POINTER(win32more.System.WinRT.HSTRING)) -> win32more.Foundation.HRESULT: ...
class IDragDropManagerInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('5ad8cba7-4c01-4dac-90-74-82-78-94-29-2d-63')
    @commethod(6)
    def GetForWindow(hwnd: win32more.Foundation.HWND, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IHolographicSpaceInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('5c4ee536-6a98-4b86-a1-70-58-70-13-d6-fd-4b')
    @commethod(6)
    def CreateForWindow(window: win32more.Foundation.HWND, riid: POINTER(Guid), holographicSpace: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IInputPaneInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('75cf2c57-9195-4931-83-32-f0-b4-09-e9-16-af')
    @commethod(6)
    def GetForWindow(appWindow: win32more.Foundation.HWND, riid: POINTER(Guid), inputPane: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IInspectable(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('af86e2e0-b12d-4c6a-9c-5a-d7-aa-65-10-1e-90')
    @commethod(3)
    def GetIids(iidCount: POINTER(UInt32), iids: POINTER(POINTER(Guid))) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetRuntimeClassName(className: POINTER(win32more.System.WinRT.HSTRING)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetTrustLevel(trustLevel: POINTER(win32more.System.WinRT.TrustLevel)) -> win32more.Foundation.HRESULT: ...
class ILanguageExceptionErrorInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('04a2dbf3-df83-116c-09-46-08-12-ab-f6-e0-7d')
    @commethod(3)
    def GetLanguageException(languageException: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class ILanguageExceptionErrorInfo2(c_void_p):
    extends: win32more.System.WinRT.ILanguageExceptionErrorInfo
    Guid = Guid('5746e5c4-5b97-424c-b6-20-28-22-91-57-34-dd')
    @commethod(4)
    def GetPreviousLanguageExceptionErrorInfo(previousLanguageExceptionErrorInfo: POINTER(win32more.System.WinRT.ILanguageExceptionErrorInfo2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CapturePropagationContext(languageException: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropagationContextHead(propagatedLanguageExceptionErrorInfoHead: POINTER(win32more.System.WinRT.ILanguageExceptionErrorInfo2_head)) -> win32more.Foundation.HRESULT: ...
class ILanguageExceptionStackBackTrace(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('cbe53fb5-f967-4258-8d-34-42-f5-e2-58-33-de')
    @commethod(3)
    def GetStackBackTrace(maxFramesToCapture: UInt32, stackBackTrace: POINTER(UIntPtr), framesCaptured: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ILanguageExceptionTransform(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('feb5a271-a6cd-45ce-88-0a-69-67-06-ba-dc-65')
    @commethod(3)
    def GetTransformedRestrictedErrorInfo(restrictedErrorInfo: POINTER(win32more.System.WinRT.IRestrictedErrorInfo_head)) -> win32more.Foundation.HRESULT: ...
class IMemoryBufferByteAccess(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5b0d3235-4dba-4d44-86-5e-8f-1d-0e-4f-d0-4d')
    @commethod(3)
    def GetBuffer(value: POINTER(c_char_p_no), capacity: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IMessageDispatcher(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('f5f84c8f-cfd0-4cd6-b6-6b-c5-d2-6f-f1-68-9d')
    @commethod(6)
    def PumpMessages() -> win32more.Foundation.HRESULT: ...
class IPlayToManagerInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('24394699-1f2c-4eb3-8c-d7-0e-c1-da-42-a5-40')
    @commethod(6)
    def GetForWindow(appWindow: win32more.Foundation.HWND, riid: POINTER(Guid), playToManager: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ShowPlayToUIForWindow(appWindow: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
class IRestrictedErrorInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('82ba7092-4c88-427d-a7-bc-16-dd-93-fe-b6-7e')
    @commethod(3)
    def GetErrorDetails(description: POINTER(win32more.Foundation.BSTR), error: POINTER(win32more.Foundation.HRESULT), restrictedDescription: POINTER(win32more.Foundation.BSTR), capabilitySid: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetReference(reference: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IRoMetaDataLocator(c_void_p):
    extends: None
    @commethod(0)
    def Locate(nameElement: win32more.Foundation.PWSTR, metaDataDestination: win32more.System.WinRT.IRoSimpleMetaDataBuilder_head) -> win32more.Foundation.HRESULT: ...
class IRoSimpleMetaDataBuilder(c_void_p):
    extends: None
    @commethod(0)
    def SetWinRtInterface(iid: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(1)
    def SetDelegate(iid: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(2)
    def SetInterfaceGroupSimpleDefault(name: win32more.Foundation.PWSTR, defaultInterfaceName: win32more.Foundation.PWSTR, defaultInterfaceIID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(3)
    def SetInterfaceGroupParameterizedDefault(name: win32more.Foundation.PWSTR, elementCount: UInt32, defaultInterfaceNameElements: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetRuntimeClassSimpleDefault(name: win32more.Foundation.PWSTR, defaultInterfaceName: win32more.Foundation.PWSTR, defaultInterfaceIID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetRuntimeClassParameterizedDefault(name: win32more.Foundation.PWSTR, elementCount: UInt32, defaultInterfaceNameElements: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetStruct(name: win32more.Foundation.PWSTR, numFields: UInt32, fieldTypeNames: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetEnum(name: win32more.Foundation.PWSTR, baseType: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetParameterizedInterface(piid: Guid, numArgs: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetParameterizedDelegate(piid: Guid, numArgs: UInt32) -> win32more.Foundation.HRESULT: ...
class IShareWindowCommandEventArgsInterop(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6571a721-643d-43d4-ac-a4-6b-6f-5f-30-f1-ad')
    @commethod(3)
    def GetWindow(value: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.HRESULT: ...
class IShareWindowCommandSourceInterop(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('461a191f-8424-43a6-a0-fa-34-51-a2-2f-56-ab')
    @commethod(3)
    def GetForWindow(appWindow: win32more.Foundation.HWND, riid: POINTER(Guid), shareWindowCommandSource: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class ISpatialInteractionManagerInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('5c4ee536-6a98-4b86-a1-70-58-70-13-d6-fd-4b')
    @commethod(6)
    def GetForWindow(window: win32more.Foundation.HWND, riid: POINTER(Guid), spatialInteractionManager: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class ISystemMediaTransportControlsInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('ddb0472d-c911-4a1f-86-d9-dc-3d-71-a9-5f-5a')
    @commethod(6)
    def GetForWindow(appWindow: win32more.Foundation.HWND, riid: POINTER(Guid), mediaTransportControl: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IUIViewSettingsInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('3694dbf9-8f68-44be-8f-f5-19-5c-98-ed-e8-a6')
    @commethod(6)
    def GetForWindow(hwnd: win32more.Foundation.HWND, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IUserActivityInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('1ade314d-0e0a-40d9-82-4c-9a-08-8a-50-05-9f')
    @commethod(6)
    def CreateSessionForWindow(window: win32more.Foundation.HWND, iid: POINTER(Guid), value: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IUserActivityRequestManagerInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('dd69f876-9699-4715-90-95-e3-7e-a3-0d-fa-1b')
    @commethod(6)
    def GetForWindow(window: win32more.Foundation.HWND, iid: POINTER(Guid), value: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IUserActivitySourceHostInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('c15df8bc-8844-487a-b8-5b-75-78-e0-f6-14-19')
    @commethod(6)
    def SetActivitySourceHost(activitySourceHost: win32more.System.WinRT.HSTRING) -> win32more.Foundation.HRESULT: ...
class IUserConsentVerifierInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('39e050c3-4e74-441a-8d-c0-b8-11-04-df-94-9c')
    @commethod(6)
    def RequestVerificationForWindowAsync(appWindow: win32more.Foundation.HWND, message: win32more.System.WinRT.HSTRING, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IWeakReference(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000037-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Resolve(riid: POINTER(Guid), objectReference: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IWeakReferenceSource(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000038-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetWeakReference(weakReference: POINTER(win32more.System.WinRT.IWeakReference_head)) -> win32more.Foundation.HRESULT: ...
class IWebAuthenticationCoreManagerInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('f4b8e804-811e-4436-b6-9c-44-cb-67-b7-20-84')
    @commethod(6)
    def RequestTokenForWindowAsync(appWindow: win32more.Foundation.HWND, request: win32more.System.WinRT.IInspectable_head, riid: POINTER(Guid), asyncInfo: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def RequestTokenWithWebAccountForWindowAsync(appWindow: win32more.Foundation.HWND, request: win32more.System.WinRT.IInspectable_head, webAccount: win32more.System.WinRT.IInspectable_head, riid: POINTER(Guid), asyncInfo: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PINSPECT_HSTRING_CALLBACK(context: c_void_p, readAddress: UIntPtr, length: UInt32, buffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PINSPECT_HSTRING_CALLBACK2(context: c_void_p, readAddress: UInt64, length: UInt32, buffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PINSPECT_MEMORY_CALLBACK(context: c_void_p, readAddress: UIntPtr, length: UInt32, buffer: c_char_p_no) -> win32more.Foundation.HRESULT: ...
RO_ERROR_REPORTING_FLAGS = UInt32
RO_ERROR_REPORTING_NONE: RO_ERROR_REPORTING_FLAGS = 0
RO_ERROR_REPORTING_SUPPRESSEXCEPTIONS: RO_ERROR_REPORTING_FLAGS = 1
RO_ERROR_REPORTING_FORCEEXCEPTIONS: RO_ERROR_REPORTING_FLAGS = 2
RO_ERROR_REPORTING_USESETERRORINFO: RO_ERROR_REPORTING_FLAGS = 4
RO_ERROR_REPORTING_SUPPRESSSETERRORINFO: RO_ERROR_REPORTING_FLAGS = 8
RO_INIT_TYPE = Int32
RO_INIT_SINGLETHREADED: RO_INIT_TYPE = 0
RO_INIT_MULTITHREADED: RO_INIT_TYPE = 1
ROPARAMIIDHANDLE = IntPtr
class ServerInformation(Structure):
    dwServerPid: UInt32
    dwServerTid: UInt32
    ui64ServerAddress: UInt64
TrustLevel = Int32
TrustLevel_BaseTrust: TrustLevel = 0
TrustLevel_PartialTrust: TrustLevel = 1
TrustLevel_FullTrust: TrustLevel = 2
make_head(_module, '_RO_REGISTRATION_COOKIE')
make_head(_module, 'DispatcherQueueOptions')
make_head(_module, 'EventRegistrationToken')
make_head(_module, 'HSTRING_HEADER')
make_head(_module, 'IAccountsSettingsPaneInterop')
make_head(_module, 'IActivationFactory')
make_head(_module, 'IAgileReference')
make_head(_module, 'IApartmentShutdown')
make_head(_module, 'IAppServiceConnectionExtendedExecution')
make_head(_module, 'IBufferByteAccess')
make_head(_module, 'ICastingController')
make_head(_module, 'ICastingEventHandler')
make_head(_module, 'ICastingSourceInfo')
make_head(_module, 'ICoreInputInterop')
make_head(_module, 'ICoreWindowAdapterInterop')
make_head(_module, 'ICoreWindowComponentInterop')
make_head(_module, 'ICoreWindowInterop')
make_head(_module, 'ICorrelationVectorInformation')
make_head(_module, 'ICorrelationVectorSource')
make_head(_module, 'IDragDropManagerInterop')
make_head(_module, 'IHolographicSpaceInterop')
make_head(_module, 'IInputPaneInterop')
make_head(_module, 'IInspectable')
make_head(_module, 'ILanguageExceptionErrorInfo')
make_head(_module, 'ILanguageExceptionErrorInfo2')
make_head(_module, 'ILanguageExceptionStackBackTrace')
make_head(_module, 'ILanguageExceptionTransform')
make_head(_module, 'IMemoryBufferByteAccess')
make_head(_module, 'IMessageDispatcher')
make_head(_module, 'IPlayToManagerInterop')
make_head(_module, 'IRestrictedErrorInfo')
make_head(_module, 'IRoMetaDataLocator')
make_head(_module, 'IRoSimpleMetaDataBuilder')
make_head(_module, 'IShareWindowCommandEventArgsInterop')
make_head(_module, 'IShareWindowCommandSourceInterop')
make_head(_module, 'ISpatialInteractionManagerInterop')
make_head(_module, 'ISystemMediaTransportControlsInterop')
make_head(_module, 'IUIViewSettingsInterop')
make_head(_module, 'IUserActivityInterop')
make_head(_module, 'IUserActivityRequestManagerInterop')
make_head(_module, 'IUserActivitySourceHostInterop')
make_head(_module, 'IUserConsentVerifierInterop')
make_head(_module, 'IWeakReference')
make_head(_module, 'IWeakReferenceSource')
make_head(_module, 'IWebAuthenticationCoreManagerInterop')
make_head(_module, 'PINSPECT_HSTRING_CALLBACK')
make_head(_module, 'PINSPECT_HSTRING_CALLBACK2')
make_head(_module, 'PINSPECT_MEMORY_CALLBACK')
make_head(_module, 'ServerInformation')
__all__ = [
    "ACTIVATIONTYPE",
    "ACTIVATIONTYPE_FROM_DATA",
    "ACTIVATIONTYPE_FROM_FILE",
    "ACTIVATIONTYPE_FROM_MONIKER",
    "ACTIVATIONTYPE_FROM_STORAGE",
    "ACTIVATIONTYPE_FROM_STREAM",
    "ACTIVATIONTYPE_UNCATEGORIZED",
    "AGILEREFERENCE_DEFAULT",
    "AGILEREFERENCE_DELAYEDMARSHAL",
    "APARTMENT_SHUTDOWN_REGISTRATION_COOKIE",
    "AgileReferenceOptions",
    "BSOS_DEFAULT",
    "BSOS_OPTIONS",
    "BSOS_PREFERDESTINATIONSTREAM",
    "CASTING_CONNECTION_ERROR_STATUS",
    "CASTING_CONNECTION_ERROR_STATUS_DEVICE_DID_NOT_RESPOND",
    "CASTING_CONNECTION_ERROR_STATUS_DEVICE_ERROR",
    "CASTING_CONNECTION_ERROR_STATUS_DEVICE_LOCKED",
    "CASTING_CONNECTION_ERROR_STATUS_INVALID_CASTING_SOURCE",
    "CASTING_CONNECTION_ERROR_STATUS_PROTECTED_PLAYBACK_FAILED",
    "CASTING_CONNECTION_ERROR_STATUS_SUCCEEDED",
    "CASTING_CONNECTION_ERROR_STATUS_UNKNOWN",
    "CASTING_CONNECTION_STATE",
    "CASTING_CONNECTION_STATE_CONNECTED",
    "CASTING_CONNECTION_STATE_CONNECTING",
    "CASTING_CONNECTION_STATE_DISCONNECTED",
    "CASTING_CONNECTION_STATE_DISCONNECTING",
    "CASTING_CONNECTION_STATE_RENDERING",
    "CastingSourceInfo_Property_CastingTypes",
    "CastingSourceInfo_Property_PreferredSourceUriScheme",
    "CastingSourceInfo_Property_ProtectedMedia",
    "CoDecodeProxy",
    "CreateControlInput",
    "CreateControlInputEx",
    "CreateDispatcherQueueController",
    "CreateRandomAccessStreamOnFile",
    "CreateRandomAccessStreamOverStream",
    "CreateStreamOverRandomAccessStream",
    "DISPATCHERQUEUE_THREAD_APARTMENTTYPE",
    "DISPATCHERQUEUE_THREAD_TYPE",
    "DQTAT_COM_ASTA",
    "DQTAT_COM_NONE",
    "DQTAT_COM_STA",
    "DQTYPE_THREAD_CURRENT",
    "DQTYPE_THREAD_DEDICATED",
    "DispatcherQueueOptions",
    "EventRegistrationToken",
    "GetRestrictedErrorInfo",
    "HSTRING",
    "HSTRING_BUFFER",
    "HSTRING_HEADER",
    "HSTRING_UserFree",
    "HSTRING_UserFree64",
    "HSTRING_UserMarshal",
    "HSTRING_UserMarshal64",
    "HSTRING_UserSize",
    "HSTRING_UserSize64",
    "HSTRING_UserUnmarshal",
    "HSTRING_UserUnmarshal64",
    "IAccountsSettingsPaneInterop",
    "IActivationFactory",
    "IAgileReference",
    "IApartmentShutdown",
    "IAppServiceConnectionExtendedExecution",
    "IBufferByteAccess",
    "ICastingController",
    "ICastingEventHandler",
    "ICastingSourceInfo",
    "ICoreInputInterop",
    "ICoreWindowAdapterInterop",
    "ICoreWindowComponentInterop",
    "ICoreWindowInterop",
    "ICorrelationVectorInformation",
    "ICorrelationVectorSource",
    "IDragDropManagerInterop",
    "IHolographicSpaceInterop",
    "IInputPaneInterop",
    "IInspectable",
    "ILanguageExceptionErrorInfo",
    "ILanguageExceptionErrorInfo2",
    "ILanguageExceptionStackBackTrace",
    "ILanguageExceptionTransform",
    "IMemoryBufferByteAccess",
    "IMessageDispatcher",
    "IPlayToManagerInterop",
    "IRestrictedErrorInfo",
    "IRoMetaDataLocator",
    "IRoSimpleMetaDataBuilder",
    "IShareWindowCommandEventArgsInterop",
    "IShareWindowCommandSourceInterop",
    "ISpatialInteractionManagerInterop",
    "ISystemMediaTransportControlsInterop",
    "IUIViewSettingsInterop",
    "IUserActivityInterop",
    "IUserActivityRequestManagerInterop",
    "IUserActivitySourceHostInterop",
    "IUserConsentVerifierInterop",
    "IWeakReference",
    "IWeakReferenceSource",
    "IWebAuthenticationCoreManagerInterop",
    "IsErrorPropagationEnabled",
    "MAX_ERROR_MESSAGE_CHARS",
    "MetaDataGetDispenser",
    "PINSPECT_HSTRING_CALLBACK",
    "PINSPECT_HSTRING_CALLBACK2",
    "PINSPECT_MEMORY_CALLBACK",
    "ROPARAMIIDHANDLE",
    "RO_ERROR_REPORTING_FLAGS",
    "RO_ERROR_REPORTING_FORCEEXCEPTIONS",
    "RO_ERROR_REPORTING_NONE",
    "RO_ERROR_REPORTING_SUPPRESSEXCEPTIONS",
    "RO_ERROR_REPORTING_SUPPRESSSETERRORINFO",
    "RO_ERROR_REPORTING_USESETERRORINFO",
    "RO_INIT_MULTITHREADED",
    "RO_INIT_SINGLETHREADED",
    "RO_INIT_TYPE",
    "RoActivateInstance",
    "RoCaptureErrorContext",
    "RoClearError",
    "RoFailFastWithErrorContext",
    "RoFreeParameterizedTypeExtra",
    "RoGetActivationFactory",
    "RoGetAgileReference",
    "RoGetApartmentIdentifier",
    "RoGetBufferMarshaler",
    "RoGetErrorReportingFlags",
    "RoGetMatchingRestrictedErrorInfo",
    "RoGetParameterizedTypeInstanceIID",
    "RoGetServerActivatableClasses",
    "RoInitialize",
    "RoInspectCapturedStackBackTrace",
    "RoInspectThreadErrorInfo",
    "RoOriginateError",
    "RoOriginateErrorW",
    "RoOriginateLanguageException",
    "RoParameterizedTypeExtraGetTypeSignature",
    "RoRegisterActivationFactories",
    "RoRegisterForApartmentShutdown",
    "RoReportFailedDelegate",
    "RoReportUnhandledError",
    "RoResolveRestrictedErrorInfoReference",
    "RoRevokeActivationFactories",
    "RoSetErrorReportingFlags",
    "RoTransformError",
    "RoTransformErrorW",
    "RoUninitialize",
    "RoUnregisterForApartmentShutdown",
    "ServerInformation",
    "SetRestrictedErrorInfo",
    "TrustLevel",
    "TrustLevel_BaseTrust",
    "TrustLevel_FullTrust",
    "TrustLevel_PartialTrust",
    "WindowsCompareStringOrdinal",
    "WindowsConcatString",
    "WindowsCreateString",
    "WindowsCreateStringReference",
    "WindowsDeleteString",
    "WindowsDeleteStringBuffer",
    "WindowsDuplicateString",
    "WindowsGetStringLen",
    "WindowsGetStringRawBuffer",
    "WindowsInspectString",
    "WindowsInspectString2",
    "WindowsIsStringEmpty",
    "WindowsPreallocateStringBuffer",
    "WindowsPromoteStringBuffer",
    "WindowsReplaceString",
    "WindowsStringHasEmbeddedNull",
    "WindowsSubstring",
    "WindowsSubstringWithSpecifiedLength",
    "WindowsTrimStringEnd",
    "WindowsTrimStringStart",
    "_RO_REGISTRATION_COOKIE",
]
_arch_optional = [
]
