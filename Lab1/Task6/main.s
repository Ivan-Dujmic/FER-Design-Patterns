	.file	"main.cpp"
	.intel_syntax noprefix
	.text
	.section	.text$_ZN4BaseC2Ev,"x"
	.linkonce discard
	.align 2
	.globl	_ZN4BaseC2Ev
	.def	_ZN4BaseC2Ev;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZN4BaseC2Ev
_ZN4BaseC2Ev:
.LFB23:
	push	rbp
	.seh_pushreg	rbp
	mov	rbp, rsp
	.seh_setframe	rbp, 0
	sub	rsp, 32
	.seh_stackalloc	32
	.seh_endprologue
	mov	QWORD PTR 16[rbp], rcx
	lea	rdx, _ZTV4Base[rip+16]
	mov	rax, QWORD PTR 16[rbp]
	mov	QWORD PTR [rax], rdx
	mov	rax, QWORD PTR 16[rbp]
	mov	rcx, rax
	call	_ZN4Base6metodaEv
	nop
	add	rsp, 32
	pop	rbp
	ret
	.seh_endproc
	.section .rdata,"dr"
.LC0:
	.ascii "ja sam bazna implementacija!\12\0"
	.section	.text$_ZN4Base15virtualnaMetodaEv,"x"
	.linkonce discard
	.align 2
	.globl	_ZN4Base15virtualnaMetodaEv
	.def	_ZN4Base15virtualnaMetodaEv;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZN4Base15virtualnaMetodaEv
_ZN4Base15virtualnaMetodaEv:
.LFB25:
	push	rbp
	.seh_pushreg	rbp
	mov	rbp, rsp
	.seh_setframe	rbp, 0
	sub	rsp, 32
	.seh_stackalloc	32
	.seh_endprologue
	mov	QWORD PTR 16[rbp], rcx
	lea	rax, .LC0[rip]
	mov	rcx, rax
	call	__mingw_printf
	nop
	add	rsp, 32
	pop	rbp
	ret
	.seh_endproc
	.section .rdata,"dr"
.LC1:
	.ascii "Metoda kaze: \0"
	.section	.text$_ZN4Base6metodaEv,"x"
	.linkonce discard
	.align 2
	.globl	_ZN4Base6metodaEv
	.def	_ZN4Base6metodaEv;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZN4Base6metodaEv
_ZN4Base6metodaEv:
.LFB26:
	push	rbp
	.seh_pushreg	rbp
	mov	rbp, rsp
	.seh_setframe	rbp, 0
	sub	rsp, 32
	.seh_stackalloc	32
	.seh_endprologue
	mov	QWORD PTR 16[rbp], rcx
	lea	rax, .LC1[rip]
	mov	rcx, rax
	call	__mingw_printf
	mov	rax, QWORD PTR 16[rbp]
	mov	rax, QWORD PTR [rax]
	mov	rdx, QWORD PTR [rax]
	mov	rax, QWORD PTR 16[rbp]
	mov	rcx, rax
	call	rdx
	nop
	add	rsp, 32
	pop	rbp
	ret
	.seh_endproc
	.section	.text$_ZN7DerivedC1Ev,"x"
	.linkonce discard
	.align 2
	.globl	_ZN7DerivedC1Ev
	.def	_ZN7DerivedC1Ev;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZN7DerivedC1Ev
_ZN7DerivedC1Ev:
.LFB29:
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
	lea	rdx, _ZTV7Derived[rip+16]
	mov	rax, QWORD PTR 16[rbp]
	mov	QWORD PTR [rax], rdx
	mov	rax, QWORD PTR 16[rbp]
	mov	rcx, rax
	call	_ZN4Base6metodaEv
	nop
	add	rsp, 32
	pop	rbp
	ret
	.seh_endproc
	.section .rdata,"dr"
	.align 8
.LC2:
	.ascii "ja sam izvedena implementacija!\12\0"
	.section	.text$_ZN7Derived15virtualnaMetodaEv,"x"
	.linkonce discard
	.align 2
	.globl	_ZN7Derived15virtualnaMetodaEv
	.def	_ZN7Derived15virtualnaMetodaEv;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZN7Derived15virtualnaMetodaEv
