#include <libloaderapi.h>
#include <stdio.h>
/* 
https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya
HMODULE LoadLibraryA(
  [in] LPCSTR lpLibFileName
);
Takes path to dll and returns a handle or NULL. Handle is the address of the loaded library in memory.

https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress
FARPROC GetProcAddress(
  [in] HMODULE hModule,
  [in] LPCSTR  lpProcName
);
Takes handle to dll and name of function, returns pointer to that function or NULL. FARPROC is a generic function pointer.
*/

typedef void* (*CreateFunc)(const void*);

void* myfactory(const char* libname, const char* ctorarg) {
  HMODULE libHandle = LoadLibraryA(libname);
  if (!libHandle) {
    printf("Failed to load library %s\n", libname);
    return NULL;
  }

  FARPROC createLoc = GetProcAddress(libHandle, "create");
  if (!createLoc) {
    printf("Failed to find create function in library %s\n", libname);
    FreeLibrary(libHandle);
    return NULL;
  }

  CreateFunc create = (CreateFunc)createLoc;
  return create((const void*)ctorarg);
}