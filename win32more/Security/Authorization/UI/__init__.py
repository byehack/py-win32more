from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security
import win32more.Security.Authorization
import win32more.Security.Authorization.UI
import win32more.System.Com
import win32more.UI.Controls
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
SI_EDIT_PERMS: Int32 = 0
SI_EDIT_OWNER: Int32 = 1
SI_CONTAINER: Int32 = 4
SI_READONLY: Int32 = 8
SI_RESET: Int32 = 32
SI_OWNER_READONLY: Int32 = 64
SI_OWNER_RECURSE: Int32 = 256
SI_NO_ACL_PROTECT: Int32 = 512
SI_NO_TREE_APPLY: Int32 = 1024
SI_PAGE_TITLE: Int32 = 2048
SI_SERVER_IS_DC: Int32 = 4096
SI_RESET_DACL_TREE: Int32 = 16384
SI_RESET_SACL_TREE: Int32 = 32768
SI_OBJECT_GUID: Int32 = 65536
SI_ACCESS_SPECIFIC: Int32 = 65536
SI_ACCESS_GENERAL: Int32 = 131072
SI_ACCESS_CONTAINER: Int32 = 262144
SI_ACCESS_PROPERTY: Int32 = 524288
DOBJ_RES_CONT: Int32 = 1
DOBJ_RES_ROOT: Int32 = 2
DOBJ_VOL_NTACLS: Int32 = 4
DOBJ_COND_NTACLS: Int32 = 8
DOBJ_RIBBON_LAUNCH: Int32 = 16
CFSTR_ACLUI_SID_INFO_LIST: String = 'CFSTR_ACLUI_SID_INFO_LIST'
SECURITY_OBJECT_ID_OBJECT_SD: UInt32 = 1
SECURITY_OBJECT_ID_SHARE: UInt32 = 2
SECURITY_OBJECT_ID_CENTRAL_POLICY: UInt32 = 3
SECURITY_OBJECT_ID_CENTRAL_ACCESS_RULE: UInt32 = 4
@winfunctype('ACLUI.dll')
def CreateSecurityPage(psi: win32more.Security.Authorization.UI.ISecurityInformation_head) -> win32more.UI.Controls.HPROPSHEETPAGE: ...
@winfunctype('ACLUI.dll')
def EditSecurity(hwndOwner: win32more.Foundation.HWND, psi: win32more.Security.Authorization.UI.ISecurityInformation_head) -> win32more.Foundation.BOOL: ...
@winfunctype('ACLUI.dll')
def EditSecurityAdvanced(hwndOwner: win32more.Foundation.HWND, psi: win32more.Security.Authorization.UI.ISecurityInformation_head, uSIPage: win32more.Security.Authorization.UI.SI_PAGE_TYPE) -> win32more.Foundation.HRESULT: ...
class EFFPERM_RESULT_LIST(Structure):
    fEvaluated: win32more.Foundation.BOOLEAN
    cObjectTypeListLength: UInt32
    pObjectTypeList: POINTER(win32more.Security.OBJECT_TYPE_LIST_head)
    pGrantedAccessList: POINTER(UInt32)
