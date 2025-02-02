from ctypes import c_void_p, c_wchar, cast, sizeof, wstring_at

from Windows.Win32.Foundation import PWSTR
from Windows.Win32.System.Environment import (FreeEnvironmentStringsW,
                                              GetEnvironmentStringsW)


# Unsafe case for c_wchar_p to python str auto-conversion.
# GetEnvironmentStringsW() returns NUL terminated list of NUL terminated string.
# name1=value1\0name2=value2\0\0
# Return value should be freed by FreeEnvironmentStringsW().
def GetEnvironmentStrings():
    ptr: PWSTR = GetEnvironmentStringsW()
    ptr_as_int: int = cast(ptr, c_void_p).value
    while (s := wstring_at(ptr_as_int)) != "":
        yield s.split("=", maxsplit=1)
        ptr_as_int += (len(s) + 1) * sizeof(c_wchar)
    FreeEnvironmentStringsW(ptr)

for name, value in GetEnvironmentStrings():
    print(f"{name} = {value}")
