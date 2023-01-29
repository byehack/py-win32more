from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Devices.AllJoyn
import win32more.Foundation
import win32more.Security
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
class _alljoyn_abouticon_handle(Structure):
    pass
class _alljoyn_abouticonobj_handle(Structure):
    pass
class _alljoyn_abouticonproxy_handle(Structure):
    pass
@winfunctype_pointer
def alljoyn_about_announced_ptr(context: c_void_p, busName: win32more.Foundation.PSTR, version: UInt16, port: UInt16, objectDescriptionArg: win32more.Devices.AllJoyn.alljoyn_msgarg, aboutDataArg: win32more.Devices.AllJoyn.alljoyn_msgarg) -> Void: ...
alljoyn_about_announceflag = Int32
UNANNOUNCED: alljoyn_about_announceflag = 0
ANNOUNCED: alljoyn_about_announceflag = 1
alljoyn_aboutdata = IntPtr
alljoyn_aboutdatalistener = IntPtr
class alljoyn_aboutdatalistener_callbacks(Structure):
    about_datalistener_getaboutdata: win32more.Devices.AllJoyn.alljoyn_aboutdatalistener_getaboutdata_ptr
    about_datalistener_getannouncedaboutdata: win32more.Devices.AllJoyn.alljoyn_aboutdatalistener_getannouncedaboutdata_ptr