class IEffectivePermission(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3853dc76-9f35-407c-88-a1-d1-93-44-36-5f-bc')
    @commethod(3)
    def GetEffectivePermission(pguidObjectType: POINTER(Guid), pUserSid: win32more.Foundation.PSID, pszServerName: win32more.Foundation.PWSTR, pSD: win32more.Security.PSECURITY_DESCRIPTOR, ppObjectTypeList: POINTER(POINTER(win32more.Security.OBJECT_TYPE_LIST_head)), pcObjectTypeListLength: POINTER(UInt32), ppGrantedAccessList: POINTER(POINTER(UInt32)), pcGrantedAccessListLength: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IEffectivePermission2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('941fabca-dd47-4fca-90-bb-b0-e1-02-55-f2-0d')
    @commethod(3)
    def ComputeEffectivePermissionWithSecondarySecurity(pSid: win32more.Foundation.PSID, pDeviceSid: win32more.Foundation.PSID, pszServerName: win32more.Foundation.PWSTR, pSecurityObjects: POINTER(win32more.Security.Authorization.UI.SECURITY_OBJECT_head), dwSecurityObjectCount: UInt32, pUserGroups: POINTER(win32more.Security.TOKEN_GROUPS_head), pAuthzUserGroupsOperations: POINTER(win32more.Security.Authorization.AUTHZ_SID_OPERATION), pDeviceGroups: POINTER(win32more.Security.TOKEN_GROUPS_head), pAuthzDeviceGroupsOperations: POINTER(win32more.Security.Authorization.AUTHZ_SID_OPERATION), pAuthzUserClaims: POINTER(win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_head), pAuthzUserClaimsOperations: POINTER(win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION), pAuthzDeviceClaims: POINTER(win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTES_INFORMATION_head), pAuthzDeviceClaimsOperations: POINTER(win32more.Security.Authorization.AUTHZ_SECURITY_ATTRIBUTE_OPERATION), pEffpermResultLists: POINTER(win32more.Security.Authorization.UI.EFFPERM_RESULT_LIST_head)) -> win32more.Foundation.HRESULT: ...
class ISecurityInformation(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('965fc360-16ff-11d0-91-cb-00-aa-00-bb-b7-23')
    @commethod(3)
    def GetObjectInformation(pObjectInfo: POINTER(win32more.Security.Authorization.UI.SI_OBJECT_INFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSecurity(RequestedInformation: win32more.Security.OBJECT_SECURITY_INFORMATION, ppSecurityDescriptor: POINTER(win32more.Security.PSECURITY_DESCRIPTOR), fDefault: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetSecurity(SecurityInformation: win32more.Security.OBJECT_SECURITY_INFORMATION, pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetAccessRights(pguidObjectType: POINTER(Guid), dwFlags: win32more.Security.Authorization.UI.SECURITY_INFO_PAGE_FLAGS, ppAccess: POINTER(POINTER(win32more.Security.Authorization.UI.SI_ACCESS_head)), pcAccesses: POINTER(UInt32), piDefaultAccess: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def MapGeneric(pguidObjectType: POINTER(Guid), pAceFlags: c_char_p_no, pMask: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetInheritTypes(ppInheritTypes: POINTER(POINTER(win32more.Security.Authorization.UI.SI_INHERIT_TYPE_head)), pcInheritTypes: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def PropertySheetPageCallback(hwnd: win32more.Foundation.HWND, uMsg: win32more.UI.Controls.PSPCB_MESSAGE, uPage: win32more.Security.Authorization.UI.SI_PAGE_TYPE) -> win32more.Foundation.HRESULT: ...
class ISecurityInformation2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c3ccfdb4-6f88-11d2-a3-ce-00-c0-4f-b1-78-2a')
    @commethod(3)
    def IsDaclCanonical(pDacl: POINTER(win32more.Security.ACL_head)) -> win32more.Foundation.BOOL: ...
    @commethod(4)
    def LookupSids(cSids: UInt32, rgpSids: POINTER(win32more.Foundation.PSID), ppdo: POINTER(win32more.System.Com.IDataObject_head)) -> win32more.Foundation.HRESULT: ...
class ISecurityInformation3(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e2cdc9cc-31bd-4f8f-8c-8b-b6-41-af-51-6a-1a')
    @commethod(3)
    def GetFullResourceName(ppszResourceName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OpenElevatedEditor(hWnd: win32more.Foundation.HWND, uPage: win32more.Security.Authorization.UI.SI_PAGE_TYPE) -> win32more.Foundation.HRESULT: ...
class ISecurityInformation4(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ea961070-cd14-4621-ac-e4-f6-3c-03-e5-83-e4')
    @commethod(3)
    def GetSecondarySecurity(pSecurityObjects: POINTER(POINTER(win32more.Security.Authorization.UI.SECURITY_OBJECT_head)), pSecurityObjectCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ISecurityObjectTypeInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fc3066eb-79ef-444b-91-11-d1-8a-75-eb-f2-fa')
    @commethod(3)
    def GetInheritSource(si: UInt32, pACL: POINTER(win32more.Security.ACL_head), ppInheritArray: POINTER(POINTER(win32more.Security.Authorization.INHERITED_FROMA_head))) -> win32more.Foundation.HRESULT: ...
SECURITY_INFO_PAGE_FLAGS = UInt32
SI_ADVANCED: SECURITY_INFO_PAGE_FLAGS = 16
SI_EDIT_AUDITS: SECURITY_INFO_PAGE_FLAGS = 2
SI_EDIT_PROPERTIES: SECURITY_INFO_PAGE_FLAGS = 128
class SECURITY_OBJECT(Structure):
    pwszName: win32more.Foundation.PWSTR
    pData: c_void_p
    cbData: UInt32
    pData2: c_void_p
    cbData2: UInt32
    Id: UInt32
    fWellKnown: win32more.Foundation.BOOLEAN
class SI_ACCESS(Structure):
    pguid: POINTER(Guid)
    mask: UInt32
    pszName: win32more.Foundation.PWSTR
    dwFlags: UInt32
class SI_INHERIT_TYPE(Structure):
    pguid: POINTER(Guid)
    dwFlags: win32more.Security.ACE_FLAGS
    pszName: win32more.Foundation.PWSTR
class SI_OBJECT_INFO(Structure):
    dwFlags: win32more.Security.Authorization.UI.SI_OBJECT_INFO_FLAGS
    hInstance: win32more.Foundation.HINSTANCE
    pszServerName: win32more.Foundation.PWSTR
    pszObjectName: win32more.Foundation.PWSTR
    pszPageTitle: win32more.Foundation.PWSTR
    guidObjectType: Guid
SI_OBJECT_INFO_FLAGS = UInt32
SI_AUDITS_ELEVATION_REQUIRED: SI_OBJECT_INFO_FLAGS = 33554432
SI_DISABLE_DENY_ACE: SI_OBJECT_INFO_FLAGS = 2147483648
SI_EDIT_EFFECTIVE: SI_OBJECT_INFO_FLAGS = 131072
SI_ENABLE_CENTRAL_POLICY: SI_OBJECT_INFO_FLAGS = 1073741824
SI_ENABLE_EDIT_ATTRIBUTE_CONDITION: SI_OBJECT_INFO_FLAGS = 536870912
SI_MAY_WRITE: SI_OBJECT_INFO_FLAGS = 268435456
SI_NO_ADDITIONAL_PERMISSION: SI_OBJECT_INFO_FLAGS = 2097152
SI_OWNER_ELEVATION_REQUIRED: SI_OBJECT_INFO_FLAGS = 67108864
SI_PERMS_ELEVATION_REQUIRED: SI_OBJECT_INFO_FLAGS = 16777216
SI_RESET_DACL: SI_OBJECT_INFO_FLAGS = 262144
SI_RESET_OWNER: SI_OBJECT_INFO_FLAGS = 1048576
SI_RESET_SACL: SI_OBJECT_INFO_FLAGS = 524288
SI_SCOPE_ELEVATION_REQUIRED: SI_OBJECT_INFO_FLAGS = 134217728
SI_VIEW_ONLY: SI_OBJECT_INFO_FLAGS = 4194304
SI_PAGE_ACTIVATED = Int32
SI_SHOW_DEFAULT: SI_PAGE_ACTIVATED = 0
SI_SHOW_PERM_ACTIVATED: SI_PAGE_ACTIVATED = 1
SI_SHOW_AUDIT_ACTIVATED: SI_PAGE_ACTIVATED = 2
SI_SHOW_OWNER_ACTIVATED: SI_PAGE_ACTIVATED = 3
SI_SHOW_EFFECTIVE_ACTIVATED: SI_PAGE_ACTIVATED = 4
SI_SHOW_SHARE_ACTIVATED: SI_PAGE_ACTIVATED = 5
SI_SHOW_CENTRAL_POLICY_ACTIVATED: SI_PAGE_ACTIVATED = 6
SI_PAGE_TYPE = Int32
SI_PAGE_PERM: SI_PAGE_TYPE = 0
SI_PAGE_ADVPERM: SI_PAGE_TYPE = 1
SI_PAGE_AUDIT: SI_PAGE_TYPE = 2
SI_PAGE_OWNER: SI_PAGE_TYPE = 3
SI_PAGE_EFFECTIVE: SI_PAGE_TYPE = 4
SI_PAGE_TAKEOWNERSHIP: SI_PAGE_TYPE = 5
SI_PAGE_SHARE: SI_PAGE_TYPE = 6
class SID_INFO(Structure):
    pSid: win32more.Foundation.PSID
    pwzCommonName: win32more.Foundation.PWSTR
    pwzClass: win32more.Foundation.PWSTR
    pwzUPN: win32more.Foundation.PWSTR
class SID_INFO_LIST(Structure):
    cItems: UInt32
    aSidInfo: win32more.Security.Authorization.UI.SID_INFO * 1
make_head(_module, 'EFFPERM_RESULT_LIST')
make_head(_module, 'IEffectivePermission')
make_head(_module, 'IEffectivePermission2')
make_head(_module, 'ISecurityInformation')
make_head(_module, 'ISecurityInformation2')
make_head(_module, 'ISecurityInformation3')
make_head(_module, 'ISecurityInformation4')
make_head(_module, 'ISecurityObjectTypeInfo')
make_head(_module, 'SECURITY_OBJECT')
make_head(_module, 'SI_ACCESS')
make_head(_module, 'SI_INHERIT_TYPE')
make_head(_module, 'SI_OBJECT_INFO')
make_head(_module, 'SID_INFO')
make_head(_module, 'SID_INFO_LIST')
__all__ = [
    "CFSTR_ACLUI_SID_INFO_LIST",
    "CreateSecurityPage",
    "DOBJ_COND_NTACLS",
    "DOBJ_RES_CONT",
    "DOBJ_RES_ROOT",
    "DOBJ_RIBBON_LAUNCH",
    "DOBJ_VOL_NTACLS",
    "EFFPERM_RESULT_LIST",
    "EditSecurity",
    "EditSecurityAdvanced",
    "IEffectivePermission",
    "IEffectivePermission2",
    "ISecurityInformation",
    "ISecurityInformation2",
    "ISecurityInformation3",
    "ISecurityInformation4",
    "ISecurityObjectTypeInfo",
    "SECURITY_INFO_PAGE_FLAGS",
    "SECURITY_OBJECT",
    "SECURITY_OBJECT_ID_CENTRAL_ACCESS_RULE",
    "SECURITY_OBJECT_ID_CENTRAL_POLICY",
    "SECURITY_OBJECT_ID_OBJECT_SD",
    "SECURITY_OBJECT_ID_SHARE",
    "SID_INFO",
    "SID_INFO_LIST",
    "SI_ACCESS",
    "SI_ACCESS_CONTAINER",
    "SI_ACCESS_GENERAL",
    "SI_ACCESS_PROPERTY",
    "SI_ACCESS_SPECIFIC",
    "SI_ADVANCED",
    "SI_AUDITS_ELEVATION_REQUIRED",
    "SI_CONTAINER",
    "SI_DISABLE_DENY_ACE",
    "SI_EDIT_AUDITS",
    "SI_EDIT_EFFECTIVE",
    "SI_EDIT_OWNER",
    "SI_EDIT_PERMS",
    "SI_EDIT_PROPERTIES",
    "SI_ENABLE_CENTRAL_POLICY",
    "SI_ENABLE_EDIT_ATTRIBUTE_CONDITION",
    "SI_INHERIT_TYPE",
    "SI_MAY_WRITE",
    "SI_NO_ACL_PROTECT",
    "SI_NO_ADDITIONAL_PERMISSION",
    "SI_NO_TREE_APPLY",
    "SI_OBJECT_GUID",
    "SI_OBJECT_INFO",
    "SI_OBJECT_INFO_FLAGS",
    "SI_OWNER_ELEVATION_REQUIRED",
    "SI_OWNER_READONLY",
    "SI_OWNER_RECURSE",
    "SI_PAGE_ACTIVATED",
    "SI_PAGE_ADVPERM",
    "SI_PAGE_AUDIT",
    "SI_PAGE_EFFECTIVE",
    "SI_PAGE_OWNER",
    "SI_PAGE_PERM",
    "SI_PAGE_SHARE",
    "SI_PAGE_TAKEOWNERSHIP",
    "SI_PAGE_TITLE",
    "SI_PAGE_TYPE",
    "SI_PERMS_ELEVATION_REQUIRED",
    "SI_READONLY",
    "SI_RESET",
    "SI_RESET_DACL",
    "SI_RESET_DACL_TREE",
    "SI_RESET_OWNER",
    "SI_RESET_SACL",
    "SI_RESET_SACL_TREE",
    "SI_SCOPE_ELEVATION_REQUIRED",
    "SI_SERVER_IS_DC",
    "SI_SHOW_AUDIT_ACTIVATED",
    "SI_SHOW_CENTRAL_POLICY_ACTIVATED",
    "SI_SHOW_DEFAULT",
    "SI_SHOW_EFFECTIVE_ACTIVATED",
    "SI_SHOW_OWNER_ACTIVATED",
    "SI_SHOW_PERM_ACTIVATED",
    "SI_SHOW_SHARE_ACTIVATED",
    "SI_VIEW_ONLY",
]
_arch_optional = [
]
