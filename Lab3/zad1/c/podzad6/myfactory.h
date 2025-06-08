#pragma once

#include <libloaderapi.h>

typedef void (*ConstructFunc)(void*, const char*);
typedef size_t (*FuncSize)(void);

int myfactory(const char*, size_t*, ConstructFunc*);