@winfunctype_pointer
def alljoyn_aboutdatalistener_getaboutdata_ptr(context: c_void_p, msgArg: win32more.Devices.AllJoyn.alljoyn_msgarg, language: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype_pointer
def alljoyn_aboutdatalistener_getannouncedaboutdata_ptr(context: c_void_p, msgArg: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.QStatus: ...
alljoyn_aboutlistener = IntPtr
class alljoyn_aboutlistener_callback(Structure):
    about_listener_announced: win32more.Devices.AllJoyn.alljoyn_about_announced_ptr
alljoyn_aboutobj = IntPtr
alljoyn_aboutobjectdescription = IntPtr
alljoyn_aboutproxy = IntPtr
alljoyn_applicationstate = Int32
NOT_CLAIMABLE: alljoyn_applicationstate = 0
CLAIMABLE: alljoyn_applicationstate = 1
CLAIMED: alljoyn_applicationstate = 2
NEED_UPDATE: alljoyn_applicationstate = 3
alljoyn_applicationstatelistener = IntPtr
class alljoyn_applicationstatelistener_callbacks(Structure):
    state: win32more.Devices.AllJoyn.alljoyn_applicationstatelistener_state_ptr
@winfunctype_pointer
def alljoyn_applicationstatelistener_state_ptr(busName: POINTER(SByte), publicKey: POINTER(SByte), applicationState: win32more.Devices.AllJoyn.alljoyn_applicationstate, context: c_void_p) -> Void: ...
alljoyn_authlistener = IntPtr
@winfunctype_pointer
def alljoyn_authlistener_authenticationcomplete_ptr(context: c_void_p, authMechanism: win32more.Foundation.PSTR, peerName: win32more.Foundation.PSTR, success: Int32) -> Void: ...
class alljoyn_authlistener_callbacks(Structure):
    request_credentials: win32more.Devices.AllJoyn.alljoyn_authlistener_requestcredentials_ptr
    verify_credentials: win32more.Devices.AllJoyn.alljoyn_authlistener_verifycredentials_ptr
    security_violation: win32more.Devices.AllJoyn.alljoyn_authlistener_securityviolation_ptr
    authentication_complete: win32more.Devices.AllJoyn.alljoyn_authlistener_authenticationcomplete_ptr
@winfunctype_pointer
def alljoyn_authlistener_requestcredentials_ptr(context: c_void_p, authMechanism: win32more.Foundation.PSTR, peerName: win32more.Foundation.PSTR, authCount: UInt16, userName: win32more.Foundation.PSTR, credMask: UInt16, credentials: win32more.Devices.AllJoyn.alljoyn_credentials) -> Int32: ...
@winfunctype_pointer
def alljoyn_authlistener_requestcredentialsasync_ptr(context: c_void_p, listener: win32more.Devices.AllJoyn.alljoyn_authlistener, authMechanism: win32more.Foundation.PSTR, peerName: win32more.Foundation.PSTR, authCount: UInt16, userName: win32more.Foundation.PSTR, credMask: UInt16, authContext: c_void_p) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype_pointer
def alljoyn_authlistener_securityviolation_ptr(context: c_void_p, status: win32more.Devices.AllJoyn.QStatus, msg: win32more.Devices.AllJoyn.alljoyn_message) -> Void: ...
@winfunctype_pointer
def alljoyn_authlistener_verifycredentials_ptr(context: c_void_p, authMechanism: win32more.Foundation.PSTR, peerName: win32more.Foundation.PSTR, credentials: win32more.Devices.AllJoyn.alljoyn_credentials) -> Int32: ...
@winfunctype_pointer
def alljoyn_authlistener_verifycredentialsasync_ptr(context: c_void_p, listener: win32more.Devices.AllJoyn.alljoyn_authlistener, authMechanism: win32more.Foundation.PSTR, peerName: win32more.Foundation.PSTR, credentials: win32more.Devices.AllJoyn.alljoyn_credentials, authContext: c_void_p) -> win32more.Devices.AllJoyn.QStatus: ...
class alljoyn_authlistenerasync_callbacks(Structure):
    request_credentials: win32more.Devices.AllJoyn.alljoyn_authlistener_requestcredentialsasync_ptr
    verify_credentials: win32more.Devices.AllJoyn.alljoyn_authlistener_verifycredentialsasync_ptr
    security_violation: win32more.Devices.AllJoyn.alljoyn_authlistener_securityviolation_ptr
    authentication_complete: win32more.Devices.AllJoyn.alljoyn_authlistener_authenticationcomplete_ptr
alljoyn_autopinger = IntPtr
@winfunctype_pointer
def alljoyn_autopinger_destination_found_ptr(context: c_void_p, group: win32more.Foundation.PSTR, destination: win32more.Foundation.PSTR) -> Void: ...
@winfunctype_pointer
def alljoyn_autopinger_destination_lost_ptr(context: c_void_p, group: win32more.Foundation.PSTR, destination: win32more.Foundation.PSTR) -> Void: ...
alljoyn_busattachment = IntPtr
@winfunctype_pointer
def alljoyn_busattachment_joinsessioncb_ptr(status: win32more.Devices.AllJoyn.QStatus, sessionId: UInt32, opts: win32more.Devices.AllJoyn.alljoyn_sessionopts, context: c_void_p) -> Void: ...
@winfunctype_pointer
def alljoyn_busattachment_setlinktimeoutcb_ptr(status: win32more.Devices.AllJoyn.QStatus, timeout: UInt32, context: c_void_p) -> Void: ...
alljoyn_buslistener = IntPtr
@winfunctype_pointer
def alljoyn_buslistener_bus_disconnected_ptr(context: c_void_p) -> Void: ...
@winfunctype_pointer
def alljoyn_buslistener_bus_prop_changed_ptr(context: c_void_p, prop_name: win32more.Foundation.PSTR, prop_value: win32more.Devices.AllJoyn.alljoyn_msgarg) -> Void: ...
@winfunctype_pointer
def alljoyn_buslistener_bus_stopping_ptr(context: c_void_p) -> Void: ...
class alljoyn_buslistener_callbacks(Structure):
    listener_registered: win32more.Devices.AllJoyn.alljoyn_buslistener_listener_registered_ptr
    listener_unregistered: win32more.Devices.AllJoyn.alljoyn_buslistener_listener_unregistered_ptr
    found_advertised_name: win32more.Devices.AllJoyn.alljoyn_buslistener_found_advertised_name_ptr
    lost_advertised_name: win32more.Devices.AllJoyn.alljoyn_buslistener_lost_advertised_name_ptr
    name_owner_changed: win32more.Devices.AllJoyn.alljoyn_buslistener_name_owner_changed_ptr
    bus_stopping: win32more.Devices.AllJoyn.alljoyn_buslistener_bus_stopping_ptr
    bus_disconnected: win32more.Devices.AllJoyn.alljoyn_buslistener_bus_disconnected_ptr
    property_changed: win32more.Devices.AllJoyn.alljoyn_buslistener_bus_prop_changed_ptr
@winfunctype_pointer
def alljoyn_buslistener_found_advertised_name_ptr(context: c_void_p, name: win32more.Foundation.PSTR, transport: UInt16, namePrefix: win32more.Foundation.PSTR) -> Void: ...
@winfunctype_pointer
def alljoyn_buslistener_listener_registered_ptr(context: c_void_p, bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> Void: ...
@winfunctype_pointer
def alljoyn_buslistener_listener_unregistered_ptr(context: c_void_p) -> Void: ...
@winfunctype_pointer
def alljoyn_buslistener_lost_advertised_name_ptr(context: c_void_p, name: win32more.Foundation.PSTR, transport: UInt16, namePrefix: win32more.Foundation.PSTR) -> Void: ...
@winfunctype_pointer
def alljoyn_buslistener_name_owner_changed_ptr(context: c_void_p, busName: win32more.Foundation.PSTR, previousOwner: win32more.Foundation.PSTR, newOwner: win32more.Foundation.PSTR) -> Void: ...
alljoyn_busobject = IntPtr
class alljoyn_busobject_callbacks(Structure):
    property_get: win32more.Devices.AllJoyn.alljoyn_busobject_prop_get_ptr
    property_set: win32more.Devices.AllJoyn.alljoyn_busobject_prop_set_ptr
    object_registered: win32more.Devices.AllJoyn.alljoyn_busobject_object_registration_ptr
    object_unregistered: win32more.Devices.AllJoyn.alljoyn_busobject_object_registration_ptr
class alljoyn_busobject_methodentry(Structure):
    member: POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_member_head)
    method_handler: win32more.Devices.AllJoyn.alljoyn_messagereceiver_methodhandler_ptr
@winfunctype_pointer
def alljoyn_busobject_object_registration_ptr(context: c_void_p) -> Void: ...
@winfunctype_pointer
def alljoyn_busobject_prop_get_ptr(context: c_void_p, ifcName: win32more.Foundation.PSTR, propName: win32more.Foundation.PSTR, val: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype_pointer
def alljoyn_busobject_prop_set_ptr(context: c_void_p, ifcName: win32more.Foundation.PSTR, propName: win32more.Foundation.PSTR, val: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.QStatus: ...
class alljoyn_certificateid(Structure):
    serial: c_char_p_no
    serialLen: UIntPtr
    issuerPublicKey: POINTER(SByte)
    issuerAki: c_char_p_no
    issuerAkiLen: UIntPtr
class alljoyn_certificateidarray(Structure):
    count: UIntPtr
    ids: POINTER(win32more.Devices.AllJoyn.alljoyn_certificateid_head)
alljoyn_claimcapability_masks = Int32
CAPABLE_ECDHE_NULL: alljoyn_claimcapability_masks = 1
CAPABLE_ECDHE_ECDSA: alljoyn_claimcapability_masks = 4
CAPABLE_ECDHE_SPEKE: alljoyn_claimcapability_masks = 8
alljoyn_claimcapabilityadditionalinfo_masks = Int32
PASSWORD_GENERATED_BY_SECURITY_MANAGER: alljoyn_claimcapabilityadditionalinfo_masks = 1
PASSWORD_GENERATED_BY_APPLICATION: alljoyn_claimcapabilityadditionalinfo_masks = 2
alljoyn_credentials = IntPtr
alljoyn_interfacedescription = IntPtr
class alljoyn_interfacedescription_member(Structure):
    iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription
    memberType: win32more.Devices.AllJoyn.alljoyn_messagetype
    name: win32more.Foundation.PSTR
    signature: win32more.Foundation.PSTR
    returnSignature: win32more.Foundation.PSTR
    argNames: win32more.Foundation.PSTR
    internal_member: c_void_p
class alljoyn_interfacedescription_property(Structure):
    name: win32more.Foundation.PSTR
    signature: win32more.Foundation.PSTR
    access: Byte
    internal_property: c_void_p
alljoyn_interfacedescription_securitypolicy = Int32
AJ_IFC_SECURITY_INHERIT: alljoyn_interfacedescription_securitypolicy = 0
AJ_IFC_SECURITY_REQUIRED: alljoyn_interfacedescription_securitypolicy = 1
AJ_IFC_SECURITY_OFF: alljoyn_interfacedescription_securitypolicy = 2
@winfunctype_pointer
def alljoyn_interfacedescription_translation_callback_ptr(sourceLanguage: win32more.Foundation.PSTR, targetLanguage: win32more.Foundation.PSTR, sourceText: win32more.Foundation.PSTR) -> win32more.Foundation.PSTR: ...
alljoyn_keystore = IntPtr
alljoyn_keystorelistener = IntPtr
@winfunctype_pointer
def alljoyn_keystorelistener_acquireexclusivelock_ptr(context: c_void_p, listener: win32more.Devices.AllJoyn.alljoyn_keystorelistener) -> win32more.Devices.AllJoyn.QStatus: ...
class alljoyn_keystorelistener_callbacks(Structure):
    load_request: win32more.Devices.AllJoyn.alljoyn_keystorelistener_loadrequest_ptr
    store_request: win32more.Devices.AllJoyn.alljoyn_keystorelistener_storerequest_ptr
@winfunctype_pointer
def alljoyn_keystorelistener_loadrequest_ptr(context: c_void_p, listener: win32more.Devices.AllJoyn.alljoyn_keystorelistener, keyStore: win32more.Devices.AllJoyn.alljoyn_keystore) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype_pointer
def alljoyn_keystorelistener_releaseexclusivelock_ptr(context: c_void_p, listener: win32more.Devices.AllJoyn.alljoyn_keystorelistener) -> Void: ...
@winfunctype_pointer
def alljoyn_keystorelistener_storerequest_ptr(context: c_void_p, listener: win32more.Devices.AllJoyn.alljoyn_keystorelistener, keyStore: win32more.Devices.AllJoyn.alljoyn_keystore) -> win32more.Devices.AllJoyn.QStatus: ...
class alljoyn_keystorelistener_with_synchronization_callbacks(Structure):
    load_request: win32more.Devices.AllJoyn.alljoyn_keystorelistener_loadrequest_ptr
    store_request: win32more.Devices.AllJoyn.alljoyn_keystorelistener_storerequest_ptr
    acquire_exclusive_lock: win32more.Devices.AllJoyn.alljoyn_keystorelistener_acquireexclusivelock_ptr
    release_exclusive_lock: win32more.Devices.AllJoyn.alljoyn_keystorelistener_releaseexclusivelock_ptr
class alljoyn_manifestarray(Structure):
    count: UIntPtr
    xmls: POINTER(POINTER(SByte))
alljoyn_message = IntPtr
@winfunctype_pointer
def alljoyn_messagereceiver_methodhandler_ptr(bus: win32more.Devices.AllJoyn.alljoyn_busobject, member: POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_member_head), message: win32more.Devices.AllJoyn.alljoyn_message) -> Void: ...
@winfunctype_pointer
def alljoyn_messagereceiver_replyhandler_ptr(message: win32more.Devices.AllJoyn.alljoyn_message, context: c_void_p) -> Void: ...
@winfunctype_pointer
def alljoyn_messagereceiver_signalhandler_ptr(member: POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_member_head), srcPath: win32more.Foundation.PSTR, message: win32more.Devices.AllJoyn.alljoyn_message) -> Void: ...
alljoyn_messagetype = Int32
ALLJOYN_MESSAGE_INVALID: alljoyn_messagetype = 0
ALLJOYN_MESSAGE_METHOD_CALL: alljoyn_messagetype = 1
ALLJOYN_MESSAGE_METHOD_RET: alljoyn_messagetype = 2
ALLJOYN_MESSAGE_ERROR: alljoyn_messagetype = 3
ALLJOYN_MESSAGE_SIGNAL: alljoyn_messagetype = 4
alljoyn_msgarg = IntPtr
alljoyn_observer = IntPtr
@winfunctype_pointer
def alljoyn_observer_object_discovered_ptr(context: c_void_p, proxyref: win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref) -> Void: ...
@winfunctype_pointer
def alljoyn_observer_object_lost_ptr(context: c_void_p, proxyref: win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref) -> Void: ...
alljoyn_observerlistener = IntPtr
class alljoyn_observerlistener_callback(Structure):
    object_discovered: win32more.Devices.AllJoyn.alljoyn_observer_object_discovered_ptr
    object_lost: win32more.Devices.AllJoyn.alljoyn_observer_object_lost_ptr
alljoyn_permissionconfigurationlistener = IntPtr
class alljoyn_permissionconfigurationlistener_callbacks(Structure):
    factory_reset: win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener_factoryreset_ptr
    policy_changed: win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener_policychanged_ptr
    start_management: win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener_startmanagement_ptr
    end_management: win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener_endmanagement_ptr
@winfunctype_pointer
def alljoyn_permissionconfigurationlistener_endmanagement_ptr(context: c_void_p) -> Void: ...
@winfunctype_pointer
def alljoyn_permissionconfigurationlistener_factoryreset_ptr(context: c_void_p) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype_pointer
def alljoyn_permissionconfigurationlistener_policychanged_ptr(context: c_void_p) -> Void: ...
@winfunctype_pointer
def alljoyn_permissionconfigurationlistener_startmanagement_ptr(context: c_void_p) -> Void: ...
alljoyn_permissionconfigurator = IntPtr
alljoyn_pinglistener = IntPtr
class alljoyn_pinglistener_callback(Structure):
    destination_found: win32more.Devices.AllJoyn.alljoyn_autopinger_destination_found_ptr
    destination_lost: win32more.Devices.AllJoyn.alljoyn_autopinger_destination_lost_ptr
alljoyn_proxybusobject = IntPtr
@winfunctype_pointer
def alljoyn_proxybusobject_listener_getallpropertiescb_ptr(status: win32more.Devices.AllJoyn.QStatus, obj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, values: win32more.Devices.AllJoyn.alljoyn_msgarg, context: c_void_p) -> Void: ...
@winfunctype_pointer
def alljoyn_proxybusobject_listener_getpropertycb_ptr(status: win32more.Devices.AllJoyn.QStatus, obj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, value: win32more.Devices.AllJoyn.alljoyn_msgarg, context: c_void_p) -> Void: ...
@winfunctype_pointer
def alljoyn_proxybusobject_listener_introspectcb_ptr(status: win32more.Devices.AllJoyn.QStatus, obj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, context: c_void_p) -> Void: ...
@winfunctype_pointer
def alljoyn_proxybusobject_listener_propertieschanged_ptr(obj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, ifaceName: win32more.Foundation.PSTR, changed: win32more.Devices.AllJoyn.alljoyn_msgarg, invalidated: win32more.Devices.AllJoyn.alljoyn_msgarg, context: c_void_p) -> Void: ...
@winfunctype_pointer
def alljoyn_proxybusobject_listener_setpropertycb_ptr(status: win32more.Devices.AllJoyn.QStatus, obj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, context: c_void_p) -> Void: ...
alljoyn_proxybusobject_ref = IntPtr
alljoyn_securityapplicationproxy = IntPtr
alljoyn_sessionlistener = IntPtr
class alljoyn_sessionlistener_callbacks(Structure):
    session_lost: win32more.Devices.AllJoyn.alljoyn_sessionlistener_sessionlost_ptr
    session_member_added: win32more.Devices.AllJoyn.alljoyn_sessionlistener_sessionmemberadded_ptr
    session_member_removed: win32more.Devices.AllJoyn.alljoyn_sessionlistener_sessionmemberremoved_ptr
@winfunctype_pointer
def alljoyn_sessionlistener_sessionlost_ptr(context: c_void_p, sessionId: UInt32, reason: win32more.Devices.AllJoyn.alljoyn_sessionlostreason) -> Void: ...
@winfunctype_pointer
def alljoyn_sessionlistener_sessionmemberadded_ptr(context: c_void_p, sessionId: UInt32, uniqueName: win32more.Foundation.PSTR) -> Void: ...
@winfunctype_pointer
def alljoyn_sessionlistener_sessionmemberremoved_ptr(context: c_void_p, sessionId: UInt32, uniqueName: win32more.Foundation.PSTR) -> Void: ...
alljoyn_sessionlostreason = Int32
ALLJOYN_SESSIONLOST_INVALID: alljoyn_sessionlostreason = 0
ALLJOYN_SESSIONLOST_REMOTE_END_LEFT_SESSION: alljoyn_sessionlostreason = 1
ALLJOYN_SESSIONLOST_REMOTE_END_CLOSED_ABRUPTLY: alljoyn_sessionlostreason = 2
ALLJOYN_SESSIONLOST_REMOVED_BY_BINDER: alljoyn_sessionlostreason = 3
ALLJOYN_SESSIONLOST_LINK_TIMEOUT: alljoyn_sessionlostreason = 4
ALLJOYN_SESSIONLOST_REASON_OTHER: alljoyn_sessionlostreason = 5
alljoyn_sessionopts = IntPtr
alljoyn_sessionportlistener = IntPtr
@winfunctype_pointer
def alljoyn_sessionportlistener_acceptsessionjoiner_ptr(context: c_void_p, sessionPort: UInt16, joiner: win32more.Foundation.PSTR, opts: win32more.Devices.AllJoyn.alljoyn_sessionopts) -> Int32: ...
class alljoyn_sessionportlistener_callbacks(Structure):
    accept_session_joiner: win32more.Devices.AllJoyn.alljoyn_sessionportlistener_acceptsessionjoiner_ptr
    session_joined: win32more.Devices.AllJoyn.alljoyn_sessionportlistener_sessionjoined_ptr
@winfunctype_pointer
def alljoyn_sessionportlistener_sessionjoined_ptr(context: c_void_p, sessionPort: UInt16, id: UInt32, joiner: win32more.Foundation.PSTR) -> Void: ...
alljoyn_typeid = Int32
ALLJOYN_INVALID: alljoyn_typeid = 0
ALLJOYN_ARRAY: alljoyn_typeid = 97
ALLJOYN_BOOLEAN: alljoyn_typeid = 98
ALLJOYN_DOUBLE: alljoyn_typeid = 100
ALLJOYN_DICT_ENTRY: alljoyn_typeid = 101
ALLJOYN_SIGNATURE: alljoyn_typeid = 103
ALLJOYN_HANDLE: alljoyn_typeid = 104
ALLJOYN_INT32: alljoyn_typeid = 105
ALLJOYN_INT16: alljoyn_typeid = 110
ALLJOYN_OBJECT_PATH: alljoyn_typeid = 111
ALLJOYN_UINT16: alljoyn_typeid = 113
ALLJOYN_STRUCT: alljoyn_typeid = 114
ALLJOYN_STRING: alljoyn_typeid = 115
ALLJOYN_UINT64: alljoyn_typeid = 116
ALLJOYN_UINT32: alljoyn_typeid = 117
ALLJOYN_VARIANT: alljoyn_typeid = 118
ALLJOYN_INT64: alljoyn_typeid = 120
ALLJOYN_BYTE: alljoyn_typeid = 121
ALLJOYN_STRUCT_OPEN: alljoyn_typeid = 40
ALLJOYN_STRUCT_CLOSE: alljoyn_typeid = 41
ALLJOYN_DICT_ENTRY_OPEN: alljoyn_typeid = 123
ALLJOYN_DICT_ENTRY_CLOSE: alljoyn_typeid = 125
ALLJOYN_BOOLEAN_ARRAY: alljoyn_typeid = 25185
ALLJOYN_DOUBLE_ARRAY: alljoyn_typeid = 25697
ALLJOYN_INT32_ARRAY: alljoyn_typeid = 26977
ALLJOYN_INT16_ARRAY: alljoyn_typeid = 28257
ALLJOYN_UINT16_ARRAY: alljoyn_typeid = 29025
ALLJOYN_UINT64_ARRAY: alljoyn_typeid = 29793
ALLJOYN_UINT32_ARRAY: alljoyn_typeid = 30049
ALLJOYN_INT64_ARRAY: alljoyn_typeid = 30817
ALLJOYN_BYTE_ARRAY: alljoyn_typeid = 31073
ALLJOYN_WILDCARD: alljoyn_typeid = 42
QCC_TRUE: UInt32 = 1
QCC_FALSE: UInt32 = 0
ALLJOYN_MESSAGE_FLAG_NO_REPLY_EXPECTED: UInt32 = 1
ALLJOYN_MESSAGE_FLAG_AUTO_START: UInt32 = 2
ALLJOYN_MESSAGE_FLAG_ALLOW_REMOTE_MSG: UInt32 = 4
ALLJOYN_MESSAGE_FLAG_SESSIONLESS: UInt32 = 16
ALLJOYN_MESSAGE_FLAG_GLOBAL_BROADCAST: UInt32 = 32
ALLJOYN_MESSAGE_FLAG_ENCRYPTED: UInt32 = 128
ALLJOYN_TRAFFIC_TYPE_MESSAGES: UInt32 = 1
ALLJOYN_TRAFFIC_TYPE_RAW_UNRELIABLE: UInt32 = 2
ALLJOYN_TRAFFIC_TYPE_RAW_RELIABLE: UInt32 = 4
ALLJOYN_PROXIMITY_ANY: UInt32 = 255
ALLJOYN_PROXIMITY_PHYSICAL: UInt32 = 1
ALLJOYN_PROXIMITY_NETWORK: UInt32 = 2
ALLJOYN_NAMED_PIPE_CONNECT_SPEC: String = 'npipe:'
ALLJOYN_READ_READY: UInt32 = 1
ALLJOYN_WRITE_READY: UInt32 = 2
ALLJOYN_DISCONNECTED: UInt32 = 4
ALLJOYN_LITTLE_ENDIAN: Byte = 108
ALLJOYN_BIG_ENDIAN: Byte = 66
ALLJOYN_MESSAGE_DEFAULT_TIMEOUT: UInt32 = 25000
ALLJOYN_CRED_PASSWORD: UInt16 = 1
ALLJOYN_CRED_USER_NAME: UInt16 = 2
ALLJOYN_CRED_CERT_CHAIN: UInt16 = 4
ALLJOYN_CRED_PRIVATE_KEY: UInt16 = 8
ALLJOYN_CRED_LOGON_ENTRY: UInt16 = 16
ALLJOYN_CRED_EXPIRATION: UInt16 = 32
ALLJOYN_CRED_NEW_PASSWORD: UInt16 = 4097
ALLJOYN_CRED_ONE_TIME_PWD: UInt16 = 8193
ALLJOYN_PROP_ACCESS_READ: Byte = 1
ALLJOYN_PROP_ACCESS_WRITE: Byte = 2
ALLJOYN_PROP_ACCESS_RW: Byte = 3
ALLJOYN_MEMBER_ANNOTATE_NO_REPLY: Byte = 1
ALLJOYN_MEMBER_ANNOTATE_DEPRECATED: Byte = 2
ALLJOYN_MEMBER_ANNOTATE_SESSIONCAST: Byte = 4
ALLJOYN_MEMBER_ANNOTATE_SESSIONLESS: Byte = 8
ALLJOYN_MEMBER_ANNOTATE_UNICAST: Byte = 16
ALLJOYN_MEMBER_ANNOTATE_GLOBAL_BROADCAST: Byte = 32
@winfunctype('MSAJApi.dll')
def AllJoynConnectToBus(connectionSpec: win32more.Foundation.PWSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('MSAJApi.dll')
def AllJoynCloseBusHandle(busHandle: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('MSAJApi.dll')
def AllJoynSendToBus(connectedBusHandle: win32more.Foundation.HANDLE, buffer: c_void_p, bytesToWrite: UInt32, bytesTransferred: POINTER(UInt32), reserved: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('MSAJApi.dll')
def AllJoynReceiveFromBus(connectedBusHandle: win32more.Foundation.HANDLE, buffer: c_void_p, bytesToRead: UInt32, bytesTransferred: POINTER(UInt32), reserved: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('MSAJApi.dll')
def AllJoynEventSelect(connectedBusHandle: win32more.Foundation.HANDLE, eventHandle: win32more.Foundation.HANDLE, eventTypes: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('MSAJApi.dll')
def AllJoynEnumEvents(connectedBusHandle: win32more.Foundation.HANDLE, eventToReset: win32more.Foundation.HANDLE, eventTypes: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('MSAJApi.dll')
def AllJoynCreateBus(outBufferSize: UInt32, inBufferSize: UInt32, lpSecurityAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head)) -> win32more.Foundation.HANDLE: ...
@winfunctype('MSAJApi.dll')
def AllJoynAcceptBusConnection(serverBusHandle: win32more.Foundation.HANDLE, abortEvent: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_unity_deferred_callbacks_process() -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_unity_set_deferred_callback_mainthread_only(mainthread_only: Int32) -> Void: ...
@winfunctype('MSAJApi.dll')
def QCC_StatusText(status: win32more.Devices.AllJoyn.QStatus) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_create() -> win32more.Devices.AllJoyn.alljoyn_msgarg: ...
@cfunctype('MSAJApi.dll')
def alljoyn_msgarg_create_and_set(signature: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.alljoyn_msgarg: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_destroy(arg: win32more.Devices.AllJoyn.alljoyn_msgarg) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_array_create(size: UIntPtr) -> win32more.Devices.AllJoyn.alljoyn_msgarg: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_array_element(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, index: UIntPtr) -> win32more.Devices.AllJoyn.alljoyn_msgarg: ...
@cfunctype('MSAJApi.dll')
def alljoyn_msgarg_set(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, signature: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@cfunctype('MSAJApi.dll')
def alljoyn_msgarg_get(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, signature: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_copy(source: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.alljoyn_msgarg: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_clone(destination: win32more.Devices.AllJoyn.alljoyn_msgarg, source: win32more.Devices.AllJoyn.alljoyn_msgarg) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_equal(lhv: win32more.Devices.AllJoyn.alljoyn_msgarg, rhv: win32more.Devices.AllJoyn.alljoyn_msgarg) -> Int32: ...
@cfunctype('MSAJApi.dll')
def alljoyn_msgarg_array_set(args: win32more.Devices.AllJoyn.alljoyn_msgarg, numArgs: POINTER(UIntPtr), signature: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@cfunctype('MSAJApi.dll')
def alljoyn_msgarg_array_get(args: win32more.Devices.AllJoyn.alljoyn_msgarg, numArgs: UIntPtr, signature: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_tostring(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, str: win32more.Foundation.PSTR, buf: UIntPtr, indent: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_array_tostring(args: win32more.Devices.AllJoyn.alljoyn_msgarg, numArgs: UIntPtr, str: win32more.Foundation.PSTR, buf: UIntPtr, indent: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_signature(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, str: win32more.Foundation.PSTR, buf: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_array_signature(values: win32more.Devices.AllJoyn.alljoyn_msgarg, numValues: UIntPtr, str: win32more.Foundation.PSTR, buf: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_hassignature(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, signature: win32more.Foundation.PSTR) -> Int32: ...
@cfunctype('MSAJApi.dll')
def alljoyn_msgarg_getdictelement(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, elemSig: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_gettype(arg: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.alljoyn_typeid: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_clear(arg: win32more.Devices.AllJoyn.alljoyn_msgarg) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_stabilize(arg: win32more.Devices.AllJoyn.alljoyn_msgarg) -> Void: ...
@cfunctype('MSAJApi.dll')
def alljoyn_msgarg_array_set_offset(args: win32more.Devices.AllJoyn.alljoyn_msgarg, argOffset: UIntPtr, numArgs: POINTER(UIntPtr), signature: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@cfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_and_stabilize(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, signature: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_uint8(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, y: Byte) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_bool(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, b: Int32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_int16(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, n: Int16) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_uint16(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, q: UInt16) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_int32(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, i: Int32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_uint32(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, u: UInt32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_int64(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, x: Int64) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_uint64(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, t: UInt64) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_double(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, d: Double) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_string(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, s: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_objectpath(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, o: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_signature(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, g: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_uint8(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, y: c_char_p_no) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_bool(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, b: POINTER(Int32)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_int16(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, n: POINTER(Int16)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_uint16(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, q: POINTER(UInt16)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_int32(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, i: POINTER(Int32)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_uint32(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, u: POINTER(UInt32)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_int64(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, x: POINTER(Int64)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_uint64(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, t: POINTER(UInt64)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_double(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, d: POINTER(Double)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_string(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, s: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_objectpath(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, o: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_signature(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, g: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_variant(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, v: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_uint8_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: UIntPtr, ay: c_char_p_no) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_bool_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: UIntPtr, ab: POINTER(Int32)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_int16_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: UIntPtr, an: POINTER(Int16)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_uint16_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: UIntPtr, aq: POINTER(UInt16)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_int32_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: UIntPtr, ai: POINTER(Int32)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_uint32_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: UIntPtr, au: POINTER(UInt32)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_int64_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: UIntPtr, ax: POINTER(Int64)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_uint64_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: UIntPtr, at: POINTER(UInt64)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_double_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: UIntPtr, ad: POINTER(Double)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_string_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: UIntPtr, as_: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_objectpath_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: UIntPtr, ao: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_set_signature_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: UIntPtr, ag: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_uint8_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: POINTER(UIntPtr), ay: c_char_p_no) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_bool_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: POINTER(UIntPtr), ab: POINTER(Int32)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_int16_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: POINTER(UIntPtr), an: POINTER(Int16)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_uint16_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: POINTER(UIntPtr), aq: POINTER(UInt16)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_int32_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: POINTER(UIntPtr), ai: POINTER(Int32)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_uint32_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: POINTER(UIntPtr), au: POINTER(UInt32)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_int64_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: POINTER(UIntPtr), ax: POINTER(Int64)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_uint64_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: POINTER(UIntPtr), at: POINTER(UInt64)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_double_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, length: POINTER(UIntPtr), ad: POINTER(Double)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_variant_array(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, signature: win32more.Foundation.PSTR, length: POINTER(UIntPtr), av: POINTER(win32more.Devices.AllJoyn.alljoyn_msgarg)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_array_numberofelements(arg: win32more.Devices.AllJoyn.alljoyn_msgarg) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_array_element(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, index: UIntPtr, element: POINTER(win32more.Devices.AllJoyn.alljoyn_msgarg)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_get_array_elementsignature(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, index: UIntPtr) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_getkey(arg: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.alljoyn_msgarg: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_getvalue(arg: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.alljoyn_msgarg: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_setdictentry(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, key: win32more.Devices.AllJoyn.alljoyn_msgarg, value: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_setstruct(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, struct_members: win32more.Devices.AllJoyn.alljoyn_msgarg, num_members: UIntPtr) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_getnummembers(arg: win32more.Devices.AllJoyn.alljoyn_msgarg) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_msgarg_getmember(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, index: UIntPtr) -> win32more.Devices.AllJoyn.alljoyn_msgarg: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_create_empty() -> win32more.Devices.AllJoyn.alljoyn_aboutdata: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_create(defaultLanguage: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.alljoyn_aboutdata: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_create_full(arg: win32more.Devices.AllJoyn.alljoyn_msgarg, language: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.alljoyn_aboutdata: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_destroy(data: win32more.Devices.AllJoyn.alljoyn_aboutdata) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_createfromxml(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, aboutDataXml: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_isvalid(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, language: win32more.Foundation.PSTR) -> Byte: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_createfrommsgarg(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, arg: win32more.Devices.AllJoyn.alljoyn_msgarg, language: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_setappid(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, appId: c_char_p_no, num: UIntPtr) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_setappid_fromstring(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, appId: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getappid(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, appId: POINTER(c_char_p_no), num: POINTER(UIntPtr)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_setdefaultlanguage(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, defaultLanguage: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getdefaultlanguage(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, defaultLanguage: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_setdevicename(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, deviceName: win32more.Foundation.PSTR, language: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getdevicename(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, deviceName: POINTER(POINTER(SByte)), language: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_setdeviceid(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, deviceId: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getdeviceid(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, deviceId: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_setappname(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, appName: win32more.Foundation.PSTR, language: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getappname(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, appName: POINTER(POINTER(SByte)), language: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_setmanufacturer(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, manufacturer: win32more.Foundation.PSTR, language: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getmanufacturer(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, manufacturer: POINTER(POINTER(SByte)), language: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_setmodelnumber(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, modelNumber: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getmodelnumber(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, modelNumber: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_setsupportedlanguage(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, language: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getsupportedlanguages(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, languageTags: POINTER(POINTER(SByte)), num: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_setdescription(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, description: win32more.Foundation.PSTR, language: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getdescription(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, description: POINTER(POINTER(SByte)), language: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_setdateofmanufacture(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, dateOfManufacture: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getdateofmanufacture(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, dateOfManufacture: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_setsoftwareversion(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, softwareVersion: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getsoftwareversion(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, softwareVersion: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getajsoftwareversion(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, ajSoftwareVersion: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_sethardwareversion(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, hardwareVersion: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_gethardwareversion(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, hardwareVersion: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_setsupporturl(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, supportUrl: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getsupporturl(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, supportUrl: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_setfield(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, name: win32more.Foundation.PSTR, value: win32more.Devices.AllJoyn.alljoyn_msgarg, language: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getfield(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, name: win32more.Foundation.PSTR, value: POINTER(win32more.Devices.AllJoyn.alljoyn_msgarg), language: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getfields(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, fields: POINTER(POINTER(SByte)), num_fields: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getaboutdata(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, msgArg: win32more.Devices.AllJoyn.alljoyn_msgarg, language: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getannouncedaboutdata(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, msgArg: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_isfieldrequired(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, fieldName: win32more.Foundation.PSTR) -> Byte: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_isfieldannounced(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, fieldName: win32more.Foundation.PSTR) -> Byte: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_isfieldlocalized(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, fieldName: win32more.Foundation.PSTR) -> Byte: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdata_getfieldsignature(data: win32more.Devices.AllJoyn.alljoyn_aboutdata, fieldName: win32more.Foundation.PSTR) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_abouticon_create() -> POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head): ...
@winfunctype('MSAJApi.dll')
def alljoyn_abouticon_destroy(icon: POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_abouticon_getcontent(icon: POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head), data: POINTER(c_char_p_no), size: POINTER(UIntPtr)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_abouticon_setcontent(icon: POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head), type: win32more.Foundation.PSTR, data: c_char_p_no, csize: UIntPtr, ownsData: Byte) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_abouticon_geturl(icon: POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head), type: POINTER(POINTER(SByte)), url: POINTER(POINTER(SByte))) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_abouticon_seturl(icon: POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head), type: win32more.Foundation.PSTR, url: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_abouticon_clear(icon: POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_abouticon_setcontent_frommsgarg(icon: POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head), arg: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_getdefaultclaimcapabilities() -> UInt16: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_getapplicationstate(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, state: POINTER(win32more.Devices.AllJoyn.alljoyn_applicationstate)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_setapplicationstate(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, state: win32more.Devices.AllJoyn.alljoyn_applicationstate) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_getpublickey(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, publicKey: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_publickey_destroy(publicKey: POINTER(SByte)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_getmanifesttemplate(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, manifestTemplateXml: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_manifesttemplate_destroy(manifestTemplateXml: POINTER(SByte)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_setmanifesttemplatefromxml(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, manifestTemplateXml: POINTER(SByte)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_getclaimcapabilities(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, claimCapabilities: POINTER(UInt16)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_setclaimcapabilities(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, claimCapabilities: UInt16) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_getclaimcapabilitiesadditionalinfo(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, additionalInfo: POINTER(UInt16)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_setclaimcapabilitiesadditionalinfo(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, additionalInfo: UInt16) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_reset(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_claim(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, caKey: POINTER(SByte), identityCertificateChain: POINTER(SByte), groupId: c_char_p_no, groupSize: UIntPtr, groupAuthority: POINTER(SByte), manifestsXmls: POINTER(POINTER(SByte)), manifestsCount: UIntPtr) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_updateidentity(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, identityCertificateChain: POINTER(SByte), manifestsXmls: POINTER(POINTER(SByte)), manifestsCount: UIntPtr) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_getidentity(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, identityCertificateChain: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_certificatechain_destroy(certificateChain: POINTER(SByte)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_getmanifests(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, manifestArray: POINTER(win32more.Devices.AllJoyn.alljoyn_manifestarray_head)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_manifestarray_cleanup(manifestArray: POINTER(win32more.Devices.AllJoyn.alljoyn_manifestarray_head)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_installmanifests(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, manifestsXmls: POINTER(POINTER(SByte)), manifestsCount: UIntPtr, append: Int32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_getidentitycertificateid(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, certificateId: POINTER(win32more.Devices.AllJoyn.alljoyn_certificateid_head)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_certificateid_cleanup(certificateId: POINTER(win32more.Devices.AllJoyn.alljoyn_certificateid_head)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_updatepolicy(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, policyXml: POINTER(SByte)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_getpolicy(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, policyXml: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_getdefaultpolicy(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, policyXml: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_policy_destroy(policyXml: POINTER(SByte)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_resetpolicy(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_getmembershipsummaries(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, certificateIds: POINTER(win32more.Devices.AllJoyn.alljoyn_certificateidarray_head)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_certificateidarray_cleanup(certificateIdArray: POINTER(win32more.Devices.AllJoyn.alljoyn_certificateidarray_head)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_installmembership(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, membershipCertificateChain: POINTER(SByte)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_removemembership(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator, serial: c_char_p_no, serialLen: UIntPtr, issuerPublicKey: POINTER(SByte), issuerAki: c_char_p_no, issuerAkiLen: UIntPtr) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_startmanagement(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurator_endmanagement(configurator: win32more.Devices.AllJoyn.alljoyn_permissionconfigurator) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_applicationstatelistener_create(callbacks: POINTER(win32more.Devices.AllJoyn.alljoyn_applicationstatelistener_callbacks_head), context: c_void_p) -> win32more.Devices.AllJoyn.alljoyn_applicationstatelistener: ...
@winfunctype('MSAJApi.dll')
def alljoyn_applicationstatelistener_destroy(listener: win32more.Devices.AllJoyn.alljoyn_applicationstatelistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_keystorelistener_create(callbacks: POINTER(win32more.Devices.AllJoyn.alljoyn_keystorelistener_callbacks_head), context: c_void_p) -> win32more.Devices.AllJoyn.alljoyn_keystorelistener: ...
@winfunctype('MSAJApi.dll')
def alljoyn_keystorelistener_with_synchronization_create(callbacks: POINTER(win32more.Devices.AllJoyn.alljoyn_keystorelistener_with_synchronization_callbacks_head), context: c_void_p) -> win32more.Devices.AllJoyn.alljoyn_keystorelistener: ...
@winfunctype('MSAJApi.dll')
def alljoyn_keystorelistener_destroy(listener: win32more.Devices.AllJoyn.alljoyn_keystorelistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_keystorelistener_putkeys(listener: win32more.Devices.AllJoyn.alljoyn_keystorelistener, keyStore: win32more.Devices.AllJoyn.alljoyn_keystore, source: win32more.Foundation.PSTR, password: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_keystorelistener_getkeys(listener: win32more.Devices.AllJoyn.alljoyn_keystorelistener, keyStore: win32more.Devices.AllJoyn.alljoyn_keystore, sink: win32more.Foundation.PSTR, sink_sz: POINTER(UIntPtr)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_sessionopts_create(traffic: Byte, isMultipoint: Int32, proximity: Byte, transports: UInt16) -> win32more.Devices.AllJoyn.alljoyn_sessionopts: ...
@winfunctype('MSAJApi.dll')
def alljoyn_sessionopts_destroy(opts: win32more.Devices.AllJoyn.alljoyn_sessionopts) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_sessionopts_get_traffic(opts: win32more.Devices.AllJoyn.alljoyn_sessionopts) -> Byte: ...
@winfunctype('MSAJApi.dll')
def alljoyn_sessionopts_set_traffic(opts: win32more.Devices.AllJoyn.alljoyn_sessionopts, traffic: Byte) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_sessionopts_get_multipoint(opts: win32more.Devices.AllJoyn.alljoyn_sessionopts) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_sessionopts_set_multipoint(opts: win32more.Devices.AllJoyn.alljoyn_sessionopts, isMultipoint: Int32) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_sessionopts_get_proximity(opts: win32more.Devices.AllJoyn.alljoyn_sessionopts) -> Byte: ...
@winfunctype('MSAJApi.dll')
def alljoyn_sessionopts_set_proximity(opts: win32more.Devices.AllJoyn.alljoyn_sessionopts, proximity: Byte) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_sessionopts_get_transports(opts: win32more.Devices.AllJoyn.alljoyn_sessionopts) -> UInt16: ...
@winfunctype('MSAJApi.dll')
def alljoyn_sessionopts_set_transports(opts: win32more.Devices.AllJoyn.alljoyn_sessionopts, transports: UInt16) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_sessionopts_iscompatible(one: win32more.Devices.AllJoyn.alljoyn_sessionopts, other: win32more.Devices.AllJoyn.alljoyn_sessionopts) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_sessionopts_cmp(one: win32more.Devices.AllJoyn.alljoyn_sessionopts, other: win32more.Devices.AllJoyn.alljoyn_sessionopts) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_create(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> win32more.Devices.AllJoyn.alljoyn_message: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_destroy(msg: win32more.Devices.AllJoyn.alljoyn_message) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_isbroadcastsignal(msg: win32more.Devices.AllJoyn.alljoyn_message) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_isglobalbroadcast(msg: win32more.Devices.AllJoyn.alljoyn_message) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_issessionless(msg: win32more.Devices.AllJoyn.alljoyn_message) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_getflags(msg: win32more.Devices.AllJoyn.alljoyn_message) -> Byte: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_isexpired(msg: win32more.Devices.AllJoyn.alljoyn_message, tillExpireMS: POINTER(UInt32)) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_isunreliable(msg: win32more.Devices.AllJoyn.alljoyn_message) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_isencrypted(msg: win32more.Devices.AllJoyn.alljoyn_message) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_getauthmechanism(msg: win32more.Devices.AllJoyn.alljoyn_message) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_gettype(msg: win32more.Devices.AllJoyn.alljoyn_message) -> win32more.Devices.AllJoyn.alljoyn_messagetype: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_getargs(msg: win32more.Devices.AllJoyn.alljoyn_message, numArgs: POINTER(UIntPtr), args: POINTER(win32more.Devices.AllJoyn.alljoyn_msgarg)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_getarg(msg: win32more.Devices.AllJoyn.alljoyn_message, argN: UIntPtr) -> win32more.Devices.AllJoyn.alljoyn_msgarg: ...
@cfunctype('MSAJApi.dll')
def alljoyn_message_parseargs(msg: win32more.Devices.AllJoyn.alljoyn_message, signature: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_getcallserial(msg: win32more.Devices.AllJoyn.alljoyn_message) -> UInt32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_getsignature(msg: win32more.Devices.AllJoyn.alljoyn_message) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_getobjectpath(msg: win32more.Devices.AllJoyn.alljoyn_message) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_getinterface(msg: win32more.Devices.AllJoyn.alljoyn_message) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_getmembername(msg: win32more.Devices.AllJoyn.alljoyn_message) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_getreplyserial(msg: win32more.Devices.AllJoyn.alljoyn_message) -> UInt32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_getsender(msg: win32more.Devices.AllJoyn.alljoyn_message) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_getreceiveendpointname(msg: win32more.Devices.AllJoyn.alljoyn_message) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_getdestination(msg: win32more.Devices.AllJoyn.alljoyn_message) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_getcompressiontoken(msg: win32more.Devices.AllJoyn.alljoyn_message) -> UInt32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_getsessionid(msg: win32more.Devices.AllJoyn.alljoyn_message) -> UInt32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_geterrorname(msg: win32more.Devices.AllJoyn.alljoyn_message, errorMessage: win32more.Foundation.PSTR, errorMessage_size: POINTER(UIntPtr)) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_tostring(msg: win32more.Devices.AllJoyn.alljoyn_message, str: win32more.Foundation.PSTR, buf: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_description(msg: win32more.Devices.AllJoyn.alljoyn_message, str: win32more.Foundation.PSTR, buf: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_gettimestamp(msg: win32more.Devices.AllJoyn.alljoyn_message) -> UInt32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_eql(one: win32more.Devices.AllJoyn.alljoyn_message, other: win32more.Devices.AllJoyn.alljoyn_message) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_message_setendianess(endian: SByte) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_authlistener_requestcredentialsresponse(listener: win32more.Devices.AllJoyn.alljoyn_authlistener, authContext: c_void_p, accept: Int32, credentials: win32more.Devices.AllJoyn.alljoyn_credentials) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_authlistener_verifycredentialsresponse(listener: win32more.Devices.AllJoyn.alljoyn_authlistener, authContext: c_void_p, accept: Int32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_authlistener_create(callbacks: POINTER(win32more.Devices.AllJoyn.alljoyn_authlistener_callbacks_head), context: c_void_p) -> win32more.Devices.AllJoyn.alljoyn_authlistener: ...
@winfunctype('MSAJApi.dll')
def alljoyn_authlistenerasync_create(callbacks: POINTER(win32more.Devices.AllJoyn.alljoyn_authlistenerasync_callbacks_head), context: c_void_p) -> win32more.Devices.AllJoyn.alljoyn_authlistener: ...
@winfunctype('MSAJApi.dll')
def alljoyn_authlistener_destroy(listener: win32more.Devices.AllJoyn.alljoyn_authlistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_authlistenerasync_destroy(listener: win32more.Devices.AllJoyn.alljoyn_authlistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_authlistener_setsharedsecret(listener: win32more.Devices.AllJoyn.alljoyn_authlistener, sharedSecret: c_char_p_no, sharedSecretSize: UIntPtr) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_credentials_create() -> win32more.Devices.AllJoyn.alljoyn_credentials: ...
@winfunctype('MSAJApi.dll')
def alljoyn_credentials_destroy(cred: win32more.Devices.AllJoyn.alljoyn_credentials) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_credentials_isset(cred: win32more.Devices.AllJoyn.alljoyn_credentials, creds: UInt16) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_credentials_setpassword(cred: win32more.Devices.AllJoyn.alljoyn_credentials, pwd: win32more.Foundation.PSTR) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_credentials_setusername(cred: win32more.Devices.AllJoyn.alljoyn_credentials, userName: win32more.Foundation.PSTR) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_credentials_setcertchain(cred: win32more.Devices.AllJoyn.alljoyn_credentials, certChain: win32more.Foundation.PSTR) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_credentials_setprivatekey(cred: win32more.Devices.AllJoyn.alljoyn_credentials, pk: win32more.Foundation.PSTR) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_credentials_setlogonentry(cred: win32more.Devices.AllJoyn.alljoyn_credentials, logonEntry: win32more.Foundation.PSTR) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_credentials_setexpiration(cred: win32more.Devices.AllJoyn.alljoyn_credentials, expiration: UInt32) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_credentials_getpassword(cred: win32more.Devices.AllJoyn.alljoyn_credentials) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_credentials_getusername(cred: win32more.Devices.AllJoyn.alljoyn_credentials) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_credentials_getcertchain(cred: win32more.Devices.AllJoyn.alljoyn_credentials) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_credentials_getprivateKey(cred: win32more.Devices.AllJoyn.alljoyn_credentials) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_credentials_getlogonentry(cred: win32more.Devices.AllJoyn.alljoyn_credentials) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_credentials_getexpiration(cred: win32more.Devices.AllJoyn.alljoyn_credentials) -> UInt32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_credentials_clear(cred: win32more.Devices.AllJoyn.alljoyn_credentials) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_buslistener_create(callbacks: POINTER(win32more.Devices.AllJoyn.alljoyn_buslistener_callbacks_head), context: c_void_p) -> win32more.Devices.AllJoyn.alljoyn_buslistener: ...
@winfunctype('MSAJApi.dll')
def alljoyn_buslistener_destroy(listener: win32more.Devices.AllJoyn.alljoyn_buslistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_member_getannotationscount(member: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_member_getannotationatindex(member: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, index: UIntPtr, name: win32more.Foundation.PSTR, name_size: POINTER(UIntPtr), value: win32more.Foundation.PSTR, value_size: POINTER(UIntPtr)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_member_getannotation(member: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, name: win32more.Foundation.PSTR, value: win32more.Foundation.PSTR, value_size: POINTER(UIntPtr)) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_member_getargannotationscount(member: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, argName: win32more.Foundation.PSTR) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_member_getargannotationatindex(member: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, argName: win32more.Foundation.PSTR, index: UIntPtr, name: win32more.Foundation.PSTR, name_size: POINTER(UIntPtr), value: win32more.Foundation.PSTR, value_size: POINTER(UIntPtr)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_member_getargannotation(member: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, argName: win32more.Foundation.PSTR, name: win32more.Foundation.PSTR, value: win32more.Foundation.PSTR, value_size: POINTER(UIntPtr)) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_property_getannotationscount(property: win32more.Devices.AllJoyn.alljoyn_interfacedescription_property) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_property_getannotationatindex(property: win32more.Devices.AllJoyn.alljoyn_interfacedescription_property, index: UIntPtr, name: win32more.Foundation.PSTR, name_size: POINTER(UIntPtr), value: win32more.Foundation.PSTR, value_size: POINTER(UIntPtr)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_property_getannotation(property: win32more.Devices.AllJoyn.alljoyn_interfacedescription_property, name: win32more.Foundation.PSTR, value: win32more.Foundation.PSTR, value_size: POINTER(UIntPtr)) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_activate(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_addannotation(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, name: win32more.Foundation.PSTR, value: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getannotation(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, name: win32more.Foundation.PSTR, value: win32more.Foundation.PSTR, value_size: POINTER(UIntPtr)) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getannotationscount(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getannotationatindex(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, index: UIntPtr, name: win32more.Foundation.PSTR, name_size: POINTER(UIntPtr), value: win32more.Foundation.PSTR, value_size: POINTER(UIntPtr)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getmember(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, name: win32more.Foundation.PSTR, member: POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_member_head)) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_addmember(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, type: win32more.Devices.AllJoyn.alljoyn_messagetype, name: win32more.Foundation.PSTR, inputSig: win32more.Foundation.PSTR, outSig: win32more.Foundation.PSTR, argNames: win32more.Foundation.PSTR, annotation: Byte) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_addmemberannotation(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, member: win32more.Foundation.PSTR, name: win32more.Foundation.PSTR, value: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getmemberannotation(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, member: win32more.Foundation.PSTR, name: win32more.Foundation.PSTR, value: win32more.Foundation.PSTR, value_size: POINTER(UIntPtr)) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getmembers(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, members: POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_member_head), numMembers: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_hasmember(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, name: win32more.Foundation.PSTR, inSig: win32more.Foundation.PSTR, outSig: win32more.Foundation.PSTR) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_addmethod(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, name: win32more.Foundation.PSTR, inputSig: win32more.Foundation.PSTR, outSig: win32more.Foundation.PSTR, argNames: win32more.Foundation.PSTR, annotation: Byte, accessPerms: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getmethod(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, name: win32more.Foundation.PSTR, member: POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_member_head)) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_addsignal(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, name: win32more.Foundation.PSTR, sig: win32more.Foundation.PSTR, argNames: win32more.Foundation.PSTR, annotation: Byte, accessPerms: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getsignal(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, name: win32more.Foundation.PSTR, member: POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_member_head)) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getproperty(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, name: win32more.Foundation.PSTR, property: POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_property_head)) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getproperties(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, props: POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription_property_head), numProps: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_addproperty(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, name: win32more.Foundation.PSTR, signature: win32more.Foundation.PSTR, access: Byte) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_addpropertyannotation(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, property: win32more.Foundation.PSTR, name: win32more.Foundation.PSTR, value: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getpropertyannotation(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, property: win32more.Foundation.PSTR, name: win32more.Foundation.PSTR, value: win32more.Foundation.PSTR, str_size: POINTER(UIntPtr)) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_hasproperty(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, name: win32more.Foundation.PSTR) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_hasproperties(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getname(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_introspect(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, str: win32more.Foundation.PSTR, buf: UIntPtr, indent: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_issecure(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getsecuritypolicy(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription) -> win32more.Devices.AllJoyn.alljoyn_interfacedescription_securitypolicy: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_setdescriptionlanguage(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, language: win32more.Foundation.PSTR) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getdescriptionlanguages(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, languages: POINTER(POINTER(SByte)), size: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getdescriptionlanguages2(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, languages: win32more.Foundation.PSTR, languagesSize: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_setdescription(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, description: win32more.Foundation.PSTR) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_setdescriptionforlanguage(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, description: win32more.Foundation.PSTR, languageTag: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getdescriptionforlanguage(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, description: win32more.Foundation.PSTR, maxLanguageLength: UIntPtr, languageTag: win32more.Foundation.PSTR) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_setmemberdescription(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, member: win32more.Foundation.PSTR, description: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_setmemberdescriptionforlanguage(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, member: win32more.Foundation.PSTR, description: win32more.Foundation.PSTR, languageTag: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getmemberdescriptionforlanguage(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, member: win32more.Foundation.PSTR, description: win32more.Foundation.PSTR, maxLanguageLength: UIntPtr, languageTag: win32more.Foundation.PSTR) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_setargdescription(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, member: win32more.Foundation.PSTR, argName: win32more.Foundation.PSTR, description: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_setargdescriptionforlanguage(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, member: win32more.Foundation.PSTR, arg: win32more.Foundation.PSTR, description: win32more.Foundation.PSTR, languageTag: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getargdescriptionforlanguage(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, member: win32more.Foundation.PSTR, arg: win32more.Foundation.PSTR, description: win32more.Foundation.PSTR, maxLanguageLength: UIntPtr, languageTag: win32more.Foundation.PSTR) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_setpropertydescription(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, name: win32more.Foundation.PSTR, description: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_setpropertydescriptionforlanguage(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, name: win32more.Foundation.PSTR, description: win32more.Foundation.PSTR, languageTag: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getpropertydescriptionforlanguage(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, property: win32more.Foundation.PSTR, description: win32more.Foundation.PSTR, maxLanguageLength: UIntPtr, languageTag: win32more.Foundation.PSTR) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_setdescriptiontranslationcallback(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, translationCallback: win32more.Devices.AllJoyn.alljoyn_interfacedescription_translation_callback_ptr) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getdescriptiontranslationcallback(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription) -> win32more.Devices.AllJoyn.alljoyn_interfacedescription_translation_callback_ptr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_hasdescription(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_addargannotation(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, member: win32more.Foundation.PSTR, argName: win32more.Foundation.PSTR, name: win32more.Foundation.PSTR, value: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_getmemberargannotation(iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, member: win32more.Foundation.PSTR, argName: win32more.Foundation.PSTR, name: win32more.Foundation.PSTR, value: win32more.Foundation.PSTR, value_size: POINTER(UIntPtr)) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_eql(one: win32more.Devices.AllJoyn.alljoyn_interfacedescription, other: win32more.Devices.AllJoyn.alljoyn_interfacedescription) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_member_eql(one: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, other: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_interfacedescription_property_eql(one: win32more.Devices.AllJoyn.alljoyn_interfacedescription_property, other: win32more.Devices.AllJoyn.alljoyn_interfacedescription_property) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_create(path: win32more.Foundation.PSTR, isPlaceholder: Int32, callbacks_in: POINTER(win32more.Devices.AllJoyn.alljoyn_busobject_callbacks_head), context_in: c_void_p) -> win32more.Devices.AllJoyn.alljoyn_busobject: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_destroy(bus: win32more.Devices.AllJoyn.alljoyn_busobject) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_getpath(bus: win32more.Devices.AllJoyn.alljoyn_busobject) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_emitpropertychanged(bus: win32more.Devices.AllJoyn.alljoyn_busobject, ifcName: win32more.Foundation.PSTR, propName: win32more.Foundation.PSTR, val: win32more.Devices.AllJoyn.alljoyn_msgarg, id: UInt32) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_emitpropertieschanged(bus: win32more.Devices.AllJoyn.alljoyn_busobject, ifcName: win32more.Foundation.PSTR, propNames: POINTER(POINTER(SByte)), numProps: UIntPtr, id: UInt32) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_getname(bus: win32more.Devices.AllJoyn.alljoyn_busobject, buffer: win32more.Foundation.PSTR, bufferSz: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_addinterface(bus: win32more.Devices.AllJoyn.alljoyn_busobject, iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_addmethodhandler(bus: win32more.Devices.AllJoyn.alljoyn_busobject, member: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, handler: win32more.Devices.AllJoyn.alljoyn_messagereceiver_methodhandler_ptr, context: c_void_p) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_addmethodhandlers(bus: win32more.Devices.AllJoyn.alljoyn_busobject, entries: POINTER(win32more.Devices.AllJoyn.alljoyn_busobject_methodentry_head), numEntries: UIntPtr) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_methodreply_args(bus: win32more.Devices.AllJoyn.alljoyn_busobject, msg: win32more.Devices.AllJoyn.alljoyn_message, args: win32more.Devices.AllJoyn.alljoyn_msgarg, numArgs: UIntPtr) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_methodreply_err(bus: win32more.Devices.AllJoyn.alljoyn_busobject, msg: win32more.Devices.AllJoyn.alljoyn_message, error: win32more.Foundation.PSTR, errorMessage: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_methodreply_status(bus: win32more.Devices.AllJoyn.alljoyn_busobject, msg: win32more.Devices.AllJoyn.alljoyn_message, status: win32more.Devices.AllJoyn.QStatus) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_getbusattachment(bus: win32more.Devices.AllJoyn.alljoyn_busobject) -> win32more.Devices.AllJoyn.alljoyn_busattachment: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_signal(bus: win32more.Devices.AllJoyn.alljoyn_busobject, destination: win32more.Foundation.PSTR, sessionId: UInt32, signal: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, args: win32more.Devices.AllJoyn.alljoyn_msgarg, numArgs: UIntPtr, timeToLive: UInt16, flags: Byte, msg: win32more.Devices.AllJoyn.alljoyn_message) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_cancelsessionlessmessage_serial(bus: win32more.Devices.AllJoyn.alljoyn_busobject, serialNumber: UInt32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_cancelsessionlessmessage(bus: win32more.Devices.AllJoyn.alljoyn_busobject, msg: win32more.Devices.AllJoyn.alljoyn_message) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_issecure(bus: win32more.Devices.AllJoyn.alljoyn_busobject) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_getannouncedinterfacenames(bus: win32more.Devices.AllJoyn.alljoyn_busobject, interfaces: POINTER(POINTER(SByte)), numInterfaces: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_setannounceflag(bus: win32more.Devices.AllJoyn.alljoyn_busobject, iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription, isAnnounced: win32more.Devices.AllJoyn.alljoyn_about_announceflag) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busobject_addinterface_announced(bus: win32more.Devices.AllJoyn.alljoyn_busobject, iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_create(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, service: win32more.Foundation.PSTR, path: win32more.Foundation.PSTR, sessionId: UInt32) -> win32more.Devices.AllJoyn.alljoyn_proxybusobject: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_create_secure(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, service: win32more.Foundation.PSTR, path: win32more.Foundation.PSTR, sessionId: UInt32) -> win32more.Devices.AllJoyn.alljoyn_proxybusobject: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_destroy(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_addinterface(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_addinterface_by_name(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, name: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_getchildren(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, children: POINTER(win32more.Devices.AllJoyn.alljoyn_proxybusobject), numChildren: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_getchild(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, path: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.alljoyn_proxybusobject: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_addchild(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, child: win32more.Devices.AllJoyn.alljoyn_proxybusobject) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_removechild(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, path: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_introspectremoteobject(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_introspectremoteobjectasync(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, callback: win32more.Devices.AllJoyn.alljoyn_proxybusobject_listener_introspectcb_ptr, context: c_void_p) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_getproperty(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, iface: win32more.Foundation.PSTR, property: win32more.Foundation.PSTR, value: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_getpropertyasync(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, iface: win32more.Foundation.PSTR, property: win32more.Foundation.PSTR, callback: win32more.Devices.AllJoyn.alljoyn_proxybusobject_listener_getpropertycb_ptr, timeout: UInt32, context: c_void_p) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_getallproperties(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, iface: win32more.Foundation.PSTR, values: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_getallpropertiesasync(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, iface: win32more.Foundation.PSTR, callback: win32more.Devices.AllJoyn.alljoyn_proxybusobject_listener_getallpropertiescb_ptr, timeout: UInt32, context: c_void_p) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_setproperty(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, iface: win32more.Foundation.PSTR, property: win32more.Foundation.PSTR, value: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_registerpropertieschangedlistener(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, iface: win32more.Foundation.PSTR, properties: POINTER(POINTER(SByte)), numProperties: UIntPtr, callback: win32more.Devices.AllJoyn.alljoyn_proxybusobject_listener_propertieschanged_ptr, context: c_void_p) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_unregisterpropertieschangedlistener(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, iface: win32more.Foundation.PSTR, callback: win32more.Devices.AllJoyn.alljoyn_proxybusobject_listener_propertieschanged_ptr) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_setpropertyasync(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, iface: win32more.Foundation.PSTR, property: win32more.Foundation.PSTR, value: win32more.Devices.AllJoyn.alljoyn_msgarg, callback: win32more.Devices.AllJoyn.alljoyn_proxybusobject_listener_setpropertycb_ptr, timeout: UInt32, context: c_void_p) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_methodcall(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, ifaceName: win32more.Foundation.PSTR, methodName: win32more.Foundation.PSTR, args: win32more.Devices.AllJoyn.alljoyn_msgarg, numArgs: UIntPtr, replyMsg: win32more.Devices.AllJoyn.alljoyn_message, timeout: UInt32, flags: Byte) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_methodcall_member(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, method: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, args: win32more.Devices.AllJoyn.alljoyn_msgarg, numArgs: UIntPtr, replyMsg: win32more.Devices.AllJoyn.alljoyn_message, timeout: UInt32, flags: Byte) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_methodcall_noreply(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, ifaceName: win32more.Foundation.PSTR, methodName: win32more.Foundation.PSTR, args: win32more.Devices.AllJoyn.alljoyn_msgarg, numArgs: UIntPtr, flags: Byte) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_methodcall_member_noreply(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, method: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, args: win32more.Devices.AllJoyn.alljoyn_msgarg, numArgs: UIntPtr, flags: Byte) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_methodcallasync(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, ifaceName: win32more.Foundation.PSTR, methodName: win32more.Foundation.PSTR, replyFunc: win32more.Devices.AllJoyn.alljoyn_messagereceiver_replyhandler_ptr, args: win32more.Devices.AllJoyn.alljoyn_msgarg, numArgs: UIntPtr, context: c_void_p, timeout: UInt32, flags: Byte) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_methodcallasync_member(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, method: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, replyFunc: win32more.Devices.AllJoyn.alljoyn_messagereceiver_replyhandler_ptr, args: win32more.Devices.AllJoyn.alljoyn_msgarg, numArgs: UIntPtr, context: c_void_p, timeout: UInt32, flags: Byte) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_parsexml(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, xml: win32more.Foundation.PSTR, identifier: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_secureconnection(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, forceAuth: Int32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_secureconnectionasync(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, forceAuth: Int32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_getinterface(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, iface: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.alljoyn_interfacedescription: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_getinterfaces(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, ifaces: POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription), numIfaces: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_getpath(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_getservicename(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_getuniquename(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_getsessionid(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject) -> UInt32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_implementsinterface(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject, iface: win32more.Foundation.PSTR) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_copy(source: win32more.Devices.AllJoyn.alljoyn_proxybusobject) -> win32more.Devices.AllJoyn.alljoyn_proxybusobject: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_isvalid(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_issecure(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_enablepropertycaching(proxyObj: win32more.Devices.AllJoyn.alljoyn_proxybusobject) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurationlistener_create(callbacks: POINTER(win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener_callbacks_head), context: c_void_p) -> win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener: ...
@winfunctype('MSAJApi.dll')
def alljoyn_permissionconfigurationlistener_destroy(listener: win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_sessionlistener_create(callbacks: POINTER(win32more.Devices.AllJoyn.alljoyn_sessionlistener_callbacks_head), context: c_void_p) -> win32more.Devices.AllJoyn.alljoyn_sessionlistener: ...
@winfunctype('MSAJApi.dll')
def alljoyn_sessionlistener_destroy(listener: win32more.Devices.AllJoyn.alljoyn_sessionlistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_sessionportlistener_create(callbacks: POINTER(win32more.Devices.AllJoyn.alljoyn_sessionportlistener_callbacks_head), context: c_void_p) -> win32more.Devices.AllJoyn.alljoyn_sessionportlistener: ...
@winfunctype('MSAJApi.dll')
def alljoyn_sessionportlistener_destroy(listener: win32more.Devices.AllJoyn.alljoyn_sessionportlistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutlistener_create(callback: POINTER(win32more.Devices.AllJoyn.alljoyn_aboutlistener_callback_head), context: c_void_p) -> win32more.Devices.AllJoyn.alljoyn_aboutlistener: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutlistener_destroy(listener: win32more.Devices.AllJoyn.alljoyn_aboutlistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_create(applicationName: win32more.Foundation.PSTR, allowRemoteMessages: Int32) -> win32more.Devices.AllJoyn.alljoyn_busattachment: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_create_concurrency(applicationName: win32more.Foundation.PSTR, allowRemoteMessages: Int32, concurrency: UInt32) -> win32more.Devices.AllJoyn.alljoyn_busattachment: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_destroy(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_start(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_stop(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_join(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_getconcurrency(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> UInt32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_getconnectspec(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_enableconcurrentcallbacks(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_createinterface(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, name: win32more.Foundation.PSTR, iface: POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_createinterface_secure(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, name: win32more.Foundation.PSTR, iface: POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription), secPolicy: win32more.Devices.AllJoyn.alljoyn_interfacedescription_securitypolicy) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_connect(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, connectSpec: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_registerbuslistener(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, listener: win32more.Devices.AllJoyn.alljoyn_buslistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_unregisterbuslistener(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, listener: win32more.Devices.AllJoyn.alljoyn_buslistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_findadvertisedname(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, namePrefix: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_findadvertisednamebytransport(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, namePrefix: win32more.Foundation.PSTR, transports: UInt16) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_cancelfindadvertisedname(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, namePrefix: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_cancelfindadvertisednamebytransport(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, namePrefix: win32more.Foundation.PSTR, transports: UInt16) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_advertisename(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, name: win32more.Foundation.PSTR, transports: UInt16) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_canceladvertisename(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, name: win32more.Foundation.PSTR, transports: UInt16) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_getinterface(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, name: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.alljoyn_interfacedescription: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_joinsession(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, sessionHost: win32more.Foundation.PSTR, sessionPort: UInt16, listener: win32more.Devices.AllJoyn.alljoyn_sessionlistener, sessionId: POINTER(UInt32), opts: win32more.Devices.AllJoyn.alljoyn_sessionopts) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_joinsessionasync(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, sessionHost: win32more.Foundation.PSTR, sessionPort: UInt16, listener: win32more.Devices.AllJoyn.alljoyn_sessionlistener, opts: win32more.Devices.AllJoyn.alljoyn_sessionopts, callback: win32more.Devices.AllJoyn.alljoyn_busattachment_joinsessioncb_ptr, context: c_void_p) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_registerbusobject(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, obj: win32more.Devices.AllJoyn.alljoyn_busobject) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_registerbusobject_secure(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, obj: win32more.Devices.AllJoyn.alljoyn_busobject) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_unregisterbusobject(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, object: win32more.Devices.AllJoyn.alljoyn_busobject) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_requestname(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, requestedName: win32more.Foundation.PSTR, flags: UInt32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_releasename(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, name: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_bindsessionport(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, sessionPort: POINTER(UInt16), opts: win32more.Devices.AllJoyn.alljoyn_sessionopts, listener: win32more.Devices.AllJoyn.alljoyn_sessionportlistener) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_unbindsessionport(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, sessionPort: UInt16) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_enablepeersecurity(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, authMechanisms: win32more.Foundation.PSTR, listener: win32more.Devices.AllJoyn.alljoyn_authlistener, keyStoreFileName: win32more.Foundation.PSTR, isShared: Int32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_enablepeersecuritywithpermissionconfigurationlistener(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, authMechanisms: win32more.Foundation.PSTR, authListener: win32more.Devices.AllJoyn.alljoyn_authlistener, keyStoreFileName: win32more.Foundation.PSTR, isShared: Int32, permissionConfigurationListener: win32more.Devices.AllJoyn.alljoyn_permissionconfigurationlistener) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_ispeersecurityenabled(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_createinterfacesfromxml(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, xml: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_getinterfaces(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, ifaces: POINTER(win32more.Devices.AllJoyn.alljoyn_interfacedescription), numIfaces: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_deleteinterface(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, iface: win32more.Devices.AllJoyn.alljoyn_interfacedescription) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_isstarted(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_isstopping(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_isconnected(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> Int32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_disconnect(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, unused: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_getdbusproxyobj(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> win32more.Devices.AllJoyn.alljoyn_proxybusobject: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_getalljoynproxyobj(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> win32more.Devices.AllJoyn.alljoyn_proxybusobject: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_getalljoyndebugobj(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> win32more.Devices.AllJoyn.alljoyn_proxybusobject: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_getuniquename(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_getglobalguidstring(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_registersignalhandler(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, signal_handler: win32more.Devices.AllJoyn.alljoyn_messagereceiver_signalhandler_ptr, member: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, srcPath: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_registersignalhandlerwithrule(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, signal_handler: win32more.Devices.AllJoyn.alljoyn_messagereceiver_signalhandler_ptr, member: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, matchRule: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_unregistersignalhandler(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, signal_handler: win32more.Devices.AllJoyn.alljoyn_messagereceiver_signalhandler_ptr, member: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, srcPath: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_unregistersignalhandlerwithrule(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, signal_handler: win32more.Devices.AllJoyn.alljoyn_messagereceiver_signalhandler_ptr, member: win32more.Devices.AllJoyn.alljoyn_interfacedescription_member, matchRule: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_unregisterallhandlers(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_registerkeystorelistener(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, listener: win32more.Devices.AllJoyn.alljoyn_keystorelistener) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_reloadkeystore(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_clearkeystore(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_clearkeys(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, guid: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_setkeyexpiration(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, guid: win32more.Foundation.PSTR, timeout: UInt32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_getkeyexpiration(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, guid: win32more.Foundation.PSTR, timeout: POINTER(UInt32)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_addlogonentry(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, authMechanism: win32more.Foundation.PSTR, userName: win32more.Foundation.PSTR, password: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_addmatch(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, rule: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_removematch(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, rule: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_setsessionlistener(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, sessionId: UInt32, listener: win32more.Devices.AllJoyn.alljoyn_sessionlistener) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_leavesession(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, sessionId: UInt32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_secureconnection(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, name: win32more.Foundation.PSTR, forceAuth: Int32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_secureconnectionasync(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, name: win32more.Foundation.PSTR, forceAuth: Int32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_removesessionmember(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, sessionId: UInt32, memberName: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_setlinktimeout(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, sessionid: UInt32, linkTimeout: POINTER(UInt32)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_setlinktimeoutasync(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, sessionid: UInt32, linkTimeout: UInt32, callback: win32more.Devices.AllJoyn.alljoyn_busattachment_setlinktimeoutcb_ptr, context: c_void_p) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_namehasowner(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, name: win32more.Foundation.PSTR, hasOwner: POINTER(Int32)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_getpeerguid(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, name: win32more.Foundation.PSTR, guid: win32more.Foundation.PSTR, guidSz: POINTER(UIntPtr)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_setdaemondebug(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, module: win32more.Foundation.PSTR, level: UInt32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_gettimestamp() -> UInt32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_ping(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, name: win32more.Foundation.PSTR, timeout: UInt32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_registeraboutlistener(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, aboutListener: win32more.Devices.AllJoyn.alljoyn_aboutlistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_unregisteraboutlistener(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, aboutListener: win32more.Devices.AllJoyn.alljoyn_aboutlistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_unregisterallaboutlisteners(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_whoimplements_interfaces(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, implementsInterfaces: POINTER(POINTER(SByte)), numberInterfaces: UIntPtr) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_whoimplements_interface(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, implementsInterface: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_cancelwhoimplements_interfaces(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, implementsInterfaces: POINTER(POINTER(SByte)), numberInterfaces: UIntPtr) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_cancelwhoimplements_interface(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, implementsInterface: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_getpermissionconfigurator(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> win32more.Devices.AllJoyn.alljoyn_permissionconfigurator: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_registerapplicationstatelistener(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, listener: win32more.Devices.AllJoyn.alljoyn_applicationstatelistener) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_unregisterapplicationstatelistener(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, listener: win32more.Devices.AllJoyn.alljoyn_applicationstatelistener) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_busattachment_deletedefaultkeystore(applicationName: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_abouticonobj_create(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, icon: POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head)) -> POINTER(win32more.Devices.AllJoyn._alljoyn_abouticonobj_handle_head): ...
@winfunctype('MSAJApi.dll')
def alljoyn_abouticonobj_destroy(icon: POINTER(win32more.Devices.AllJoyn._alljoyn_abouticonobj_handle_head)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_abouticonproxy_create(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, busName: win32more.Foundation.PSTR, sessionId: UInt32) -> POINTER(win32more.Devices.AllJoyn._alljoyn_abouticonproxy_handle_head): ...
@winfunctype('MSAJApi.dll')
def alljoyn_abouticonproxy_destroy(proxy: POINTER(win32more.Devices.AllJoyn._alljoyn_abouticonproxy_handle_head)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_abouticonproxy_geticon(proxy: POINTER(win32more.Devices.AllJoyn._alljoyn_abouticonproxy_handle_head), icon: POINTER(win32more.Devices.AllJoyn._alljoyn_abouticon_handle_head)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_abouticonproxy_getversion(proxy: POINTER(win32more.Devices.AllJoyn._alljoyn_abouticonproxy_handle_head), version: POINTER(UInt16)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdatalistener_create(callbacks: POINTER(win32more.Devices.AllJoyn.alljoyn_aboutdatalistener_callbacks_head), context: c_void_p) -> win32more.Devices.AllJoyn.alljoyn_aboutdatalistener: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutdatalistener_destroy(listener: win32more.Devices.AllJoyn.alljoyn_aboutdatalistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobj_create(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, isAnnounced: win32more.Devices.AllJoyn.alljoyn_about_announceflag) -> win32more.Devices.AllJoyn.alljoyn_aboutobj: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobj_destroy(obj: win32more.Devices.AllJoyn.alljoyn_aboutobj) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobj_announce(obj: win32more.Devices.AllJoyn.alljoyn_aboutobj, sessionPort: UInt16, aboutData: win32more.Devices.AllJoyn.alljoyn_aboutdata) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobj_announce_using_datalistener(obj: win32more.Devices.AllJoyn.alljoyn_aboutobj, sessionPort: UInt16, aboutListener: win32more.Devices.AllJoyn.alljoyn_aboutdatalistener) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobj_unannounce(obj: win32more.Devices.AllJoyn.alljoyn_aboutobj) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobjectdescription_create() -> win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobjectdescription_create_full(arg: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobjectdescription_createfrommsgarg(description: win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription, arg: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobjectdescription_destroy(description: win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobjectdescription_getpaths(description: win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription, paths: POINTER(POINTER(SByte)), numPaths: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobjectdescription_getinterfaces(description: win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription, path: win32more.Foundation.PSTR, interfaces: POINTER(POINTER(SByte)), numInterfaces: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobjectdescription_getinterfacepaths(description: win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription, interfaceName: win32more.Foundation.PSTR, paths: POINTER(POINTER(SByte)), numPaths: UIntPtr) -> UIntPtr: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobjectdescription_clear(description: win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobjectdescription_haspath(description: win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription, path: win32more.Foundation.PSTR) -> Byte: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobjectdescription_hasinterface(description: win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription, interfaceName: win32more.Foundation.PSTR) -> Byte: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobjectdescription_hasinterfaceatpath(description: win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription, path: win32more.Foundation.PSTR, interfaceName: win32more.Foundation.PSTR) -> Byte: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutobjectdescription_getmsgarg(description: win32more.Devices.AllJoyn.alljoyn_aboutobjectdescription, msgArg: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutproxy_create(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, busName: win32more.Foundation.PSTR, sessionId: UInt32) -> win32more.Devices.AllJoyn.alljoyn_aboutproxy: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutproxy_destroy(proxy: win32more.Devices.AllJoyn.alljoyn_aboutproxy) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutproxy_getobjectdescription(proxy: win32more.Devices.AllJoyn.alljoyn_aboutproxy, objectDesc: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutproxy_getaboutdata(proxy: win32more.Devices.AllJoyn.alljoyn_aboutproxy, language: win32more.Foundation.PSTR, data: win32more.Devices.AllJoyn.alljoyn_msgarg) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_aboutproxy_getversion(proxy: win32more.Devices.AllJoyn.alljoyn_aboutproxy, version: POINTER(UInt16)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_pinglistener_create(callback: POINTER(win32more.Devices.AllJoyn.alljoyn_pinglistener_callback_head), context: c_void_p) -> win32more.Devices.AllJoyn.alljoyn_pinglistener: ...
@winfunctype('MSAJApi.dll')
def alljoyn_pinglistener_destroy(listener: win32more.Devices.AllJoyn.alljoyn_pinglistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_autopinger_create(bus: win32more.Devices.AllJoyn.alljoyn_busattachment) -> win32more.Devices.AllJoyn.alljoyn_autopinger: ...
@winfunctype('MSAJApi.dll')
def alljoyn_autopinger_destroy(autopinger: win32more.Devices.AllJoyn.alljoyn_autopinger) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_autopinger_pause(autopinger: win32more.Devices.AllJoyn.alljoyn_autopinger) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_autopinger_resume(autopinger: win32more.Devices.AllJoyn.alljoyn_autopinger) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_autopinger_addpinggroup(autopinger: win32more.Devices.AllJoyn.alljoyn_autopinger, group: win32more.Foundation.PSTR, listener: win32more.Devices.AllJoyn.alljoyn_pinglistener, pinginterval: UInt32) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_autopinger_removepinggroup(autopinger: win32more.Devices.AllJoyn.alljoyn_autopinger, group: win32more.Foundation.PSTR) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_autopinger_setpinginterval(autopinger: win32more.Devices.AllJoyn.alljoyn_autopinger, group: win32more.Foundation.PSTR, pinginterval: UInt32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_autopinger_adddestination(autopinger: win32more.Devices.AllJoyn.alljoyn_autopinger, group: win32more.Foundation.PSTR, destination: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_autopinger_removedestination(autopinger: win32more.Devices.AllJoyn.alljoyn_autopinger, group: win32more.Foundation.PSTR, destination: win32more.Foundation.PSTR, removeall: Int32) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_getversion() -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_getbuildinfo() -> win32more.Foundation.PSTR: ...
@winfunctype('MSAJApi.dll')
def alljoyn_getnumericversion() -> UInt32: ...
@winfunctype('MSAJApi.dll')
def alljoyn_init() -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_shutdown() -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_routerinit() -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_routerinitwithconfig(configXml: POINTER(SByte)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_routershutdown() -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_ref_create(proxy: win32more.Devices.AllJoyn.alljoyn_proxybusobject) -> win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_ref_get(ref: win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref) -> win32more.Devices.AllJoyn.alljoyn_proxybusobject: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_ref_incref(ref: win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_proxybusobject_ref_decref(ref: win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_observerlistener_create(callback: POINTER(win32more.Devices.AllJoyn.alljoyn_observerlistener_callback_head), context: c_void_p) -> win32more.Devices.AllJoyn.alljoyn_observerlistener: ...
@winfunctype('MSAJApi.dll')
def alljoyn_observerlistener_destroy(listener: win32more.Devices.AllJoyn.alljoyn_observerlistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_observer_create(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, mandatoryInterfaces: POINTER(POINTER(SByte)), numMandatoryInterfaces: UIntPtr) -> win32more.Devices.AllJoyn.alljoyn_observer: ...
@winfunctype('MSAJApi.dll')
def alljoyn_observer_destroy(observer: win32more.Devices.AllJoyn.alljoyn_observer) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_observer_registerlistener(observer: win32more.Devices.AllJoyn.alljoyn_observer, listener: win32more.Devices.AllJoyn.alljoyn_observerlistener, triggerOnExisting: Int32) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_observer_unregisterlistener(observer: win32more.Devices.AllJoyn.alljoyn_observer, listener: win32more.Devices.AllJoyn.alljoyn_observerlistener) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_observer_unregisteralllisteners(observer: win32more.Devices.AllJoyn.alljoyn_observer) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_observer_get(observer: win32more.Devices.AllJoyn.alljoyn_observer, uniqueBusName: win32more.Foundation.PSTR, objectPath: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref: ...
@winfunctype('MSAJApi.dll')
def alljoyn_observer_getfirst(observer: win32more.Devices.AllJoyn.alljoyn_observer) -> win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref: ...
@winfunctype('MSAJApi.dll')
def alljoyn_observer_getnext(observer: win32more.Devices.AllJoyn.alljoyn_observer, proxyref: win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref) -> win32more.Devices.AllJoyn.alljoyn_proxybusobject_ref: ...
@winfunctype('MSAJApi.dll')
def alljoyn_passwordmanager_setcredentials(authMechanism: win32more.Foundation.PSTR, password: win32more.Foundation.PSTR) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_getpermissionmanagementsessionport() -> UInt16: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_create(bus: win32more.Devices.AllJoyn.alljoyn_busattachment, appBusName: POINTER(SByte), sessionId: UInt32) -> win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_destroy(proxy: win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_claim(proxy: win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy, caKey: POINTER(SByte), identityCertificateChain: POINTER(SByte), groupId: c_char_p_no, groupSize: UIntPtr, groupAuthority: POINTER(SByte), manifestsXmls: POINTER(POINTER(SByte)), manifestsCount: UIntPtr) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_getmanifesttemplate(proxy: win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy, manifestTemplateXml: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_manifesttemplate_destroy(manifestTemplateXml: POINTER(SByte)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_getapplicationstate(proxy: win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy, applicationState: POINTER(win32more.Devices.AllJoyn.alljoyn_applicationstate)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_getclaimcapabilities(proxy: win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy, capabilities: POINTER(UInt16)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_getclaimcapabilitiesadditionalinfo(proxy: win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy, additionalInfo: POINTER(UInt16)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_getpolicy(proxy: win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy, policyXml: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_getdefaultpolicy(proxy: win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy, policyXml: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_policy_destroy(policyXml: POINTER(SByte)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_updatepolicy(proxy: win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy, policyXml: POINTER(SByte)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_updateidentity(proxy: win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy, identityCertificateChain: POINTER(SByte), manifestsXmls: POINTER(POINTER(SByte)), manifestsCount: UIntPtr) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_installmembership(proxy: win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy, membershipCertificateChain: POINTER(SByte)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_reset(proxy: win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_resetpolicy(proxy: win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_startmanagement(proxy: win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_endmanagement(proxy: win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_geteccpublickey(proxy: win32more.Devices.AllJoyn.alljoyn_securityapplicationproxy, eccPublicKey: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_eccpublickey_destroy(eccPublicKey: POINTER(SByte)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_signmanifest(unsignedManifestXml: POINTER(SByte), identityCertificatePem: POINTER(SByte), signingPrivateKeyPem: POINTER(SByte), signedManifestXml: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_manifest_destroy(signedManifestXml: POINTER(SByte)) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_computemanifestdigest(unsignedManifestXml: POINTER(SByte), identityCertificatePem: POINTER(SByte), digest: POINTER(c_char_p_no), digestSize: POINTER(UIntPtr)) -> win32more.Devices.AllJoyn.QStatus: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_digest_destroy(digest: c_char_p_no) -> Void: ...
@winfunctype('MSAJApi.dll')
def alljoyn_securityapplicationproxy_setmanifestsignature(unsignedManifestXml: POINTER(SByte), identityCertificatePem: POINTER(SByte), signature: c_char_p_no, signatureSize: UIntPtr, signedManifestXml: POINTER(POINTER(SByte))) -> win32more.Devices.AllJoyn.QStatus: ...
QStatus = Int32
ER_OK: QStatus = 0
ER_FAIL: QStatus = 1
ER_UTF_CONVERSION_FAILED: QStatus = 2
ER_BUFFER_TOO_SMALL: QStatus = 3
ER_OS_ERROR: QStatus = 4
ER_OUT_OF_MEMORY: QStatus = 5
ER_SOCKET_BIND_ERROR: QStatus = 6
ER_INIT_FAILED: QStatus = 7
ER_WOULDBLOCK: QStatus = 8
ER_NOT_IMPLEMENTED: QStatus = 9
ER_TIMEOUT: QStatus = 10
ER_SOCK_OTHER_END_CLOSED: QStatus = 11
ER_BAD_ARG_1: QStatus = 12
ER_BAD_ARG_2: QStatus = 13
ER_BAD_ARG_3: QStatus = 14
ER_BAD_ARG_4: QStatus = 15
ER_BAD_ARG_5: QStatus = 16
ER_BAD_ARG_6: QStatus = 17
ER_BAD_ARG_7: QStatus = 18
ER_BAD_ARG_8: QStatus = 19
ER_INVALID_ADDRESS: QStatus = 20
ER_INVALID_DATA: QStatus = 21
ER_READ_ERROR: QStatus = 22
ER_WRITE_ERROR: QStatus = 23
ER_OPEN_FAILED: QStatus = 24
ER_PARSE_ERROR: QStatus = 25
ER_END_OF_DATA: QStatus = 26
ER_CONN_REFUSED: QStatus = 27
ER_BAD_ARG_COUNT: QStatus = 28
ER_WARNING: QStatus = 29
ER_EOF: QStatus = 30
ER_DEADLOCK: QStatus = 31
ER_COMMON_ERRORS: QStatus = 4096
ER_STOPPING_THREAD: QStatus = 4097
ER_ALERTED_THREAD: QStatus = 4098
ER_XML_MALFORMED: QStatus = 4099
ER_AUTH_FAIL: QStatus = 4100
ER_AUTH_USER_REJECT: QStatus = 4101
ER_NO_SUCH_ALARM: QStatus = 4102
ER_TIMER_FALLBEHIND: QStatus = 4103
ER_SSL_ERRORS: QStatus = 4104
ER_SSL_INIT: QStatus = 4105
ER_SSL_CONNECT: QStatus = 4106
ER_SSL_VERIFY: QStatus = 4107
ER_EXTERNAL_THREAD: QStatus = 4108
ER_CRYPTO_ERROR: QStatus = 4109
ER_CRYPTO_TRUNCATED: QStatus = 4110
ER_CRYPTO_KEY_UNAVAILABLE: QStatus = 4111
ER_BAD_HOSTNAME: QStatus = 4112
ER_CRYPTO_KEY_UNUSABLE: QStatus = 4113
ER_EMPTY_KEY_BLOB: QStatus = 4114
ER_CORRUPT_KEYBLOB: QStatus = 4115
ER_INVALID_KEY_ENCODING: QStatus = 4116
ER_DEAD_THREAD: QStatus = 4117
ER_THREAD_RUNNING: QStatus = 4118
ER_THREAD_STOPPING: QStatus = 4119
ER_BAD_STRING_ENCODING: QStatus = 4120
ER_CRYPTO_INSUFFICIENT_SECURITY: QStatus = 4121
ER_CRYPTO_ILLEGAL_PARAMETERS: QStatus = 4122
ER_CRYPTO_HASH_UNINITIALIZED: QStatus = 4123
ER_THREAD_NO_WAIT: QStatus = 4124
ER_TIMER_EXITING: QStatus = 4125
ER_INVALID_GUID: QStatus = 4126
ER_THREADPOOL_EXHAUSTED: QStatus = 4127
ER_THREADPOOL_STOPPING: QStatus = 4128
ER_INVALID_STREAM: QStatus = 4129
ER_TIMER_FULL: QStatus = 4130
ER_IODISPATCH_STOPPING: QStatus = 4131
ER_SLAP_INVALID_PACKET_LEN: QStatus = 4132
ER_SLAP_HDR_CHECKSUM_ERROR: QStatus = 4133
ER_SLAP_INVALID_PACKET_TYPE: QStatus = 4134
ER_SLAP_LEN_MISMATCH: QStatus = 4135
ER_SLAP_PACKET_TYPE_MISMATCH: QStatus = 4136
ER_SLAP_CRC_ERROR: QStatus = 4137
ER_SLAP_ERROR: QStatus = 4138
ER_SLAP_OTHER_END_CLOSED: QStatus = 4139
ER_TIMER_NOT_ALLOWED: QStatus = 4140
ER_NOT_CONN: QStatus = 4141
ER_XML_CONVERTER_ERROR: QStatus = 8192
ER_XML_INVALID_RULES_COUNT: QStatus = 8193
ER_XML_INTERFACE_MEMBERS_MISSING: QStatus = 8194
ER_XML_INVALID_MEMBER_TYPE: QStatus = 8195
ER_XML_INVALID_MEMBER_ACTION: QStatus = 8196
ER_XML_MEMBER_DENY_ACTION_WITH_OTHER: QStatus = 8197
ER_XML_INVALID_ANNOTATIONS_COUNT: QStatus = 8198
ER_XML_INVALID_ELEMENT_NAME: QStatus = 8199
ER_XML_INVALID_ATTRIBUTE_VALUE: QStatus = 8200
ER_XML_INVALID_SECURITY_LEVEL_ANNOTATION_VALUE: QStatus = 8201
ER_XML_INVALID_ELEMENT_CHILDREN_COUNT: QStatus = 8202
ER_XML_INVALID_POLICY_VERSION: QStatus = 8203
ER_XML_INVALID_POLICY_SERIAL_NUMBER: QStatus = 8204
ER_XML_INVALID_ACL_PEER_TYPE: QStatus = 8205
ER_XML_INVALID_ACL_PEER_CHILDREN_COUNT: QStatus = 8206
ER_XML_ACL_ALL_TYPE_PEER_WITH_OTHERS: QStatus = 8207
ER_XML_INVALID_ACL_PEER_PUBLIC_KEY: QStatus = 8208
ER_XML_ACL_PEER_NOT_UNIQUE: QStatus = 8209
ER_XML_ACL_PEER_PUBLIC_KEY_SET: QStatus = 8210
ER_XML_ACLS_MISSING: QStatus = 8211
ER_XML_ACL_PEERS_MISSING: QStatus = 8212
ER_XML_INVALID_OBJECT_PATH: QStatus = 8213
ER_XML_INVALID_INTERFACE_NAME: QStatus = 8214
ER_XML_INVALID_MEMBER_NAME: QStatus = 8215
ER_XML_INVALID_MANIFEST_VERSION: QStatus = 8216
ER_XML_INVALID_OID: QStatus = 8217
ER_XML_INVALID_BASE64: QStatus = 8218
ER_XML_INTERFACE_NAME_NOT_UNIQUE: QStatus = 8219
ER_XML_MEMBER_NAME_NOT_UNIQUE: QStatus = 8220
ER_XML_OBJECT_PATH_NOT_UNIQUE: QStatus = 8221
ER_XML_ANNOTATION_NOT_UNIQUE: QStatus = 8222
ER_NONE: QStatus = 65535
ER_BUS_ERRORS: QStatus = 36864
ER_BUS_READ_ERROR: QStatus = 36865
ER_BUS_WRITE_ERROR: QStatus = 36866
ER_BUS_BAD_VALUE_TYPE: QStatus = 36867
ER_BUS_BAD_HEADER_FIELD: QStatus = 36868
ER_BUS_BAD_SIGNATURE: QStatus = 36869
ER_BUS_BAD_OBJ_PATH: QStatus = 36870
ER_BUS_BAD_MEMBER_NAME: QStatus = 36871
ER_BUS_BAD_INTERFACE_NAME: QStatus = 36872
ER_BUS_BAD_ERROR_NAME: QStatus = 36873
ER_BUS_BAD_BUS_NAME: QStatus = 36874
ER_BUS_NAME_TOO_LONG: QStatus = 36875
ER_BUS_BAD_LENGTH: QStatus = 36876
ER_BUS_BAD_VALUE: QStatus = 36877
ER_BUS_BAD_HDR_FLAGS: QStatus = 36878
ER_BUS_BAD_BODY_LEN: QStatus = 36879
ER_BUS_BAD_HEADER_LEN: QStatus = 36880
ER_BUS_UNKNOWN_SERIAL: QStatus = 36881
ER_BUS_UNKNOWN_PATH: QStatus = 36882
ER_BUS_UNKNOWN_INTERFACE: QStatus = 36883
ER_BUS_ESTABLISH_FAILED: QStatus = 36884
ER_BUS_UNEXPECTED_SIGNATURE: QStatus = 36885
ER_BUS_INTERFACE_MISSING: QStatus = 36886
ER_BUS_PATH_MISSING: QStatus = 36887
ER_BUS_MEMBER_MISSING: QStatus = 36888
ER_BUS_REPLY_SERIAL_MISSING: QStatus = 36889
ER_BUS_ERROR_NAME_MISSING: QStatus = 36890
ER_BUS_INTERFACE_NO_SUCH_MEMBER: QStatus = 36891
ER_BUS_NO_SUCH_OBJECT: QStatus = 36892
ER_BUS_OBJECT_NO_SUCH_MEMBER: QStatus = 36893
ER_BUS_OBJECT_NO_SUCH_INTERFACE: QStatus = 36894
ER_BUS_NO_SUCH_INTERFACE: QStatus = 36895
ER_BUS_MEMBER_NO_SUCH_SIGNATURE: QStatus = 36896
ER_BUS_NOT_NUL_TERMINATED: QStatus = 36897
ER_BUS_NO_SUCH_PROPERTY: QStatus = 36898
ER_BUS_SET_WRONG_SIGNATURE: QStatus = 36899
ER_BUS_PROPERTY_VALUE_NOT_SET: QStatus = 36900
ER_BUS_PROPERTY_ACCESS_DENIED: QStatus = 36901
ER_BUS_NO_TRANSPORTS: QStatus = 36902
ER_BUS_BAD_TRANSPORT_ARGS: QStatus = 36903
ER_BUS_NO_ROUTE: QStatus = 36904
ER_BUS_NO_ENDPOINT: QStatus = 36905
ER_BUS_BAD_SEND_PARAMETER: QStatus = 36906
ER_BUS_UNMATCHED_REPLY_SERIAL: QStatus = 36907
ER_BUS_BAD_SENDER_ID: QStatus = 36908
ER_BUS_TRANSPORT_NOT_STARTED: QStatus = 36909
ER_BUS_EMPTY_MESSAGE: QStatus = 36910
ER_BUS_NOT_OWNER: QStatus = 36911
ER_BUS_SET_PROPERTY_REJECTED: QStatus = 36912
ER_BUS_CONNECT_FAILED: QStatus = 36913
ER_BUS_REPLY_IS_ERROR_MESSAGE: QStatus = 36914
ER_BUS_NOT_AUTHENTICATING: QStatus = 36915
ER_BUS_NO_LISTENER: QStatus = 36916
ER_BUS_NOT_ALLOWED: QStatus = 36918
ER_BUS_WRITE_QUEUE_FULL: QStatus = 36919
ER_BUS_ENDPOINT_CLOSING: QStatus = 36920
ER_BUS_INTERFACE_MISMATCH: QStatus = 36921
ER_BUS_MEMBER_ALREADY_EXISTS: QStatus = 36922
ER_BUS_PROPERTY_ALREADY_EXISTS: QStatus = 36923
ER_BUS_IFACE_ALREADY_EXISTS: QStatus = 36924
ER_BUS_ERROR_RESPONSE: QStatus = 36925
ER_BUS_BAD_XML: QStatus = 36926
ER_BUS_BAD_CHILD_PATH: QStatus = 36927
ER_BUS_OBJ_ALREADY_EXISTS: QStatus = 36928
ER_BUS_OBJ_NOT_FOUND: QStatus = 36929
ER_BUS_CANNOT_EXPAND_MESSAGE: QStatus = 36930
ER_BUS_NOT_COMPRESSED: QStatus = 36931
ER_BUS_ALREADY_CONNECTED: QStatus = 36932
ER_BUS_NOT_CONNECTED: QStatus = 36933
ER_BUS_ALREADY_LISTENING: QStatus = 36934
ER_BUS_KEY_UNAVAILABLE: QStatus = 36935
ER_BUS_TRUNCATED: QStatus = 36936
ER_BUS_KEY_STORE_NOT_LOADED: QStatus = 36937
ER_BUS_NO_AUTHENTICATION_MECHANISM: QStatus = 36938
ER_BUS_BUS_ALREADY_STARTED: QStatus = 36939
ER_BUS_BUS_NOT_STARTED: QStatus = 36940
ER_BUS_KEYBLOB_OP_INVALID: QStatus = 36941
ER_BUS_INVALID_HEADER_CHECKSUM: QStatus = 36942
ER_BUS_MESSAGE_NOT_ENCRYPTED: QStatus = 36943
ER_BUS_INVALID_HEADER_SERIAL: QStatus = 36944
ER_BUS_TIME_TO_LIVE_EXPIRED: QStatus = 36945
ER_BUS_HDR_EXPANSION_INVALID: QStatus = 36946
ER_BUS_MISSING_COMPRESSION_TOKEN: QStatus = 36947
ER_BUS_NO_PEER_GUID: QStatus = 36948
ER_BUS_MESSAGE_DECRYPTION_FAILED: QStatus = 36949
ER_BUS_SECURITY_FATAL: QStatus = 36950
ER_BUS_KEY_EXPIRED: QStatus = 36951
ER_BUS_CORRUPT_KEYSTORE: QStatus = 36952
ER_BUS_NO_CALL_FOR_REPLY: QStatus = 36953
ER_BUS_NOT_A_COMPLETE_TYPE: QStatus = 36954
ER_BUS_POLICY_VIOLATION: QStatus = 36955
ER_BUS_NO_SUCH_SERVICE: QStatus = 36956
ER_BUS_TRANSPORT_NOT_AVAILABLE: QStatus = 36957
ER_BUS_INVALID_AUTH_MECHANISM: QStatus = 36958
ER_BUS_KEYSTORE_VERSION_MISMATCH: QStatus = 36959
ER_BUS_BLOCKING_CALL_NOT_ALLOWED: QStatus = 36960
ER_BUS_SIGNATURE_MISMATCH: QStatus = 36961
ER_BUS_STOPPING: QStatus = 36962
ER_BUS_METHOD_CALL_ABORTED: QStatus = 36963
ER_BUS_CANNOT_ADD_INTERFACE: QStatus = 36964
ER_BUS_CANNOT_ADD_HANDLER: QStatus = 36965
ER_BUS_KEYSTORE_NOT_LOADED: QStatus = 36966
ER_BUS_NO_SUCH_HANDLE: QStatus = 36971
ER_BUS_HANDLES_NOT_ENABLED: QStatus = 36972
ER_BUS_HANDLES_MISMATCH: QStatus = 36973
ER_BUS_NO_SESSION: QStatus = 36975
ER_BUS_ELEMENT_NOT_FOUND: QStatus = 36976
ER_BUS_NOT_A_DICTIONARY: QStatus = 36977
ER_BUS_WAIT_FAILED: QStatus = 36978
ER_BUS_BAD_SESSION_OPTS: QStatus = 36980
ER_BUS_CONNECTION_REJECTED: QStatus = 36981
ER_DBUS_REQUEST_NAME_REPLY_PRIMARY_OWNER: QStatus = 36982
ER_DBUS_REQUEST_NAME_REPLY_IN_QUEUE: QStatus = 36983
ER_DBUS_REQUEST_NAME_REPLY_EXISTS: QStatus = 36984
ER_DBUS_REQUEST_NAME_REPLY_ALREADY_OWNER: QStatus = 36985
ER_DBUS_RELEASE_NAME_REPLY_RELEASED: QStatus = 36986
ER_DBUS_RELEASE_NAME_REPLY_NON_EXISTENT: QStatus = 36987
ER_DBUS_RELEASE_NAME_REPLY_NOT_OWNER: QStatus = 36988
ER_DBUS_START_REPLY_ALREADY_RUNNING: QStatus = 36990
ER_ALLJOYN_BINDSESSIONPORT_REPLY_ALREADY_EXISTS: QStatus = 36992
ER_ALLJOYN_BINDSESSIONPORT_REPLY_FAILED: QStatus = 36993
ER_ALLJOYN_JOINSESSION_REPLY_NO_SESSION: QStatus = 36995
ER_ALLJOYN_JOINSESSION_REPLY_UNREACHABLE: QStatus = 36996
ER_ALLJOYN_JOINSESSION_REPLY_CONNECT_FAILED: QStatus = 36997
ER_ALLJOYN_JOINSESSION_REPLY_REJECTED: QStatus = 36998
ER_ALLJOYN_JOINSESSION_REPLY_BAD_SESSION_OPTS: QStatus = 36999
ER_ALLJOYN_JOINSESSION_REPLY_FAILED: QStatus = 37000
ER_ALLJOYN_LEAVESESSION_REPLY_NO_SESSION: QStatus = 37002
ER_ALLJOYN_LEAVESESSION_REPLY_FAILED: QStatus = 37003
ER_ALLJOYN_ADVERTISENAME_REPLY_TRANSPORT_NOT_AVAILABLE: QStatus = 37004
ER_ALLJOYN_ADVERTISENAME_REPLY_ALREADY_ADVERTISING: QStatus = 37005
ER_ALLJOYN_ADVERTISENAME_REPLY_FAILED: QStatus = 37006
ER_ALLJOYN_CANCELADVERTISENAME_REPLY_FAILED: QStatus = 37008
ER_ALLJOYN_FINDADVERTISEDNAME_REPLY_TRANSPORT_NOT_AVAILABLE: QStatus = 37009
ER_ALLJOYN_FINDADVERTISEDNAME_REPLY_ALREADY_DISCOVERING: QStatus = 37010
ER_ALLJOYN_FINDADVERTISEDNAME_REPLY_FAILED: QStatus = 37011
ER_ALLJOYN_CANCELFINDADVERTISEDNAME_REPLY_FAILED: QStatus = 37013
ER_BUS_UNEXPECTED_DISPOSITION: QStatus = 37014
ER_BUS_INTERFACE_ACTIVATED: QStatus = 37015
ER_ALLJOYN_UNBINDSESSIONPORT_REPLY_BAD_PORT: QStatus = 37016
ER_ALLJOYN_UNBINDSESSIONPORT_REPLY_FAILED: QStatus = 37017
ER_ALLJOYN_BINDSESSIONPORT_REPLY_INVALID_OPTS: QStatus = 37018
ER_ALLJOYN_JOINSESSION_REPLY_ALREADY_JOINED: QStatus = 37019
ER_BUS_SELF_CONNECT: QStatus = 37020
ER_BUS_SECURITY_NOT_ENABLED: QStatus = 37021
ER_BUS_LISTENER_ALREADY_SET: QStatus = 37022
ER_BUS_PEER_AUTH_VERSION_MISMATCH: QStatus = 37023
ER_ALLJOYN_SETLINKTIMEOUT_REPLY_NOT_SUPPORTED: QStatus = 37024
ER_ALLJOYN_SETLINKTIMEOUT_REPLY_NO_DEST_SUPPORT: QStatus = 37025
ER_ALLJOYN_SETLINKTIMEOUT_REPLY_FAILED: QStatus = 37026
ER_ALLJOYN_ACCESS_PERMISSION_WARNING: QStatus = 37027
ER_ALLJOYN_ACCESS_PERMISSION_ERROR: QStatus = 37028
ER_BUS_DESTINATION_NOT_AUTHENTICATED: QStatus = 37029
ER_BUS_ENDPOINT_REDIRECTED: QStatus = 37030
ER_BUS_AUTHENTICATION_PENDING: QStatus = 37031
ER_BUS_NOT_AUTHORIZED: QStatus = 37032
ER_PACKET_BUS_NO_SUCH_CHANNEL: QStatus = 37033
ER_PACKET_BAD_FORMAT: QStatus = 37034
ER_PACKET_CONNECT_TIMEOUT: QStatus = 37035
ER_PACKET_CHANNEL_FAIL: QStatus = 37036
ER_PACKET_TOO_LARGE: QStatus = 37037
ER_PACKET_BAD_PARAMETER: QStatus = 37038
ER_PACKET_BAD_CRC: QStatus = 37039
ER_RENDEZVOUS_SERVER_DEACTIVATED_USER: QStatus = 37067
ER_RENDEZVOUS_SERVER_UNKNOWN_USER: QStatus = 37068
ER_UNABLE_TO_CONNECT_TO_RENDEZVOUS_SERVER: QStatus = 37069
ER_NOT_CONNECTED_TO_RENDEZVOUS_SERVER: QStatus = 37070
ER_UNABLE_TO_SEND_MESSAGE_TO_RENDEZVOUS_SERVER: QStatus = 37071
ER_INVALID_RENDEZVOUS_SERVER_INTERFACE_MESSAGE: QStatus = 37072
ER_INVALID_PERSISTENT_CONNECTION_MESSAGE_RESPONSE: QStatus = 37073
ER_INVALID_ON_DEMAND_CONNECTION_MESSAGE_RESPONSE: QStatus = 37074
ER_INVALID_HTTP_METHOD_USED_FOR_RENDEZVOUS_SERVER_INTERFACE_MESSAGE: QStatus = 37075
ER_RENDEZVOUS_SERVER_ERR500_INTERNAL_ERROR: QStatus = 37076
ER_RENDEZVOUS_SERVER_ERR503_STATUS_UNAVAILABLE: QStatus = 37077
ER_RENDEZVOUS_SERVER_ERR401_UNAUTHORIZED_REQUEST: QStatus = 37078
ER_RENDEZVOUS_SERVER_UNRECOVERABLE_ERROR: QStatus = 37079
ER_RENDEZVOUS_SERVER_ROOT_CERTIFICATE_UNINITIALIZED: QStatus = 37080
ER_BUS_NO_SUCH_ANNOTATION: QStatus = 37081
ER_BUS_ANNOTATION_ALREADY_EXISTS: QStatus = 37082
ER_SOCK_CLOSING: QStatus = 37083
ER_NO_SUCH_DEVICE: QStatus = 37084
ER_P2P: QStatus = 37085
ER_P2P_TIMEOUT: QStatus = 37086
ER_P2P_NOT_CONNECTED: QStatus = 37087
ER_BAD_TRANSPORT_MASK: QStatus = 37088
ER_PROXIMITY_CONNECTION_ESTABLISH_FAIL: QStatus = 37089
ER_PROXIMITY_NO_PEERS_FOUND: QStatus = 37090
ER_BUS_OBJECT_NOT_REGISTERED: QStatus = 37091
ER_P2P_DISABLED: QStatus = 37092
ER_P2P_BUSY: QStatus = 37093
ER_BUS_INCOMPATIBLE_DAEMON: QStatus = 37094
ER_P2P_NO_GO: QStatus = 37095
ER_P2P_NO_STA: QStatus = 37096
ER_P2P_FORBIDDEN: QStatus = 37097
ER_ALLJOYN_ONAPPSUSPEND_REPLY_FAILED: QStatus = 37098
ER_ALLJOYN_ONAPPSUSPEND_REPLY_UNSUPPORTED: QStatus = 37099
ER_ALLJOYN_ONAPPRESUME_REPLY_FAILED: QStatus = 37100
ER_ALLJOYN_ONAPPRESUME_REPLY_UNSUPPORTED: QStatus = 37101
ER_BUS_NO_SUCH_MESSAGE: QStatus = 37102
ER_ALLJOYN_REMOVESESSIONMEMBER_REPLY_NO_SESSION: QStatus = 37103
ER_ALLJOYN_REMOVESESSIONMEMBER_NOT_BINDER: QStatus = 37104
ER_ALLJOYN_REMOVESESSIONMEMBER_NOT_MULTIPOINT: QStatus = 37105
ER_ALLJOYN_REMOVESESSIONMEMBER_NOT_FOUND: QStatus = 37106
ER_ALLJOYN_REMOVESESSIONMEMBER_INCOMPATIBLE_REMOTE_DAEMON: QStatus = 37107
ER_ALLJOYN_REMOVESESSIONMEMBER_REPLY_FAILED: QStatus = 37108
ER_BUS_REMOVED_BY_BINDER: QStatus = 37109
ER_BUS_MATCH_RULE_NOT_FOUND: QStatus = 37110
ER_ALLJOYN_PING_FAILED: QStatus = 37111
ER_ALLJOYN_PING_REPLY_UNREACHABLE: QStatus = 37112
ER_UDP_MSG_TOO_LONG: QStatus = 37113
ER_UDP_DEMUX_NO_ENDPOINT: QStatus = 37114
ER_UDP_NO_NETWORK: QStatus = 37115
ER_UDP_UNEXPECTED_LENGTH: QStatus = 37116
ER_UDP_UNEXPECTED_FLOW: QStatus = 37117
ER_UDP_DISCONNECT: QStatus = 37118
ER_UDP_NOT_IMPLEMENTED: QStatus = 37119
ER_UDP_NO_LISTENER: QStatus = 37120
ER_UDP_STOPPING: QStatus = 37121
ER_ARDP_BACKPRESSURE: QStatus = 37122
ER_UDP_BACKPRESSURE: QStatus = 37123
ER_ARDP_INVALID_STATE: QStatus = 37124
ER_ARDP_TTL_EXPIRED: QStatus = 37125
ER_ARDP_PERSIST_TIMEOUT: QStatus = 37126
ER_ARDP_PROBE_TIMEOUT: QStatus = 37127
ER_ARDP_REMOTE_CONNECTION_RESET: QStatus = 37128
ER_UDP_BUSHELLO: QStatus = 37129
ER_UDP_MESSAGE: QStatus = 37130
ER_UDP_INVALID: QStatus = 37131
ER_UDP_UNSUPPORTED: QStatus = 37132
ER_UDP_ENDPOINT_STALLED: QStatus = 37133
ER_ARDP_INVALID_RESPONSE: QStatus = 37134
ER_ARDP_INVALID_CONNECTION: QStatus = 37135
ER_UDP_LOCAL_DISCONNECT: QStatus = 37136
ER_UDP_EARLY_EXIT: QStatus = 37137
ER_UDP_LOCAL_DISCONNECT_FAIL: QStatus = 37138
ER_ARDP_DISCONNECTING: QStatus = 37139
ER_ALLJOYN_PING_REPLY_INCOMPATIBLE_REMOTE_ROUTING_NODE: QStatus = 37140
ER_ALLJOYN_PING_REPLY_TIMEOUT: QStatus = 37141
ER_ALLJOYN_PING_REPLY_UNKNOWN_NAME: QStatus = 37142
ER_ALLJOYN_PING_REPLY_FAILED: QStatus = 37143
ER_TCP_MAX_UNTRUSTED: QStatus = 37144
ER_ALLJOYN_PING_REPLY_IN_PROGRESS: QStatus = 37145
ER_LANGUAGE_NOT_SUPPORTED: QStatus = 37146
ER_ABOUT_FIELD_ALREADY_SPECIFIED: QStatus = 37147
ER_UDP_NOT_DISCONNECTED: QStatus = 37148
ER_UDP_ENDPOINT_NOT_STARTED: QStatus = 37149
ER_UDP_ENDPOINT_REMOVED: QStatus = 37150
ER_ARDP_VERSION_NOT_SUPPORTED: QStatus = 37151
ER_CONNECTION_LIMIT_EXCEEDED: QStatus = 37152
ER_ARDP_WRITE_BLOCKED: QStatus = 37153
ER_PERMISSION_DENIED: QStatus = 37154
ER_ABOUT_DEFAULT_LANGUAGE_NOT_SPECIFIED: QStatus = 37155
ER_ABOUT_SESSIONPORT_NOT_BOUND: QStatus = 37156
ER_ABOUT_ABOUTDATA_MISSING_REQUIRED_FIELD: QStatus = 37157
ER_ABOUT_INVALID_ABOUTDATA_LISTENER: QStatus = 37158
ER_BUS_PING_GROUP_NOT_FOUND: QStatus = 37159
ER_BUS_REMOVED_BY_BINDER_SELF: QStatus = 37160
ER_INVALID_CONFIG: QStatus = 37161
ER_ABOUT_INVALID_ABOUTDATA_FIELD_VALUE: QStatus = 37162
ER_ABOUT_INVALID_ABOUTDATA_FIELD_APPID_SIZE: QStatus = 37163
ER_BUS_TRANSPORT_ACCESS_DENIED: QStatus = 37164
ER_INVALID_CERTIFICATE: QStatus = 37165
ER_CERTIFICATE_NOT_FOUND: QStatus = 37166
ER_DUPLICATE_CERTIFICATE: QStatus = 37167
ER_UNKNOWN_CERTIFICATE: QStatus = 37168
ER_MISSING_DIGEST_IN_CERTIFICATE: QStatus = 37169
ER_DIGEST_MISMATCH: QStatus = 37170
ER_DUPLICATE_KEY: QStatus = 37171
ER_NO_COMMON_TRUST: QStatus = 37172
ER_MANIFEST_NOT_FOUND: QStatus = 37173
ER_INVALID_CERT_CHAIN: QStatus = 37174
ER_NO_TRUST_ANCHOR: QStatus = 37175
ER_INVALID_APPLICATION_STATE: QStatus = 37176
ER_FEATURE_NOT_AVAILABLE: QStatus = 37177
ER_KEY_STORE_ALREADY_INITIALIZED: QStatus = 37178
ER_KEY_STORE_ID_NOT_YET_SET: QStatus = 37179
ER_POLICY_NOT_NEWER: QStatus = 37180
ER_MANIFEST_REJECTED: QStatus = 37181
ER_INVALID_CERTIFICATE_USAGE: QStatus = 37182
ER_INVALID_SIGNAL_EMISSION_TYPE: QStatus = 37183
ER_APPLICATION_STATE_LISTENER_ALREADY_EXISTS: QStatus = 37184
ER_APPLICATION_STATE_LISTENER_NO_SUCH_LISTENER: QStatus = 37185
ER_MANAGEMENT_ALREADY_STARTED: QStatus = 37186
ER_MANAGEMENT_NOT_STARTED: QStatus = 37187
ER_BUS_DESCRIPTION_ALREADY_EXISTS: QStatus = 37188
make_head(_module, '_alljoyn_abouticon_handle')
make_head(_module, '_alljoyn_abouticonobj_handle')
make_head(_module, '_alljoyn_abouticonproxy_handle')
make_head(_module, 'alljoyn_about_announced_ptr')
make_head(_module, 'alljoyn_aboutdatalistener_callbacks')
make_head(_module, 'alljoyn_aboutdatalistener_getaboutdata_ptr')
make_head(_module, 'alljoyn_aboutdatalistener_getannouncedaboutdata_ptr')
make_head(_module, 'alljoyn_aboutlistener_callback')
make_head(_module, 'alljoyn_applicationstatelistener_callbacks')
make_head(_module, 'alljoyn_applicationstatelistener_state_ptr')
make_head(_module, 'alljoyn_authlistener_authenticationcomplete_ptr')
make_head(_module, 'alljoyn_authlistener_callbacks')
make_head(_module, 'alljoyn_authlistener_requestcredentials_ptr')
make_head(_module, 'alljoyn_authlistener_requestcredentialsasync_ptr')
make_head(_module, 'alljoyn_authlistener_securityviolation_ptr')
make_head(_module, 'alljoyn_authlistener_verifycredentials_ptr')
make_head(_module, 'alljoyn_authlistener_verifycredentialsasync_ptr')
make_head(_module, 'alljoyn_authlistenerasync_callbacks')
make_head(_module, 'alljoyn_autopinger_destination_found_ptr')
make_head(_module, 'alljoyn_autopinger_destination_lost_ptr')
make_head(_module, 'alljoyn_busattachment_joinsessioncb_ptr')
make_head(_module, 'alljoyn_busattachment_setlinktimeoutcb_ptr')
make_head(_module, 'alljoyn_buslistener_bus_disconnected_ptr')
make_head(_module, 'alljoyn_buslistener_bus_prop_changed_ptr')
make_head(_module, 'alljoyn_buslistener_bus_stopping_ptr')
make_head(_module, 'alljoyn_buslistener_callbacks')
make_head(_module, 'alljoyn_buslistener_found_advertised_name_ptr')
make_head(_module, 'alljoyn_buslistener_listener_registered_ptr')
make_head(_module, 'alljoyn_buslistener_listener_unregistered_ptr')
make_head(_module, 'alljoyn_buslistener_lost_advertised_name_ptr')
make_head(_module, 'alljoyn_buslistener_name_owner_changed_ptr')
make_head(_module, 'alljoyn_busobject_callbacks')
make_head(_module, 'alljoyn_busobject_methodentry')
make_head(_module, 'alljoyn_busobject_object_registration_ptr')
make_head(_module, 'alljoyn_busobject_prop_get_ptr')
make_head(_module, 'alljoyn_busobject_prop_set_ptr')
make_head(_module, 'alljoyn_certificateid')
make_head(_module, 'alljoyn_certificateidarray')
make_head(_module, 'alljoyn_interfacedescription_member')
make_head(_module, 'alljoyn_interfacedescription_property')
make_head(_module, 'alljoyn_interfacedescription_translation_callback_ptr')
make_head(_module, 'alljoyn_keystorelistener_acquireexclusivelock_ptr')
make_head(_module, 'alljoyn_keystorelistener_callbacks')
make_head(_module, 'alljoyn_keystorelistener_loadrequest_ptr')
make_head(_module, 'alljoyn_keystorelistener_releaseexclusivelock_ptr')
make_head(_module, 'alljoyn_keystorelistener_storerequest_ptr')
make_head(_module, 'alljoyn_keystorelistener_with_synchronization_callbacks')
make_head(_module, 'alljoyn_manifestarray')
make_head(_module, 'alljoyn_messagereceiver_methodhandler_ptr')
make_head(_module, 'alljoyn_messagereceiver_replyhandler_ptr')
make_head(_module, 'alljoyn_messagereceiver_signalhandler_ptr')
make_head(_module, 'alljoyn_observer_object_discovered_ptr')
make_head(_module, 'alljoyn_observer_object_lost_ptr')
make_head(_module, 'alljoyn_observerlistener_callback')
make_head(_module, 'alljoyn_permissionconfigurationlistener_callbacks')
make_head(_module, 'alljoyn_permissionconfigurationlistener_endmanagement_ptr')
make_head(_module, 'alljoyn_permissionconfigurationlistener_factoryreset_ptr')
make_head(_module, 'alljoyn_permissionconfigurationlistener_policychanged_ptr')
make_head(_module, 'alljoyn_permissionconfigurationlistener_startmanagement_ptr')
make_head(_module, 'alljoyn_pinglistener_callback')
make_head(_module, 'alljoyn_proxybusobject_listener_getallpropertiescb_ptr')
make_head(_module, 'alljoyn_proxybusobject_listener_getpropertycb_ptr')
make_head(_module, 'alljoyn_proxybusobject_listener_introspectcb_ptr')
make_head(_module, 'alljoyn_proxybusobject_listener_propertieschanged_ptr')
make_head(_module, 'alljoyn_proxybusobject_listener_setpropertycb_ptr')
make_head(_module, 'alljoyn_sessionlistener_callbacks')
make_head(_module, 'alljoyn_sessionlistener_sessionlost_ptr')
make_head(_module, 'alljoyn_sessionlistener_sessionmemberadded_ptr')
make_head(_module, 'alljoyn_sessionlistener_sessionmemberremoved_ptr')
make_head(_module, 'alljoyn_sessionportlistener_acceptsessionjoiner_ptr')
make_head(_module, 'alljoyn_sessionportlistener_callbacks')
make_head(_module, 'alljoyn_sessionportlistener_sessionjoined_ptr')
__all__ = [
    "AJ_IFC_SECURITY_INHERIT",
    "AJ_IFC_SECURITY_OFF",
    "AJ_IFC_SECURITY_REQUIRED",
    "ALLJOYN_ARRAY",
    "ALLJOYN_BIG_ENDIAN",
    "ALLJOYN_BOOLEAN",
    "ALLJOYN_BOOLEAN_ARRAY",
    "ALLJOYN_BYTE",
    "ALLJOYN_BYTE_ARRAY",
    "ALLJOYN_CRED_CERT_CHAIN",
    "ALLJOYN_CRED_EXPIRATION",
    "ALLJOYN_CRED_LOGON_ENTRY",
    "ALLJOYN_CRED_NEW_PASSWORD",
    "ALLJOYN_CRED_ONE_TIME_PWD",
    "ALLJOYN_CRED_PASSWORD",
    "ALLJOYN_CRED_PRIVATE_KEY",
    "ALLJOYN_CRED_USER_NAME",
    "ALLJOYN_DICT_ENTRY",
    "ALLJOYN_DICT_ENTRY_CLOSE",
    "ALLJOYN_DICT_ENTRY_OPEN",
    "ALLJOYN_DISCONNECTED",
    "ALLJOYN_DOUBLE",
    "ALLJOYN_DOUBLE_ARRAY",
    "ALLJOYN_HANDLE",
    "ALLJOYN_INT16",
    "ALLJOYN_INT16_ARRAY",
    "ALLJOYN_INT32",
    "ALLJOYN_INT32_ARRAY",
    "ALLJOYN_INT64",
    "ALLJOYN_INT64_ARRAY",
    "ALLJOYN_INVALID",
    "ALLJOYN_LITTLE_ENDIAN",
    "ALLJOYN_MEMBER_ANNOTATE_DEPRECATED",
    "ALLJOYN_MEMBER_ANNOTATE_GLOBAL_BROADCAST",
    "ALLJOYN_MEMBER_ANNOTATE_NO_REPLY",
    "ALLJOYN_MEMBER_ANNOTATE_SESSIONCAST",
    "ALLJOYN_MEMBER_ANNOTATE_SESSIONLESS",
    "ALLJOYN_MEMBER_ANNOTATE_UNICAST",
    "ALLJOYN_MESSAGE_DEFAULT_TIMEOUT",
    "ALLJOYN_MESSAGE_ERROR",
    "ALLJOYN_MESSAGE_FLAG_ALLOW_REMOTE_MSG",
    "ALLJOYN_MESSAGE_FLAG_AUTO_START",
    "ALLJOYN_MESSAGE_FLAG_ENCRYPTED",
    "ALLJOYN_MESSAGE_FLAG_GLOBAL_BROADCAST",
    "ALLJOYN_MESSAGE_FLAG_NO_REPLY_EXPECTED",
    "ALLJOYN_MESSAGE_FLAG_SESSIONLESS",
    "ALLJOYN_MESSAGE_INVALID",
    "ALLJOYN_MESSAGE_METHOD_CALL",
    "ALLJOYN_MESSAGE_METHOD_RET",
    "ALLJOYN_MESSAGE_SIGNAL",
    "ALLJOYN_NAMED_PIPE_CONNECT_SPEC",
    "ALLJOYN_OBJECT_PATH",
    "ALLJOYN_PROP_ACCESS_READ",
    "ALLJOYN_PROP_ACCESS_RW",
    "ALLJOYN_PROP_ACCESS_WRITE",
    "ALLJOYN_PROXIMITY_ANY",
    "ALLJOYN_PROXIMITY_NETWORK",
    "ALLJOYN_PROXIMITY_PHYSICAL",
    "ALLJOYN_READ_READY",
    "ALLJOYN_SESSIONLOST_INVALID",
    "ALLJOYN_SESSIONLOST_LINK_TIMEOUT",
    "ALLJOYN_SESSIONLOST_REASON_OTHER",
    "ALLJOYN_SESSIONLOST_REMOTE_END_CLOSED_ABRUPTLY",
    "ALLJOYN_SESSIONLOST_REMOTE_END_LEFT_SESSION",
    "ALLJOYN_SESSIONLOST_REMOVED_BY_BINDER",
    "ALLJOYN_SIGNATURE",
    "ALLJOYN_STRING",
    "ALLJOYN_STRUCT",
    "ALLJOYN_STRUCT_CLOSE",
    "ALLJOYN_STRUCT_OPEN",
    "ALLJOYN_TRAFFIC_TYPE_MESSAGES",
    "ALLJOYN_TRAFFIC_TYPE_RAW_RELIABLE",
    "ALLJOYN_TRAFFIC_TYPE_RAW_UNRELIABLE",
    "ALLJOYN_UINT16",
    "ALLJOYN_UINT16_ARRAY",
    "ALLJOYN_UINT32",
    "ALLJOYN_UINT32_ARRAY",
    "ALLJOYN_UINT64",
    "ALLJOYN_UINT64_ARRAY",
    "ALLJOYN_VARIANT",
    "ALLJOYN_WILDCARD",
    "ALLJOYN_WRITE_READY",
    "ANNOUNCED",
    "AllJoynAcceptBusConnection",
    "AllJoynCloseBusHandle",
    "AllJoynConnectToBus",
    "AllJoynCreateBus",
    "AllJoynEnumEvents",
    "AllJoynEventSelect",
    "AllJoynReceiveFromBus",
    "AllJoynSendToBus",
    "CAPABLE_ECDHE_ECDSA",
    "CAPABLE_ECDHE_NULL",
    "CAPABLE_ECDHE_SPEKE",
    "CLAIMABLE",
    "CLAIMED",
    "ER_ABOUT_ABOUTDATA_MISSING_REQUIRED_FIELD",
    "ER_ABOUT_DEFAULT_LANGUAGE_NOT_SPECIFIED",
    "ER_ABOUT_FIELD_ALREADY_SPECIFIED",
    "ER_ABOUT_INVALID_ABOUTDATA_FIELD_APPID_SIZE",
    "ER_ABOUT_INVALID_ABOUTDATA_FIELD_VALUE",
    "ER_ABOUT_INVALID_ABOUTDATA_LISTENER",
    "ER_ABOUT_SESSIONPORT_NOT_BOUND",
    "ER_ALERTED_THREAD",
    "ER_ALLJOYN_ACCESS_PERMISSION_ERROR",
    "ER_ALLJOYN_ACCESS_PERMISSION_WARNING",
    "ER_ALLJOYN_ADVERTISENAME_REPLY_ALREADY_ADVERTISING",
    "ER_ALLJOYN_ADVERTISENAME_REPLY_FAILED",
    "ER_ALLJOYN_ADVERTISENAME_REPLY_TRANSPORT_NOT_AVAILABLE",
    "ER_ALLJOYN_BINDSESSIONPORT_REPLY_ALREADY_EXISTS",
    "ER_ALLJOYN_BINDSESSIONPORT_REPLY_FAILED",
    "ER_ALLJOYN_BINDSESSIONPORT_REPLY_INVALID_OPTS",
    "ER_ALLJOYN_CANCELADVERTISENAME_REPLY_FAILED",
    "ER_ALLJOYN_CANCELFINDADVERTISEDNAME_REPLY_FAILED",
    "ER_ALLJOYN_FINDADVERTISEDNAME_REPLY_ALREADY_DISCOVERING",
    "ER_ALLJOYN_FINDADVERTISEDNAME_REPLY_FAILED",
    "ER_ALLJOYN_FINDADVERTISEDNAME_REPLY_TRANSPORT_NOT_AVAILABLE",
    "ER_ALLJOYN_JOINSESSION_REPLY_ALREADY_JOINED",
    "ER_ALLJOYN_JOINSESSION_REPLY_BAD_SESSION_OPTS",
    "ER_ALLJOYN_JOINSESSION_REPLY_CONNECT_FAILED",
    "ER_ALLJOYN_JOINSESSION_REPLY_FAILED",
    "ER_ALLJOYN_JOINSESSION_REPLY_NO_SESSION",
    "ER_ALLJOYN_JOINSESSION_REPLY_REJECTED",
    "ER_ALLJOYN_JOINSESSION_REPLY_UNREACHABLE",
    "ER_ALLJOYN_LEAVESESSION_REPLY_FAILED",
    "ER_ALLJOYN_LEAVESESSION_REPLY_NO_SESSION",
    "ER_ALLJOYN_ONAPPRESUME_REPLY_FAILED",
    "ER_ALLJOYN_ONAPPRESUME_REPLY_UNSUPPORTED",
    "ER_ALLJOYN_ONAPPSUSPEND_REPLY_FAILED",
    "ER_ALLJOYN_ONAPPSUSPEND_REPLY_UNSUPPORTED",
    "ER_ALLJOYN_PING_FAILED",
    "ER_ALLJOYN_PING_REPLY_FAILED",
    "ER_ALLJOYN_PING_REPLY_INCOMPATIBLE_REMOTE_ROUTING_NODE",
    "ER_ALLJOYN_PING_REPLY_IN_PROGRESS",
    "ER_ALLJOYN_PING_REPLY_TIMEOUT",
    "ER_ALLJOYN_PING_REPLY_UNKNOWN_NAME",
    "ER_ALLJOYN_PING_REPLY_UNREACHABLE",
    "ER_ALLJOYN_REMOVESESSIONMEMBER_INCOMPATIBLE_REMOTE_DAEMON",
    "ER_ALLJOYN_REMOVESESSIONMEMBER_NOT_BINDER",
    "ER_ALLJOYN_REMOVESESSIONMEMBER_NOT_FOUND",
    "ER_ALLJOYN_REMOVESESSIONMEMBER_NOT_MULTIPOINT",
    "ER_ALLJOYN_REMOVESESSIONMEMBER_REPLY_FAILED",
    "ER_ALLJOYN_REMOVESESSIONMEMBER_REPLY_NO_SESSION",
    "ER_ALLJOYN_SETLINKTIMEOUT_REPLY_FAILED",
    "ER_ALLJOYN_SETLINKTIMEOUT_REPLY_NOT_SUPPORTED",
    "ER_ALLJOYN_SETLINKTIMEOUT_REPLY_NO_DEST_SUPPORT",
    "ER_ALLJOYN_UNBINDSESSIONPORT_REPLY_BAD_PORT",
    "ER_ALLJOYN_UNBINDSESSIONPORT_REPLY_FAILED",
    "ER_APPLICATION_STATE_LISTENER_ALREADY_EXISTS",
    "ER_APPLICATION_STATE_LISTENER_NO_SUCH_LISTENER",
    "ER_ARDP_BACKPRESSURE",
    "ER_ARDP_DISCONNECTING",
    "ER_ARDP_INVALID_CONNECTION",
    "ER_ARDP_INVALID_RESPONSE",
    "ER_ARDP_INVALID_STATE",
    "ER_ARDP_PERSIST_TIMEOUT",
    "ER_ARDP_PROBE_TIMEOUT",
    "ER_ARDP_REMOTE_CONNECTION_RESET",
    "ER_ARDP_TTL_EXPIRED",
    "ER_ARDP_VERSION_NOT_SUPPORTED",
    "ER_ARDP_WRITE_BLOCKED",
    "ER_AUTH_FAIL",
    "ER_AUTH_USER_REJECT",
    "ER_BAD_ARG_1",
    "ER_BAD_ARG_2",
    "ER_BAD_ARG_3",
    "ER_BAD_ARG_4",
    "ER_BAD_ARG_5",
    "ER_BAD_ARG_6",
    "ER_BAD_ARG_7",
    "ER_BAD_ARG_8",
    "ER_BAD_ARG_COUNT",
    "ER_BAD_HOSTNAME",
    "ER_BAD_STRING_ENCODING",
    "ER_BAD_TRANSPORT_MASK",
    "ER_BUFFER_TOO_SMALL",
    "ER_BUS_ALREADY_CONNECTED",
    "ER_BUS_ALREADY_LISTENING",
    "ER_BUS_ANNOTATION_ALREADY_EXISTS",
    "ER_BUS_AUTHENTICATION_PENDING",
    "ER_BUS_BAD_BODY_LEN",
    "ER_BUS_BAD_BUS_NAME",
    "ER_BUS_BAD_CHILD_PATH",
    "ER_BUS_BAD_ERROR_NAME",
    "ER_BUS_BAD_HDR_FLAGS",
    "ER_BUS_BAD_HEADER_FIELD",
    "ER_BUS_BAD_HEADER_LEN",
    "ER_BUS_BAD_INTERFACE_NAME",
    "ER_BUS_BAD_LENGTH",
    "ER_BUS_BAD_MEMBER_NAME",
    "ER_BUS_BAD_OBJ_PATH",
    "ER_BUS_BAD_SENDER_ID",
    "ER_BUS_BAD_SEND_PARAMETER",
    "ER_BUS_BAD_SESSION_OPTS",
    "ER_BUS_BAD_SIGNATURE",
    "ER_BUS_BAD_TRANSPORT_ARGS",
    "ER_BUS_BAD_VALUE",
    "ER_BUS_BAD_VALUE_TYPE",
    "ER_BUS_BAD_XML",
    "ER_BUS_BLOCKING_CALL_NOT_ALLOWED",
    "ER_BUS_BUS_ALREADY_STARTED",
    "ER_BUS_BUS_NOT_STARTED",
    "ER_BUS_CANNOT_ADD_HANDLER",
    "ER_BUS_CANNOT_ADD_INTERFACE",
    "ER_BUS_CANNOT_EXPAND_MESSAGE",
    "ER_BUS_CONNECTION_REJECTED",
    "ER_BUS_CONNECT_FAILED",
    "ER_BUS_CORRUPT_KEYSTORE",
    "ER_BUS_DESCRIPTION_ALREADY_EXISTS",
    "ER_BUS_DESTINATION_NOT_AUTHENTICATED",
    "ER_BUS_ELEMENT_NOT_FOUND",
    "ER_BUS_EMPTY_MESSAGE",
    "ER_BUS_ENDPOINT_CLOSING",
    "ER_BUS_ENDPOINT_REDIRECTED",
    "ER_BUS_ERRORS",
    "ER_BUS_ERROR_NAME_MISSING",
    "ER_BUS_ERROR_RESPONSE",
    "ER_BUS_ESTABLISH_FAILED",
    "ER_BUS_HANDLES_MISMATCH",
    "ER_BUS_HANDLES_NOT_ENABLED",
    "ER_BUS_HDR_EXPANSION_INVALID",
    "ER_BUS_IFACE_ALREADY_EXISTS",
    "ER_BUS_INCOMPATIBLE_DAEMON",
    "ER_BUS_INTERFACE_ACTIVATED",
    "ER_BUS_INTERFACE_MISMATCH",
    "ER_BUS_INTERFACE_MISSING",
    "ER_BUS_INTERFACE_NO_SUCH_MEMBER",
    "ER_BUS_INVALID_AUTH_MECHANISM",
    "ER_BUS_INVALID_HEADER_CHECKSUM",
    "ER_BUS_INVALID_HEADER_SERIAL",
    "ER_BUS_KEYBLOB_OP_INVALID",
    "ER_BUS_KEYSTORE_NOT_LOADED",
    "ER_BUS_KEYSTORE_VERSION_MISMATCH",
    "ER_BUS_KEY_EXPIRED",
    "ER_BUS_KEY_STORE_NOT_LOADED",
    "ER_BUS_KEY_UNAVAILABLE",
    "ER_BUS_LISTENER_ALREADY_SET",
    "ER_BUS_MATCH_RULE_NOT_FOUND",
    "ER_BUS_MEMBER_ALREADY_EXISTS",
    "ER_BUS_MEMBER_MISSING",
    "ER_BUS_MEMBER_NO_SUCH_SIGNATURE",
    "ER_BUS_MESSAGE_DECRYPTION_FAILED",
    "ER_BUS_MESSAGE_NOT_ENCRYPTED",
    "ER_BUS_METHOD_CALL_ABORTED",
    "ER_BUS_MISSING_COMPRESSION_TOKEN",
    "ER_BUS_NAME_TOO_LONG",
    "ER_BUS_NOT_ALLOWED",
    "ER_BUS_NOT_AUTHENTICATING",
    "ER_BUS_NOT_AUTHORIZED",
    "ER_BUS_NOT_A_COMPLETE_TYPE",
    "ER_BUS_NOT_A_DICTIONARY",
    "ER_BUS_NOT_COMPRESSED",
    "ER_BUS_NOT_CONNECTED",
    "ER_BUS_NOT_NUL_TERMINATED",
    "ER_BUS_NOT_OWNER",
    "ER_BUS_NO_AUTHENTICATION_MECHANISM",
    "ER_BUS_NO_CALL_FOR_REPLY",
    "ER_BUS_NO_ENDPOINT",
    "ER_BUS_NO_LISTENER",
    "ER_BUS_NO_PEER_GUID",
    "ER_BUS_NO_ROUTE",
    "ER_BUS_NO_SESSION",
    "ER_BUS_NO_SUCH_ANNOTATION",
    "ER_BUS_NO_SUCH_HANDLE",
    "ER_BUS_NO_SUCH_INTERFACE",
    "ER_BUS_NO_SUCH_MESSAGE",
    "ER_BUS_NO_SUCH_OBJECT",
    "ER_BUS_NO_SUCH_PROPERTY",
    "ER_BUS_NO_SUCH_SERVICE",
    "ER_BUS_NO_TRANSPORTS",
    "ER_BUS_OBJECT_NOT_REGISTERED",
    "ER_BUS_OBJECT_NO_SUCH_INTERFACE",
    "ER_BUS_OBJECT_NO_SUCH_MEMBER",
    "ER_BUS_OBJ_ALREADY_EXISTS",
    "ER_BUS_OBJ_NOT_FOUND",
    "ER_BUS_PATH_MISSING",
    "ER_BUS_PEER_AUTH_VERSION_MISMATCH",
    "ER_BUS_PING_GROUP_NOT_FOUND",
    "ER_BUS_POLICY_VIOLATION",
    "ER_BUS_PROPERTY_ACCESS_DENIED",
    "ER_BUS_PROPERTY_ALREADY_EXISTS",
    "ER_BUS_PROPERTY_VALUE_NOT_SET",
    "ER_BUS_READ_ERROR",
    "ER_BUS_REMOVED_BY_BINDER",
    "ER_BUS_REMOVED_BY_BINDER_SELF",
    "ER_BUS_REPLY_IS_ERROR_MESSAGE",
    "ER_BUS_REPLY_SERIAL_MISSING",
    "ER_BUS_SECURITY_FATAL",
    "ER_BUS_SECURITY_NOT_ENABLED",
    "ER_BUS_SELF_CONNECT",
    "ER_BUS_SET_PROPERTY_REJECTED",
    "ER_BUS_SET_WRONG_SIGNATURE",
    "ER_BUS_SIGNATURE_MISMATCH",
    "ER_BUS_STOPPING",
    "ER_BUS_TIME_TO_LIVE_EXPIRED",
    "ER_BUS_TRANSPORT_ACCESS_DENIED",
    "ER_BUS_TRANSPORT_NOT_AVAILABLE",
    "ER_BUS_TRANSPORT_NOT_STARTED",
    "ER_BUS_TRUNCATED",
    "ER_BUS_UNEXPECTED_DISPOSITION",
    "ER_BUS_UNEXPECTED_SIGNATURE",
    "ER_BUS_UNKNOWN_INTERFACE",
    "ER_BUS_UNKNOWN_PATH",
    "ER_BUS_UNKNOWN_SERIAL",
    "ER_BUS_UNMATCHED_REPLY_SERIAL",
    "ER_BUS_WAIT_FAILED",
    "ER_BUS_WRITE_ERROR",
    "ER_BUS_WRITE_QUEUE_FULL",
    "ER_CERTIFICATE_NOT_FOUND",
    "ER_COMMON_ERRORS",
    "ER_CONNECTION_LIMIT_EXCEEDED",
    "ER_CONN_REFUSED",
    "ER_CORRUPT_KEYBLOB",
    "ER_CRYPTO_ERROR",
    "ER_CRYPTO_HASH_UNINITIALIZED",
    "ER_CRYPTO_ILLEGAL_PARAMETERS",
    "ER_CRYPTO_INSUFFICIENT_SECURITY",
    "ER_CRYPTO_KEY_UNAVAILABLE",
    "ER_CRYPTO_KEY_UNUSABLE",
    "ER_CRYPTO_TRUNCATED",
    "ER_DBUS_RELEASE_NAME_REPLY_NON_EXISTENT",
    "ER_DBUS_RELEASE_NAME_REPLY_NOT_OWNER",
    "ER_DBUS_RELEASE_NAME_REPLY_RELEASED",
    "ER_DBUS_REQUEST_NAME_REPLY_ALREADY_OWNER",
    "ER_DBUS_REQUEST_NAME_REPLY_EXISTS",
    "ER_DBUS_REQUEST_NAME_REPLY_IN_QUEUE",
    "ER_DBUS_REQUEST_NAME_REPLY_PRIMARY_OWNER",
    "ER_DBUS_START_REPLY_ALREADY_RUNNING",
    "ER_DEADLOCK",
    "ER_DEAD_THREAD",
    "ER_DIGEST_MISMATCH",
    "ER_DUPLICATE_CERTIFICATE",
    "ER_DUPLICATE_KEY",
    "ER_EMPTY_KEY_BLOB",
    "ER_END_OF_DATA",
    "ER_EOF",
    "ER_EXTERNAL_THREAD",
    "ER_FAIL",
    "ER_FEATURE_NOT_AVAILABLE",
    "ER_INIT_FAILED",
    "ER_INVALID_ADDRESS",
    "ER_INVALID_APPLICATION_STATE",
    "ER_INVALID_CERTIFICATE",
    "ER_INVALID_CERTIFICATE_USAGE",
    "ER_INVALID_CERT_CHAIN",
    "ER_INVALID_CONFIG",
    "ER_INVALID_DATA",
    "ER_INVALID_GUID",
    "ER_INVALID_HTTP_METHOD_USED_FOR_RENDEZVOUS_SERVER_INTERFACE_MESSAGE",
    "ER_INVALID_KEY_ENCODING",
    "ER_INVALID_ON_DEMAND_CONNECTION_MESSAGE_RESPONSE",
    "ER_INVALID_PERSISTENT_CONNECTION_MESSAGE_RESPONSE",
    "ER_INVALID_RENDEZVOUS_SERVER_INTERFACE_MESSAGE",
    "ER_INVALID_SIGNAL_EMISSION_TYPE",
    "ER_INVALID_STREAM",
    "ER_IODISPATCH_STOPPING",
    "ER_KEY_STORE_ALREADY_INITIALIZED",
    "ER_KEY_STORE_ID_NOT_YET_SET",
    "ER_LANGUAGE_NOT_SUPPORTED",
    "ER_MANAGEMENT_ALREADY_STARTED",
    "ER_MANAGEMENT_NOT_STARTED",
    "ER_MANIFEST_NOT_FOUND",
    "ER_MANIFEST_REJECTED",
    "ER_MISSING_DIGEST_IN_CERTIFICATE",
    "ER_NONE",
    "ER_NOT_CONN",
    "ER_NOT_CONNECTED_TO_RENDEZVOUS_SERVER",
    "ER_NOT_IMPLEMENTED",
    "ER_NO_COMMON_TRUST",
    "ER_NO_SUCH_ALARM",
    "ER_NO_SUCH_DEVICE",
    "ER_NO_TRUST_ANCHOR",
    "ER_OK",
    "ER_OPEN_FAILED",
    "ER_OS_ERROR",
    "ER_OUT_OF_MEMORY",
    "ER_P2P",
    "ER_P2P_BUSY",
    "ER_P2P_DISABLED",
    "ER_P2P_FORBIDDEN",
    "ER_P2P_NOT_CONNECTED",
    "ER_P2P_NO_GO",
    "ER_P2P_NO_STA",
    "ER_P2P_TIMEOUT",
    "ER_PACKET_BAD_CRC",
    "ER_PACKET_BAD_FORMAT",
    "ER_PACKET_BAD_PARAMETER",
    "ER_PACKET_BUS_NO_SUCH_CHANNEL",
    "ER_PACKET_CHANNEL_FAIL",
    "ER_PACKET_CONNECT_TIMEOUT",
    "ER_PACKET_TOO_LARGE",
    "ER_PARSE_ERROR",
    "ER_PERMISSION_DENIED",
    "ER_POLICY_NOT_NEWER",
    "ER_PROXIMITY_CONNECTION_ESTABLISH_FAIL",
    "ER_PROXIMITY_NO_PEERS_FOUND",
    "ER_READ_ERROR",
    "ER_RENDEZVOUS_SERVER_DEACTIVATED_USER",
    "ER_RENDEZVOUS_SERVER_ERR401_UNAUTHORIZED_REQUEST",
    "ER_RENDEZVOUS_SERVER_ERR500_INTERNAL_ERROR",
    "ER_RENDEZVOUS_SERVER_ERR503_STATUS_UNAVAILABLE",
    "ER_RENDEZVOUS_SERVER_ROOT_CERTIFICATE_UNINITIALIZED",
    "ER_RENDEZVOUS_SERVER_UNKNOWN_USER",
    "ER_RENDEZVOUS_SERVER_UNRECOVERABLE_ERROR",
    "ER_SLAP_CRC_ERROR",
    "ER_SLAP_ERROR",
    "ER_SLAP_HDR_CHECKSUM_ERROR",
    "ER_SLAP_INVALID_PACKET_LEN",
    "ER_SLAP_INVALID_PACKET_TYPE",
    "ER_SLAP_LEN_MISMATCH",
    "ER_SLAP_OTHER_END_CLOSED",
    "ER_SLAP_PACKET_TYPE_MISMATCH",
    "ER_SOCKET_BIND_ERROR",
    "ER_SOCK_CLOSING",
    "ER_SOCK_OTHER_END_CLOSED",
    "ER_SSL_CONNECT",
    "ER_SSL_ERRORS",
    "ER_SSL_INIT",
    "ER_SSL_VERIFY",
    "ER_STOPPING_THREAD",
    "ER_TCP_MAX_UNTRUSTED",
    "ER_THREADPOOL_EXHAUSTED",
    "ER_THREADPOOL_STOPPING",
    "ER_THREAD_NO_WAIT",
    "ER_THREAD_RUNNING",
    "ER_THREAD_STOPPING",
    "ER_TIMEOUT",
    "ER_TIMER_EXITING",
    "ER_TIMER_FALLBEHIND",
    "ER_TIMER_FULL",
    "ER_TIMER_NOT_ALLOWED",
    "ER_UDP_BACKPRESSURE",
    "ER_UDP_BUSHELLO",
    "ER_UDP_DEMUX_NO_ENDPOINT",
    "ER_UDP_DISCONNECT",
    "ER_UDP_EARLY_EXIT",
    "ER_UDP_ENDPOINT_NOT_STARTED",
    "ER_UDP_ENDPOINT_REMOVED",
    "ER_UDP_ENDPOINT_STALLED",
    "ER_UDP_INVALID",
    "ER_UDP_LOCAL_DISCONNECT",
    "ER_UDP_LOCAL_DISCONNECT_FAIL",
    "ER_UDP_MESSAGE",
    "ER_UDP_MSG_TOO_LONG",
    "ER_UDP_NOT_DISCONNECTED",
    "ER_UDP_NOT_IMPLEMENTED",
    "ER_UDP_NO_LISTENER",
    "ER_UDP_NO_NETWORK",
    "ER_UDP_STOPPING",
    "ER_UDP_UNEXPECTED_FLOW",
    "ER_UDP_UNEXPECTED_LENGTH",
    "ER_UDP_UNSUPPORTED",
    "ER_UNABLE_TO_CONNECT_TO_RENDEZVOUS_SERVER",
    "ER_UNABLE_TO_SEND_MESSAGE_TO_RENDEZVOUS_SERVER",
    "ER_UNKNOWN_CERTIFICATE",
    "ER_UTF_CONVERSION_FAILED",
    "ER_WARNING",
    "ER_WOULDBLOCK",
    "ER_WRITE_ERROR",
    "ER_XML_ACLS_MISSING",
    "ER_XML_ACL_ALL_TYPE_PEER_WITH_OTHERS",
    "ER_XML_ACL_PEERS_MISSING",
    "ER_XML_ACL_PEER_NOT_UNIQUE",
    "ER_XML_ACL_PEER_PUBLIC_KEY_SET",
    "ER_XML_ANNOTATION_NOT_UNIQUE",
    "ER_XML_CONVERTER_ERROR",
    "ER_XML_INTERFACE_MEMBERS_MISSING",
    "ER_XML_INTERFACE_NAME_NOT_UNIQUE",
    "ER_XML_INVALID_ACL_PEER_CHILDREN_COUNT",
    "ER_XML_INVALID_ACL_PEER_PUBLIC_KEY",
    "ER_XML_INVALID_ACL_PEER_TYPE",
    "ER_XML_INVALID_ANNOTATIONS_COUNT",
    "ER_XML_INVALID_ATTRIBUTE_VALUE",
    "ER_XML_INVALID_BASE64",
    "ER_XML_INVALID_ELEMENT_CHILDREN_COUNT",
    "ER_XML_INVALID_ELEMENT_NAME",
    "ER_XML_INVALID_INTERFACE_NAME",
    "ER_XML_INVALID_MANIFEST_VERSION",
    "ER_XML_INVALID_MEMBER_ACTION",
    "ER_XML_INVALID_MEMBER_NAME",
    "ER_XML_INVALID_MEMBER_TYPE",
    "ER_XML_INVALID_OBJECT_PATH",
    "ER_XML_INVALID_OID",
    "ER_XML_INVALID_POLICY_SERIAL_NUMBER",
    "ER_XML_INVALID_POLICY_VERSION",
    "ER_XML_INVALID_RULES_COUNT",
    "ER_XML_INVALID_SECURITY_LEVEL_ANNOTATION_VALUE",
    "ER_XML_MALFORMED",
    "ER_XML_MEMBER_DENY_ACTION_WITH_OTHER",
    "ER_XML_MEMBER_NAME_NOT_UNIQUE",
    "ER_XML_OBJECT_PATH_NOT_UNIQUE",
    "NEED_UPDATE",
    "NOT_CLAIMABLE",
    "PASSWORD_GENERATED_BY_APPLICATION",
    "PASSWORD_GENERATED_BY_SECURITY_MANAGER",
    "QCC_FALSE",
    "QCC_StatusText",
    "QCC_TRUE",
    "QStatus",
    "UNANNOUNCED",
    "_alljoyn_abouticon_handle",
    "_alljoyn_abouticonobj_handle",
    "_alljoyn_abouticonproxy_handle",
    "alljoyn_about_announced_ptr",
    "alljoyn_about_announceflag",
    "alljoyn_aboutdata",
    "alljoyn_aboutdata_create",
    "alljoyn_aboutdata_create_empty",
    "alljoyn_aboutdata_create_full",
    "alljoyn_aboutdata_createfrommsgarg",
    "alljoyn_aboutdata_createfromxml",
    "alljoyn_aboutdata_destroy",
    "alljoyn_aboutdata_getaboutdata",
    "alljoyn_aboutdata_getajsoftwareversion",
    "alljoyn_aboutdata_getannouncedaboutdata",
    "alljoyn_aboutdata_getappid",
    "alljoyn_aboutdata_getappname",
    "alljoyn_aboutdata_getdateofmanufacture",
    "alljoyn_aboutdata_getdefaultlanguage",
    "alljoyn_aboutdata_getdescription",
    "alljoyn_aboutdata_getdeviceid",
    "alljoyn_aboutdata_getdevicename",
    "alljoyn_aboutdata_getfield",
    "alljoyn_aboutdata_getfields",
    "alljoyn_aboutdata_getfieldsignature",
    "alljoyn_aboutdata_gethardwareversion",
    "alljoyn_aboutdata_getmanufacturer",
    "alljoyn_aboutdata_getmodelnumber",
    "alljoyn_aboutdata_getsoftwareversion",
    "alljoyn_aboutdata_getsupportedlanguages",
    "alljoyn_aboutdata_getsupporturl",
    "alljoyn_aboutdata_isfieldannounced",
    "alljoyn_aboutdata_isfieldlocalized",
    "alljoyn_aboutdata_isfieldrequired",
    "alljoyn_aboutdata_isvalid",
    "alljoyn_aboutdata_setappid",
    "alljoyn_aboutdata_setappid_fromstring",
    "alljoyn_aboutdata_setappname",
    "alljoyn_aboutdata_setdateofmanufacture",
    "alljoyn_aboutdata_setdefaultlanguage",
    "alljoyn_aboutdata_setdescription",
    "alljoyn_aboutdata_setdeviceid",
    "alljoyn_aboutdata_setdevicename",
    "alljoyn_aboutdata_setfield",
    "alljoyn_aboutdata_sethardwareversion",
    "alljoyn_aboutdata_setmanufacturer",
    "alljoyn_aboutdata_setmodelnumber",
    "alljoyn_aboutdata_setsoftwareversion",
    "alljoyn_aboutdata_setsupportedlanguage",
    "alljoyn_aboutdata_setsupporturl",
    "alljoyn_aboutdatalistener",
    "alljoyn_aboutdatalistener_callbacks",
    "alljoyn_aboutdatalistener_create",
    "alljoyn_aboutdatalistener_destroy",
    "alljoyn_aboutdatalistener_getaboutdata_ptr",
    "alljoyn_aboutdatalistener_getannouncedaboutdata_ptr",
    "alljoyn_abouticon_clear",
    "alljoyn_abouticon_create",
    "alljoyn_abouticon_destroy",
    "alljoyn_abouticon_getcontent",
    "alljoyn_abouticon_geturl",
    "alljoyn_abouticon_setcontent",
    "alljoyn_abouticon_setcontent_frommsgarg",
    "alljoyn_abouticon_seturl",
    "alljoyn_abouticonobj_create",
    "alljoyn_abouticonobj_destroy",
    "alljoyn_abouticonproxy_create",
    "alljoyn_abouticonproxy_destroy",
    "alljoyn_abouticonproxy_geticon",
    "alljoyn_abouticonproxy_getversion",
    "alljoyn_aboutlistener",
    "alljoyn_aboutlistener_callback",
    "alljoyn_aboutlistener_create",
    "alljoyn_aboutlistener_destroy",
    "alljoyn_aboutobj",
    "alljoyn_aboutobj_announce",
    "alljoyn_aboutobj_announce_using_datalistener",
    "alljoyn_aboutobj_create",
    "alljoyn_aboutobj_destroy",
    "alljoyn_aboutobj_unannounce",
    "alljoyn_aboutobjectdescription",
    "alljoyn_aboutobjectdescription_clear",
    "alljoyn_aboutobjectdescription_create",
    "alljoyn_aboutobjectdescription_create_full",
    "alljoyn_aboutobjectdescription_createfrommsgarg",
    "alljoyn_aboutobjectdescription_destroy",
    "alljoyn_aboutobjectdescription_getinterfacepaths",
    "alljoyn_aboutobjectdescription_getinterfaces",
    "alljoyn_aboutobjectdescription_getmsgarg",
    "alljoyn_aboutobjectdescription_getpaths",
    "alljoyn_aboutobjectdescription_hasinterface",
    "alljoyn_aboutobjectdescription_hasinterfaceatpath",
    "alljoyn_aboutobjectdescription_haspath",
    "alljoyn_aboutproxy",
    "alljoyn_aboutproxy_create",
    "alljoyn_aboutproxy_destroy",
    "alljoyn_aboutproxy_getaboutdata",
    "alljoyn_aboutproxy_getobjectdescription",
    "alljoyn_aboutproxy_getversion",
    "alljoyn_applicationstate",
    "alljoyn_applicationstatelistener",
    "alljoyn_applicationstatelistener_callbacks",
    "alljoyn_applicationstatelistener_create",
    "alljoyn_applicationstatelistener_destroy",
    "alljoyn_applicationstatelistener_state_ptr",
    "alljoyn_authlistener",
    "alljoyn_authlistener_authenticationcomplete_ptr",
    "alljoyn_authlistener_callbacks",
    "alljoyn_authlistener_create",
    "alljoyn_authlistener_destroy",
    "alljoyn_authlistener_requestcredentials_ptr",
    "alljoyn_authlistener_requestcredentialsasync_ptr",
    "alljoyn_authlistener_requestcredentialsresponse",
    "alljoyn_authlistener_securityviolation_ptr",
    "alljoyn_authlistener_setsharedsecret",
    "alljoyn_authlistener_verifycredentials_ptr",
    "alljoyn_authlistener_verifycredentialsasync_ptr",
    "alljoyn_authlistener_verifycredentialsresponse",
    "alljoyn_authlistenerasync_callbacks",
    "alljoyn_authlistenerasync_create",
    "alljoyn_authlistenerasync_destroy",
    "alljoyn_autopinger",
    "alljoyn_autopinger_adddestination",
    "alljoyn_autopinger_addpinggroup",
    "alljoyn_autopinger_create",
    "alljoyn_autopinger_destination_found_ptr",
    "alljoyn_autopinger_destination_lost_ptr",
    "alljoyn_autopinger_destroy",
    "alljoyn_autopinger_pause",
    "alljoyn_autopinger_removedestination",
    "alljoyn_autopinger_removepinggroup",
    "alljoyn_autopinger_resume",
    "alljoyn_autopinger_setpinginterval",
    "alljoyn_busattachment",
    "alljoyn_busattachment_addlogonentry",
    "alljoyn_busattachment_addmatch",
    "alljoyn_busattachment_advertisename",
    "alljoyn_busattachment_bindsessionport",
    "alljoyn_busattachment_canceladvertisename",
    "alljoyn_busattachment_cancelfindadvertisedname",
    "alljoyn_busattachment_cancelfindadvertisednamebytransport",
    "alljoyn_busattachment_cancelwhoimplements_interface",
    "alljoyn_busattachment_cancelwhoimplements_interfaces",
    "alljoyn_busattachment_clearkeys",
    "alljoyn_busattachment_clearkeystore",
    "alljoyn_busattachment_connect",
    "alljoyn_busattachment_create",
    "alljoyn_busattachment_create_concurrency",
    "alljoyn_busattachment_createinterface",
    "alljoyn_busattachment_createinterface_secure",
    "alljoyn_busattachment_createinterfacesfromxml",
    "alljoyn_busattachment_deletedefaultkeystore",
    "alljoyn_busattachment_deleteinterface",
    "alljoyn_busattachment_destroy",
    "alljoyn_busattachment_disconnect",
    "alljoyn_busattachment_enableconcurrentcallbacks",
    "alljoyn_busattachment_enablepeersecurity",
    "alljoyn_busattachment_enablepeersecuritywithpermissionconfigurationlistener",
    "alljoyn_busattachment_findadvertisedname",
    "alljoyn_busattachment_findadvertisednamebytransport",
    "alljoyn_busattachment_getalljoyndebugobj",
    "alljoyn_busattachment_getalljoynproxyobj",
    "alljoyn_busattachment_getconcurrency",
    "alljoyn_busattachment_getconnectspec",
    "alljoyn_busattachment_getdbusproxyobj",
    "alljoyn_busattachment_getglobalguidstring",
    "alljoyn_busattachment_getinterface",
    "alljoyn_busattachment_getinterfaces",
    "alljoyn_busattachment_getkeyexpiration",
    "alljoyn_busattachment_getpeerguid",
    "alljoyn_busattachment_getpermissionconfigurator",
    "alljoyn_busattachment_gettimestamp",
    "alljoyn_busattachment_getuniquename",
    "alljoyn_busattachment_isconnected",
    "alljoyn_busattachment_ispeersecurityenabled",
    "alljoyn_busattachment_isstarted",
    "alljoyn_busattachment_isstopping",
    "alljoyn_busattachment_join",
    "alljoyn_busattachment_joinsession",
    "alljoyn_busattachment_joinsessionasync",
    "alljoyn_busattachment_joinsessioncb_ptr",
    "alljoyn_busattachment_leavesession",
    "alljoyn_busattachment_namehasowner",
    "alljoyn_busattachment_ping",
    "alljoyn_busattachment_registeraboutlistener",
    "alljoyn_busattachment_registerapplicationstatelistener",
    "alljoyn_busattachment_registerbuslistener",
    "alljoyn_busattachment_registerbusobject",
    "alljoyn_busattachment_registerbusobject_secure",
    "alljoyn_busattachment_registerkeystorelistener",
    "alljoyn_busattachment_registersignalhandler",
    "alljoyn_busattachment_registersignalhandlerwithrule",
    "alljoyn_busattachment_releasename",
    "alljoyn_busattachment_reloadkeystore",
    "alljoyn_busattachment_removematch",
    "alljoyn_busattachment_removesessionmember",
    "alljoyn_busattachment_requestname",
    "alljoyn_busattachment_secureconnection",
    "alljoyn_busattachment_secureconnectionasync",
    "alljoyn_busattachment_setdaemondebug",
    "alljoyn_busattachment_setkeyexpiration",
    "alljoyn_busattachment_setlinktimeout",
    "alljoyn_busattachment_setlinktimeoutasync",
    "alljoyn_busattachment_setlinktimeoutcb_ptr",
    "alljoyn_busattachment_setsessionlistener",
    "alljoyn_busattachment_start",
    "alljoyn_busattachment_stop",
    "alljoyn_busattachment_unbindsessionport",
    "alljoyn_busattachment_unregisteraboutlistener",
    "alljoyn_busattachment_unregisterallaboutlisteners",
    "alljoyn_busattachment_unregisterallhandlers",
    "alljoyn_busattachment_unregisterapplicationstatelistener",
    "alljoyn_busattachment_unregisterbuslistener",
    "alljoyn_busattachment_unregisterbusobject",
    "alljoyn_busattachment_unregistersignalhandler",
    "alljoyn_busattachment_unregistersignalhandlerwithrule",
    "alljoyn_busattachment_whoimplements_interface",
    "alljoyn_busattachment_whoimplements_interfaces",
    "alljoyn_buslistener",
    "alljoyn_buslistener_bus_disconnected_ptr",
    "alljoyn_buslistener_bus_prop_changed_ptr",
    "alljoyn_buslistener_bus_stopping_ptr",
    "alljoyn_buslistener_callbacks",
    "alljoyn_buslistener_create",
    "alljoyn_buslistener_destroy",
    "alljoyn_buslistener_found_advertised_name_ptr",
    "alljoyn_buslistener_listener_registered_ptr",
    "alljoyn_buslistener_listener_unregistered_ptr",
    "alljoyn_buslistener_lost_advertised_name_ptr",
    "alljoyn_buslistener_name_owner_changed_ptr",
    "alljoyn_busobject",
    "alljoyn_busobject_addinterface",
    "alljoyn_busobject_addinterface_announced",
    "alljoyn_busobject_addmethodhandler",
    "alljoyn_busobject_addmethodhandlers",
    "alljoyn_busobject_callbacks",
    "alljoyn_busobject_cancelsessionlessmessage",
    "alljoyn_busobject_cancelsessionlessmessage_serial",
    "alljoyn_busobject_create",
    "alljoyn_busobject_destroy",
    "alljoyn_busobject_emitpropertieschanged",
    "alljoyn_busobject_emitpropertychanged",
    "alljoyn_busobject_getannouncedinterfacenames",
    "alljoyn_busobject_getbusattachment",
    "alljoyn_busobject_getname",
    "alljoyn_busobject_getpath",
    "alljoyn_busobject_issecure",
    "alljoyn_busobject_methodentry",
    "alljoyn_busobject_methodreply_args",
    "alljoyn_busobject_methodreply_err",
    "alljoyn_busobject_methodreply_status",
    "alljoyn_busobject_object_registration_ptr",
    "alljoyn_busobject_prop_get_ptr",
    "alljoyn_busobject_prop_set_ptr",
    "alljoyn_busobject_setannounceflag",
    "alljoyn_busobject_signal",
    "alljoyn_certificateid",
    "alljoyn_certificateidarray",
    "alljoyn_claimcapability_masks",
    "alljoyn_claimcapabilityadditionalinfo_masks",
    "alljoyn_credentials",
    "alljoyn_credentials_clear",
    "alljoyn_credentials_create",
    "alljoyn_credentials_destroy",
    "alljoyn_credentials_getcertchain",
    "alljoyn_credentials_getexpiration",
    "alljoyn_credentials_getlogonentry",
    "alljoyn_credentials_getpassword",
    "alljoyn_credentials_getprivateKey",
    "alljoyn_credentials_getusername",
    "alljoyn_credentials_isset",
    "alljoyn_credentials_setcertchain",
    "alljoyn_credentials_setexpiration",
    "alljoyn_credentials_setlogonentry",
    "alljoyn_credentials_setpassword",
    "alljoyn_credentials_setprivatekey",
    "alljoyn_credentials_setusername",
    "alljoyn_getbuildinfo",
    "alljoyn_getnumericversion",
    "alljoyn_getversion",
    "alljoyn_init",
    "alljoyn_interfacedescription",
    "alljoyn_interfacedescription_activate",
    "alljoyn_interfacedescription_addannotation",
    "alljoyn_interfacedescription_addargannotation",
    "alljoyn_interfacedescription_addmember",
    "alljoyn_interfacedescription_addmemberannotation",
    "alljoyn_interfacedescription_addmethod",
    "alljoyn_interfacedescription_addproperty",
    "alljoyn_interfacedescription_addpropertyannotation",
    "alljoyn_interfacedescription_addsignal",
    "alljoyn_interfacedescription_eql",
    "alljoyn_interfacedescription_getannotation",
    "alljoyn_interfacedescription_getannotationatindex",
    "alljoyn_interfacedescription_getannotationscount",
    "alljoyn_interfacedescription_getargdescriptionforlanguage",
    "alljoyn_interfacedescription_getdescriptionforlanguage",
    "alljoyn_interfacedescription_getdescriptionlanguages",
    "alljoyn_interfacedescription_getdescriptionlanguages2",
    "alljoyn_interfacedescription_getdescriptiontranslationcallback",
    "alljoyn_interfacedescription_getmember",
    "alljoyn_interfacedescription_getmemberannotation",
    "alljoyn_interfacedescription_getmemberargannotation",
    "alljoyn_interfacedescription_getmemberdescriptionforlanguage",
    "alljoyn_interfacedescription_getmembers",
    "alljoyn_interfacedescription_getmethod",
    "alljoyn_interfacedescription_getname",
    "alljoyn_interfacedescription_getproperties",
    "alljoyn_interfacedescription_getproperty",
    "alljoyn_interfacedescription_getpropertyannotation",
    "alljoyn_interfacedescription_getpropertydescriptionforlanguage",
    "alljoyn_interfacedescription_getsecuritypolicy",
    "alljoyn_interfacedescription_getsignal",
    "alljoyn_interfacedescription_hasdescription",
    "alljoyn_interfacedescription_hasmember",
    "alljoyn_interfacedescription_hasproperties",
    "alljoyn_interfacedescription_hasproperty",
    "alljoyn_interfacedescription_introspect",
    "alljoyn_interfacedescription_issecure",
    "alljoyn_interfacedescription_member",
    "alljoyn_interfacedescription_member_eql",
    "alljoyn_interfacedescription_member_getannotation",
    "alljoyn_interfacedescription_member_getannotationatindex",
    "alljoyn_interfacedescription_member_getannotationscount",
    "alljoyn_interfacedescription_member_getargannotation",
    "alljoyn_interfacedescription_member_getargannotationatindex",
    "alljoyn_interfacedescription_member_getargannotationscount",
    "alljoyn_interfacedescription_property",
    "alljoyn_interfacedescription_property_eql",
    "alljoyn_interfacedescription_property_getannotation",
    "alljoyn_interfacedescription_property_getannotationatindex",
    "alljoyn_interfacedescription_property_getannotationscount",
    "alljoyn_interfacedescription_securitypolicy",
    "alljoyn_interfacedescription_setargdescription",
    "alljoyn_interfacedescription_setargdescriptionforlanguage",
    "alljoyn_interfacedescription_setdescription",
    "alljoyn_interfacedescription_setdescriptionforlanguage",
    "alljoyn_interfacedescription_setdescriptionlanguage",
    "alljoyn_interfacedescription_setdescriptiontranslationcallback",
    "alljoyn_interfacedescription_setmemberdescription",
    "alljoyn_interfacedescription_setmemberdescriptionforlanguage",
    "alljoyn_interfacedescription_setpropertydescription",
    "alljoyn_interfacedescription_setpropertydescriptionforlanguage",
    "alljoyn_interfacedescription_translation_callback_ptr",
    "alljoyn_keystore",
    "alljoyn_keystorelistener",
    "alljoyn_keystorelistener_acquireexclusivelock_ptr",
    "alljoyn_keystorelistener_callbacks",
    "alljoyn_keystorelistener_create",
    "alljoyn_keystorelistener_destroy",
    "alljoyn_keystorelistener_getkeys",
    "alljoyn_keystorelistener_loadrequest_ptr",
    "alljoyn_keystorelistener_putkeys",
    "alljoyn_keystorelistener_releaseexclusivelock_ptr",
    "alljoyn_keystorelistener_storerequest_ptr",
    "alljoyn_keystorelistener_with_synchronization_callbacks",
    "alljoyn_keystorelistener_with_synchronization_create",
    "alljoyn_manifestarray",
    "alljoyn_message",
    "alljoyn_message_create",
    "alljoyn_message_description",
    "alljoyn_message_destroy",
    "alljoyn_message_eql",
    "alljoyn_message_getarg",
    "alljoyn_message_getargs",
    "alljoyn_message_getauthmechanism",
    "alljoyn_message_getcallserial",
    "alljoyn_message_getcompressiontoken",
    "alljoyn_message_getdestination",
    "alljoyn_message_geterrorname",
    "alljoyn_message_getflags",
    "alljoyn_message_getinterface",
    "alljoyn_message_getmembername",
    "alljoyn_message_getobjectpath",
    "alljoyn_message_getreceiveendpointname",
    "alljoyn_message_getreplyserial",
    "alljoyn_message_getsender",
    "alljoyn_message_getsessionid",
    "alljoyn_message_getsignature",
    "alljoyn_message_gettimestamp",
    "alljoyn_message_gettype",
    "alljoyn_message_isbroadcastsignal",
    "alljoyn_message_isencrypted",
    "alljoyn_message_isexpired",
    "alljoyn_message_isglobalbroadcast",
    "alljoyn_message_issessionless",
    "alljoyn_message_isunreliable",
    "alljoyn_message_parseargs",
    "alljoyn_message_setendianess",
    "alljoyn_message_tostring",
    "alljoyn_messagereceiver_methodhandler_ptr",
    "alljoyn_messagereceiver_replyhandler_ptr",
    "alljoyn_messagereceiver_signalhandler_ptr",
    "alljoyn_messagetype",
    "alljoyn_msgarg",
    "alljoyn_msgarg_array_create",
    "alljoyn_msgarg_array_element",
    "alljoyn_msgarg_array_get",
    "alljoyn_msgarg_array_set",
    "alljoyn_msgarg_array_set_offset",
    "alljoyn_msgarg_array_signature",
    "alljoyn_msgarg_array_tostring",
    "alljoyn_msgarg_clear",
    "alljoyn_msgarg_clone",
    "alljoyn_msgarg_copy",
    "alljoyn_msgarg_create",
    "alljoyn_msgarg_create_and_set",
    "alljoyn_msgarg_destroy",
    "alljoyn_msgarg_equal",
    "alljoyn_msgarg_get",
    "alljoyn_msgarg_get_array_element",
    "alljoyn_msgarg_get_array_elementsignature",
    "alljoyn_msgarg_get_array_numberofelements",
    "alljoyn_msgarg_get_bool",
    "alljoyn_msgarg_get_bool_array",
    "alljoyn_msgarg_get_double",
    "alljoyn_msgarg_get_double_array",
    "alljoyn_msgarg_get_int16",
    "alljoyn_msgarg_get_int16_array",
    "alljoyn_msgarg_get_int32",
    "alljoyn_msgarg_get_int32_array",
    "alljoyn_msgarg_get_int64",
    "alljoyn_msgarg_get_int64_array",
    "alljoyn_msgarg_get_objectpath",
    "alljoyn_msgarg_get_signature",
    "alljoyn_msgarg_get_string",
    "alljoyn_msgarg_get_uint16",
    "alljoyn_msgarg_get_uint16_array",
    "alljoyn_msgarg_get_uint32",
    "alljoyn_msgarg_get_uint32_array",
    "alljoyn_msgarg_get_uint64",
    "alljoyn_msgarg_get_uint64_array",
    "alljoyn_msgarg_get_uint8",
    "alljoyn_msgarg_get_uint8_array",
    "alljoyn_msgarg_get_variant",
    "alljoyn_msgarg_get_variant_array",
    "alljoyn_msgarg_getdictelement",
    "alljoyn_msgarg_getkey",
    "alljoyn_msgarg_getmember",
    "alljoyn_msgarg_getnummembers",
    "alljoyn_msgarg_gettype",
    "alljoyn_msgarg_getvalue",
    "alljoyn_msgarg_hassignature",
    "alljoyn_msgarg_set",
    "alljoyn_msgarg_set_and_stabilize",
    "alljoyn_msgarg_set_bool",
    "alljoyn_msgarg_set_bool_array",
    "alljoyn_msgarg_set_double",
    "alljoyn_msgarg_set_double_array",
    "alljoyn_msgarg_set_int16",
    "alljoyn_msgarg_set_int16_array",
    "alljoyn_msgarg_set_int32",
    "alljoyn_msgarg_set_int32_array",
    "alljoyn_msgarg_set_int64",
    "alljoyn_msgarg_set_int64_array",
    "alljoyn_msgarg_set_objectpath",
    "alljoyn_msgarg_set_objectpath_array",
    "alljoyn_msgarg_set_signature",
    "alljoyn_msgarg_set_signature_array",
    "alljoyn_msgarg_set_string",
    "alljoyn_msgarg_set_string_array",
    "alljoyn_msgarg_set_uint16",
    "alljoyn_msgarg_set_uint16_array",
    "alljoyn_msgarg_set_uint32",
    "alljoyn_msgarg_set_uint32_array",
    "alljoyn_msgarg_set_uint64",
    "alljoyn_msgarg_set_uint64_array",
    "alljoyn_msgarg_set_uint8",
    "alljoyn_msgarg_set_uint8_array",
    "alljoyn_msgarg_setdictentry",
    "alljoyn_msgarg_setstruct",
    "alljoyn_msgarg_signature",
    "alljoyn_msgarg_stabilize",
    "alljoyn_msgarg_tostring",
    "alljoyn_observer",
    "alljoyn_observer_create",
    "alljoyn_observer_destroy",
    "alljoyn_observer_get",
    "alljoyn_observer_getfirst",
    "alljoyn_observer_getnext",
    "alljoyn_observer_object_discovered_ptr",
    "alljoyn_observer_object_lost_ptr",
    "alljoyn_observer_registerlistener",
    "alljoyn_observer_unregisteralllisteners",
    "alljoyn_observer_unregisterlistener",
    "alljoyn_observerlistener",
    "alljoyn_observerlistener_callback",
    "alljoyn_observerlistener_create",
    "alljoyn_observerlistener_destroy",
    "alljoyn_passwordmanager_setcredentials",
    "alljoyn_permissionconfigurationlistener",
    "alljoyn_permissionconfigurationlistener_callbacks",
    "alljoyn_permissionconfigurationlistener_create",
    "alljoyn_permissionconfigurationlistener_destroy",
    "alljoyn_permissionconfigurationlistener_endmanagement_ptr",
    "alljoyn_permissionconfigurationlistener_factoryreset_ptr",
    "alljoyn_permissionconfigurationlistener_policychanged_ptr",
    "alljoyn_permissionconfigurationlistener_startmanagement_ptr",
    "alljoyn_permissionconfigurator",
    "alljoyn_permissionconfigurator_certificatechain_destroy",
    "alljoyn_permissionconfigurator_certificateid_cleanup",
    "alljoyn_permissionconfigurator_certificateidarray_cleanup",
    "alljoyn_permissionconfigurator_claim",
    "alljoyn_permissionconfigurator_endmanagement",
    "alljoyn_permissionconfigurator_getapplicationstate",
    "alljoyn_permissionconfigurator_getclaimcapabilities",
    "alljoyn_permissionconfigurator_getclaimcapabilitiesadditionalinfo",
    "alljoyn_permissionconfigurator_getdefaultclaimcapabilities",
    "alljoyn_permissionconfigurator_getdefaultpolicy",
    "alljoyn_permissionconfigurator_getidentity",
    "alljoyn_permissionconfigurator_getidentitycertificateid",
    "alljoyn_permissionconfigurator_getmanifests",
    "alljoyn_permissionconfigurator_getmanifesttemplate",
    "alljoyn_permissionconfigurator_getmembershipsummaries",
    "alljoyn_permissionconfigurator_getpolicy",
    "alljoyn_permissionconfigurator_getpublickey",
    "alljoyn_permissionconfigurator_installmanifests",
    "alljoyn_permissionconfigurator_installmembership",
    "alljoyn_permissionconfigurator_manifestarray_cleanup",
    "alljoyn_permissionconfigurator_manifesttemplate_destroy",
    "alljoyn_permissionconfigurator_policy_destroy",
    "alljoyn_permissionconfigurator_publickey_destroy",
    "alljoyn_permissionconfigurator_removemembership",
    "alljoyn_permissionconfigurator_reset",
    "alljoyn_permissionconfigurator_resetpolicy",
    "alljoyn_permissionconfigurator_setapplicationstate",
    "alljoyn_permissionconfigurator_setclaimcapabilities",
    "alljoyn_permissionconfigurator_setclaimcapabilitiesadditionalinfo",
    "alljoyn_permissionconfigurator_setmanifesttemplatefromxml",
    "alljoyn_permissionconfigurator_startmanagement",
    "alljoyn_permissionconfigurator_updateidentity",
    "alljoyn_permissionconfigurator_updatepolicy",
    "alljoyn_pinglistener",
    "alljoyn_pinglistener_callback",
    "alljoyn_pinglistener_create",
    "alljoyn_pinglistener_destroy",
    "alljoyn_proxybusobject",
    "alljoyn_proxybusobject_addchild",
    "alljoyn_proxybusobject_addinterface",
    "alljoyn_proxybusobject_addinterface_by_name",
    "alljoyn_proxybusobject_copy",
    "alljoyn_proxybusobject_create",
    "alljoyn_proxybusobject_create_secure",
    "alljoyn_proxybusobject_destroy",
    "alljoyn_proxybusobject_enablepropertycaching",
    "alljoyn_proxybusobject_getallproperties",
    "alljoyn_proxybusobject_getallpropertiesasync",
    "alljoyn_proxybusobject_getchild",
    "alljoyn_proxybusobject_getchildren",
    "alljoyn_proxybusobject_getinterface",
    "alljoyn_proxybusobject_getinterfaces",
    "alljoyn_proxybusobject_getpath",
    "alljoyn_proxybusobject_getproperty",
    "alljoyn_proxybusobject_getpropertyasync",
    "alljoyn_proxybusobject_getservicename",
    "alljoyn_proxybusobject_getsessionid",
    "alljoyn_proxybusobject_getuniquename",
    "alljoyn_proxybusobject_implementsinterface",
    "alljoyn_proxybusobject_introspectremoteobject",
    "alljoyn_proxybusobject_introspectremoteobjectasync",
    "alljoyn_proxybusobject_issecure",
    "alljoyn_proxybusobject_isvalid",
    "alljoyn_proxybusobject_listener_getallpropertiescb_ptr",
    "alljoyn_proxybusobject_listener_getpropertycb_ptr",
    "alljoyn_proxybusobject_listener_introspectcb_ptr",
    "alljoyn_proxybusobject_listener_propertieschanged_ptr",
    "alljoyn_proxybusobject_listener_setpropertycb_ptr",
    "alljoyn_proxybusobject_methodcall",
    "alljoyn_proxybusobject_methodcall_member",
    "alljoyn_proxybusobject_methodcall_member_noreply",
    "alljoyn_proxybusobject_methodcall_noreply",
    "alljoyn_proxybusobject_methodcallasync",
    "alljoyn_proxybusobject_methodcallasync_member",
    "alljoyn_proxybusobject_parsexml",
    "alljoyn_proxybusobject_ref",
    "alljoyn_proxybusobject_ref_create",
    "alljoyn_proxybusobject_ref_decref",
    "alljoyn_proxybusobject_ref_get",
    "alljoyn_proxybusobject_ref_incref",
    "alljoyn_proxybusobject_registerpropertieschangedlistener",
    "alljoyn_proxybusobject_removechild",
    "alljoyn_proxybusobject_secureconnection",
    "alljoyn_proxybusobject_secureconnectionasync",
    "alljoyn_proxybusobject_setproperty",
    "alljoyn_proxybusobject_setpropertyasync",
    "alljoyn_proxybusobject_unregisterpropertieschangedlistener",
    "alljoyn_routerinit",
    "alljoyn_routerinitwithconfig",
    "alljoyn_routershutdown",
    "alljoyn_securityapplicationproxy",
    "alljoyn_securityapplicationproxy_claim",
    "alljoyn_securityapplicationproxy_computemanifestdigest",
    "alljoyn_securityapplicationproxy_create",
    "alljoyn_securityapplicationproxy_destroy",
    "alljoyn_securityapplicationproxy_digest_destroy",
    "alljoyn_securityapplicationproxy_eccpublickey_destroy",
    "alljoyn_securityapplicationproxy_endmanagement",
    "alljoyn_securityapplicationproxy_getapplicationstate",
    "alljoyn_securityapplicationproxy_getclaimcapabilities",
    "alljoyn_securityapplicationproxy_getclaimcapabilitiesadditionalinfo",
    "alljoyn_securityapplicationproxy_getdefaultpolicy",
    "alljoyn_securityapplicationproxy_geteccpublickey",
    "alljoyn_securityapplicationproxy_getmanifesttemplate",
    "alljoyn_securityapplicationproxy_getpermissionmanagementsessionport",
    "alljoyn_securityapplicationproxy_getpolicy",
    "alljoyn_securityapplicationproxy_installmembership",
    "alljoyn_securityapplicationproxy_manifest_destroy",
    "alljoyn_securityapplicationproxy_manifesttemplate_destroy",
    "alljoyn_securityapplicationproxy_policy_destroy",
    "alljoyn_securityapplicationproxy_reset",
    "alljoyn_securityapplicationproxy_resetpolicy",
    "alljoyn_securityapplicationproxy_setmanifestsignature",
    "alljoyn_securityapplicationproxy_signmanifest",
    "alljoyn_securityapplicationproxy_startmanagement",
    "alljoyn_securityapplicationproxy_updateidentity",
    "alljoyn_securityapplicationproxy_updatepolicy",
    "alljoyn_sessionlistener",
    "alljoyn_sessionlistener_callbacks",
    "alljoyn_sessionlistener_create",
    "alljoyn_sessionlistener_destroy",
    "alljoyn_sessionlistener_sessionlost_ptr",
    "alljoyn_sessionlistener_sessionmemberadded_ptr",
    "alljoyn_sessionlistener_sessionmemberremoved_ptr",
    "alljoyn_sessionlostreason",
    "alljoyn_sessionopts",
    "alljoyn_sessionopts_cmp",
    "alljoyn_sessionopts_create",
    "alljoyn_sessionopts_destroy",
    "alljoyn_sessionopts_get_multipoint",
    "alljoyn_sessionopts_get_proximity",
    "alljoyn_sessionopts_get_traffic",
    "alljoyn_sessionopts_get_transports",
    "alljoyn_sessionopts_iscompatible",
    "alljoyn_sessionopts_set_multipoint",
    "alljoyn_sessionopts_set_proximity",
    "alljoyn_sessionopts_set_traffic",
    "alljoyn_sessionopts_set_transports",
    "alljoyn_sessionportlistener",
    "alljoyn_sessionportlistener_acceptsessionjoiner_ptr",
    "alljoyn_sessionportlistener_callbacks",
    "alljoyn_sessionportlistener_create",
    "alljoyn_sessionportlistener_destroy",
    "alljoyn_sessionportlistener_sessionjoined_ptr",
    "alljoyn_shutdown",
    "alljoyn_typeid",
    "alljoyn_unity_deferred_callbacks_process",
    "alljoyn_unity_set_deferred_callback_mainthread_only",
]
_arch_optional = [
]