_ZN7Derived15virtualnaMetodaEv:
.LFB30:
	push	rbp
	.seh_pushreg	rbp
	mov	rbp, rsp
	.seh_setframe	rbp, 0
	sub	rsp, 32
	.seh_stackalloc	32
	.seh_endprologue
	mov	QWORD PTR 16[rbp], rcx
	lea	rax, .LC2[rip]
	mov	rcx, rax
	call	__mingw_printf
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
.LFB31:
	push	rbp
	.seh_pushreg	rbp
	push	rdi
	.seh_pushreg	rdi
	push	rsi
	.seh_pushreg	rsi
	push	rbx
	.seh_pushreg	rbx
	sub	rsp, 56
	.seh_stackalloc	56
	lea	rbp, 48[rsp]
	.seh_setframe	rbp, 48
	.seh_endprologue
	call	__main
	mov	ecx, 8
.LEHB0:
	call	_Znwy
.LEHE0:
	mov	rbx, rax
	mov	edi, 1
	mov	rcx, rbx
.LEHB1:
	call	_ZN7DerivedC1Ev
.LEHE1:
	mov	QWORD PTR -8[rbp], rbx
	mov	rax, QWORD PTR -8[rbp]
	mov	rcx, rax
.LEHB2:
	call	_ZN4Base6metodaEv
	mov	eax, 0
	jmp	.L11
.L10:
	mov	rsi, rax
	test	dil, dil
	je	.L9
	mov	edx, 8
	mov	rcx, rbx
	call	_ZdlPvy
.L9:
	mov	rax, rsi
	mov	rcx, rax
	call	_Unwind_Resume
.LEHE2:
.L11:
	add	rsp, 56
	pop	rbx
	pop	rsi
	pop	rdi
	pop	rbp
	ret
	.seh_handler	__gxx_personality_seh0, @unwind, @except
	.seh_handlerdata
.LLSDA31:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE31-.LLSDACSB31
.LLSDACSB31:
	.uleb128 .LEHB0-.LFB31
	.uleb128 .LEHE0-.LEHB0
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB1-.LFB31
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L10-.LFB31
	.uleb128 0
	.uleb128 .LEHB2-.LFB31
	.uleb128 .LEHE2-.LEHB2
	.uleb128 0
	.uleb128 0
.LLSDACSE31:
	.text
	.seh_endproc
	.globl	_ZTV7Derived
	.section	.rdata$_ZTV7Derived,"dr"
	.linkonce same_size
	.align 8
_ZTV7Derived:
	.quad	0
	.quad	_ZTI7Derived
	.quad	_ZN7Derived15virtualnaMetodaEv
	.globl	_ZTV4Base
	.section	.rdata$_ZTV4Base,"dr"
	.linkonce same_size
	.align 8
_ZTV4Base:
	.quad	0
	.quad	_ZTI4Base
	.quad	_ZN4Base15virtualnaMetodaEv
	.globl	_ZTI7Derived
	.section	.rdata$_ZTI7Derived,"dr"
	.linkonce same_size
	.align 8
_ZTI7Derived:
	.quad	_ZTVN10__cxxabiv120__si_class_type_infoE+16
	.quad	_ZTS7Derived
	.quad	_ZTI4Base
	.globl	_ZTS7Derived
	.section	.rdata$_ZTS7Derived,"dr"
	.linkonce same_size
	.align 8
_ZTS7Derived:
	.ascii "7Derived\0"
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
	.def	__gxx_personality_seh0;	.scl	2;	.type	32;	.endef
	.def	__main;	.scl	2;	.type	32;	.endef
	.ident	"GCC: (Rev2, Built by MSYS2 project) 14.2.0"
	.def	_Znwy;	.scl	2;	.type	32;	.endef
	.def	_ZdlPvy;	.scl	2;	.type	32;	.endef
	.def	_Unwind_Resume;	.scl	2;	.type	32;	.endef
