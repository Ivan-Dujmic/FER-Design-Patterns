#pragma once

#ifdef __cplusplus
extern "C" {
#endif

#include <libloaderapi.h>

typedef void (*ConstructFunc)(void*, const char*);
typedef size_t (*FuncSize)(void);

int myfactory(const char*, size_t*, ConstructFunc*);

#ifdef __cplusplus
}
#endif