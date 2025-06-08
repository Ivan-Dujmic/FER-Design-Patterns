	.file	"main.cpp"
	.intel_syntax noprefix
	.text
	.section	.text$_ZN9CoolClass3setEi,"x"
	.linkonce discard
	.align 2
	.globl	_ZN9CoolClass3setEi
	.def	_ZN9CoolClass3setEi;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZN9CoolClass3setEi
_ZN9CoolClass3setEi:
.LFB0:
	push	rbp
	.seh_pushreg	rbp
	mov	rbp, rsp
	.seh_setframe	rbp, 0
	.seh_endprologue
	mov	QWORD PTR 16[rbp], rcx
	mov	DWORD PTR 24[rbp], edx
	mov	rax, QWORD PTR 16[rbp]
	mov	edx, DWORD PTR 24[rbp]
	mov	DWORD PTR 8[rax], edx
	nop
	pop	rbp
	ret
	.seh_endproc
	.section	.text$_ZN9CoolClass3getEv,"x"
	.linkonce discard
	.align 2
	.globl	_ZN9CoolClass3getEv
	.def	_ZN9CoolClass3getEv;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZN9CoolClass3getEv
_ZN9CoolClass3getEv:
.LFB1:
	push	rbp
	.seh_pushreg	rbp
	mov	rbp, rsp
	.seh_setframe	rbp, 0
	.seh_endprologue
	mov	QWORD PTR 16[rbp], rcx
	mov	rax, QWORD PTR 16[rbp]
	mov	eax, DWORD PTR 8[rax]
	pop	rbp
	ret
	.seh_endproc
	.section	.text$_ZN13PlainOldClass3setEi,"x"
	.linkonce discard
	.align 2
	.globl	_ZN13PlainOldClass3setEi
	.def	_ZN13PlainOldClass3setEi;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZN13PlainOldClass3setEi
_ZN13PlainOldClass3setEi:
.LFB2:
	push	rbp
	.seh_pushreg	rbp
	mov	rbp, rsp
	.seh_setframe	rbp, 0
	.seh_endprologue
	mov	QWORD PTR 16[rbp], rcx
	mov	DWORD PTR 24[rbp], edx
	mov	rax, QWORD PTR 16[rbp]
	mov	edx, DWORD PTR 24[rbp]
	mov	DWORD PTR [rax], edx
	nop
	pop	rbp
	ret
	.seh_endproc
	.section	.text$_ZN4BaseC2Ev,"x"
	.linkonce discard
	.align 2
	.globl	_ZN4BaseC2Ev
	.def	_ZN4BaseC2Ev;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZN4BaseC2Ev
_ZN4BaseC2Ev:
.LFB7:
	push	rbp
	.seh_pushreg	rbp
	mov	rbp, rsp
	.seh_setframe	rbp, 0
	.seh_endprologue
	mov	QWORD PTR 16[rbp], rcx
	lea	rdx, _ZTV4Base[rip+16]
	mov	rax, QWORD PTR 16[rbp]
	mov	QWORD PTR [rax], rdx
	nop
	pop	rbp
	ret
	.seh_endproc
	.section	.text$_ZN9CoolClassC1Ev,"x"
	.linkonce discard
	.align 2
	.globl	_ZN9CoolClassC1Ev
	.def	_ZN9CoolClassC1Ev;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZN9CoolClassC1Ev
_ZN9CoolClassC1Ev:
.LFB10:
	push	rbp
	.seh_pushreg	rbp
	mov	rbp, rsp
	.seh_setframe	rbp, 0
	sub	rsp, 32
	.seh_stackalloc	32
	.seh_endprologue
	mov	QWORD PTR 16[rbp], rcx
	mov	rax, QWORD PTR 16[rbp]
	mov	rcx, rax
	call	_ZN4BaseC2Ev
	lea	rdx, _ZTV9CoolClass[rip+16]
	mov	rax, QWORD PTR 16[rbp]
	mov	QWORD PTR [rax], rdx
	nop
	add	rsp, 32
	pop	rbp
	ret
	.seh_endproc
	.text
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
.LFB4:
	push	rbp
	.seh_pushreg	rbp
	push	rbx
	.seh_pushreg	rbx
	sub	rsp, 56
	.seh_stackalloc	56
	lea	rbp, 48[rsp]
	.seh_setframe	rbp, 48
	.seh_endprologue
	call	__main
	mov	ecx, 16
	call	_Znwy
	mov	rbx, rax
	mov	rcx, rbx
	call	_ZN9CoolClassC1Ev
	mov	QWORD PTR -8[rbp], rbx
	lea	rax, -12[rbp]
	mov	edx, 42
	mov	rcx, rax
	call	_ZN13PlainOldClass3setEi
	mov	rax, QWORD PTR -8[rbp]
	mov	rax, QWORD PTR [rax]
	mov	r8, QWORD PTR [rax]
	mov	rax, QWORD PTR -8[rbp]
	mov	edx, 42
	mov	rcx, rax
	call	r8
	mov	eax, 0
	add	rsp, 56
	pop	rbx
	pop	rbp
	ret
	.seh_endproc
	.globl	_ZTV9CoolClass
	.section	.rdata$_ZTV9CoolClass,"dr"
	.linkonce same_size
	.align 8
_ZTV9CoolClass:
	.quad	0
	.quad	_ZTI9CoolClass
	.quad	_ZN9CoolClass3setEi
	.quad	_ZN9CoolClass3getEv
	.globl	_ZTV4Base
	.section	.rdata$_ZTV4Base,"dr"
	.linkonce same_size
	.align 8
_ZTV4Base:
	.quad	0
	.quad	_ZTI4Base
	.quad	__cxa_pure_virtual
	.quad	__cxa_pure_virtual
	.globl	_ZTI9CoolClass
	.section	.rdata$_ZTI9CoolClass,"dr"
	.linkonce same_size
	.align 8
_ZTI9CoolClass:
	.quad	_ZTVN10__cxxabiv120__si_class_type_infoE+16
	.quad	_ZTS9CoolClass
	.quad	_ZTI4Base
	.globl	_ZTS9CoolClass
	.section	.rdata$_ZTS9CoolClass,"dr"
	.linkonce same_size
	.align 8
_ZTS9CoolClass:
	.ascii "9CoolClass\0"
	.globl	_ZTI4Base
	.section	.rdata$_ZTI4Base,"dr"
	.linkonce same_size
	.align 8
_ZTI4Base:
	.quad	_ZTVN10__cxxabiv117__class_type_infoE+16
	.quad	_ZTS4Base
	.globl	_ZTS4Base
	.section	.rdata$_ZTS4Base,"dr"
	.linkonce same_size
_ZTS4Base:
	.ascii "4Base\0"
	.weak	__cxa_pure_virtual
	.def	__main;	.scl	2;	.type	32;	.endef
	.ident	"GCC: (Rev2, Built by MSYS2 project) 14.2.0"
	.def	_Znwy;	.scl	2;	.type	32;	.endef
	.def	__cxa_pure_virtual;	.scl	2;	.type	32;	.endef
