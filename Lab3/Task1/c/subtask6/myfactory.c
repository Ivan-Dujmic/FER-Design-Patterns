#include <libloaderapi.h>
#include <stdio.h>

typedef void (*ConstructFunc)(void*, const char*);
typedef size_t (*FuncSize)(void);

int myfactory(const char* libname, size_t* size, ConstructFunc* construct) {
  HMODULE libHandle = LoadLibraryA(libname);
  if (!libHandle) {
    printf("Failed to load library %s\n", libname);
    return -1;
  }

  FuncSize sizeFunc = (FuncSize)GetProcAddress(libHandle, "sizeof_object");
  ConstructFunc constructFunc = (ConstructFunc)GetProcAddress(libHandle, "construct");

  if (!sizeFunc || !constructFunc) {
    printf("Failed to find required functions in %s\n", libname);
    FreeLibrary(libHandle);
    return -1;
  }

  *size = sizeFunc();
  *construct = constructFunc;

  return 0;
}