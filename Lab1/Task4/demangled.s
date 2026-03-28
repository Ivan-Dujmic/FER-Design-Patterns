; https://demangler.com/
; CTRL+F ZAD# za pronalazak dijela koda vezanog za zadatak #

.file	"main.cpp"
	.intel_syntax noprefix
	.text
	.section	.text$CoolClass::set(int),"x"
	.linkonce discard
	.align 2
	.globl	CoolClass::set(int)
	.def	CoolClass::set(int);	.scl	2;	.type	32;	.endef
	.seh_proc	CoolClass::set(int)
CoolClass::set(int):
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
	.section	.text$CoolClass::get(),"x"
	.linkonce discard
	.align 2
	.globl	CoolClass::get()
	.def	CoolClass::get();	.scl	2;	.type	32;	.endef
	.seh_proc	CoolClass::get()
CoolClass::get():
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
	.section	.text$PlainOldClass::set(int),"x"
	.linkonce discard
	.align 2
	.globl	PlainOldClass::set(int)
	.def	PlainOldClass::set(int);	.scl	2;	.type	32;	.endef
	.seh_proc	PlainOldClass::set(int)
PlainOldClass::set(int):
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
	.section	.text$Base::Base(),"x"
	.linkonce discard
	.align 2
	.globl	Base::Base()
	.def	Base::Base();	.scl	2;	.type	32;	.endef
	.seh_proc	Base::Base()
Base::Base():
.LFB7:
	push	rbp
	.seh_pushreg	rbp
	mov	rbp, rsp
	.seh_setframe	rbp, 0
	.seh_endprologue
	mov	QWORD PTR 16[rbp], rcx
	lea	rdx, vtable for Base[rip 16]
	mov	rax, QWORD PTR 16[rbp]
	mov	QWORD PTR [rax], rdx
	nop
	pop	rbp
	ret
	.seh_endproc
	.section	.text$CoolClass::CoolClass(),"x"
	.linkonce discard
	.align 2
	.globl	CoolClass::CoolClass()
	.def	CoolClass::CoolClass();	.scl	2;	.type	32;	.endef
	.seh_proc	CoolClass::CoolClass()
CoolClass::CoolClass():
.LFB10:
	push	rbp
	.seh_pushreg	rbp
	mov	rbp, rsp
	.seh_setframe	rbp, 0
	sub	rsp, 32
	.seh_stackalloc	32
	.seh_endprologue
    ; ZAD6 START
    ; postavljanje pokazivača na vtable u konstruktoru
	mov	QWORD PTR 16[rbp], rcx
	mov	rax, QWORD PTR 16[rbp]
	mov	rcx, rax
	call	Base::Base()
	lea	rdx, vtable for CoolClass[rip 16]
	mov	rax, QWORD PTR 16[rbp]
	mov	QWORD PTR [rax], rdx
    ; ZAD6 END
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
    ; ZAD1 ZAD2 ZAD3 ZAD4 START
	mov	ecx, 16 ; u registar ecx stavljamo 16 što je veličina u bajtovima koju ćemo tražiti u pozivu new za CoolClass objekt
	call	operator new(unsigned long long)    ; alokacija memorije za CoolClass
	mov	rbx, rax    ; rezultat operacije new (adresa alokacije) sprema se u rbx (iz rax)
	mov	rcx, rbx    ; taj pokazivač također sada stavljamo u rcx
	call	CoolClass::CoolClass()  ; poziv konstruktora
	mov	QWORD PTR -8[rbp], rbx  ; pamćenje pokazivača na novonastali objekt
    ; CoolClass završen, nastavlja se s PlainOldClass
    ; ZAD5 START
	lea	rax, -12[rbp]   ; dobivanje adrese na stogu za PlainOldclass objekt
    ; ZAD1 ZAD2 ZAD3 ZAD4 END
	mov	edx, 42 ; pripremamo argument (42) u edx
	mov	rcx, rax    ; pripremamo adresu (koja je u rax) kao argument (this) tako da ju stavljamo u rcx
	call	PlainOldClass::set(int) ; poziv metode set
    ; PlainOldClass završen, nastavlja se s CoolClass
	mov	rax, QWORD PTR -8[rbp]  ; učitavanje pokazivača na CoolClass
	mov	rax, QWORD PTR [rax]    ; učitavanje prvog člana tog objekta (vtable)
	mov	r8, QWORD PTR [rax]     ; učitavanje adrese funkcije set()
	mov	rax, QWORD PTR -8[rbp]  ; ponovno učitavanje pokazivača na CoolClass
	mov	edx, 42     ; postavljanje argumenta
	mov	rcx, rax    ; this argument
	call	r8      ; poziv funkcije set()
    ; ZAD5 END
	mov	eax, 0
	add	rsp, 56
	pop	rbx
	pop	rbp
	ret
	.seh_endproc
    ; ZAD6 START
    ; definicija vtablea
	.globl	vtable for CoolClass
	.section	.rdata$vtable for CoolClass,"dr"
	.linkonce same_size
	.align 8
vtable for CoolClass:
	.quad	0
	.quad	typeinfo for CoolClass  ; pokazivač na RTTI
	.quad	CoolClass::set(int)
	.quad	CoolClass::get()
    ; ZAD6 END
	.globl	vtable for Base
	.section	.rdata$vtable for Base,"dr"
	.linkonce same_size
	.align 8
vtable for Base:
	.quad	0
	.quad	typeinfo for Base
	.quad	__cxa_pure_virtual
	.quad	__cxa_pure_virtual
	.globl	typeinfo for CoolClass
	.section	.rdata$typeinfo for CoolClass,"dr"
	.linkonce same_size
	.align 8
typeinfo for CoolClass:
	.quad	vtable for __cxxabiv1::__si_class_type_info 16
	.quad	typeinfo name for CoolClass
	.quad	typeinfo for Base
	.globl	typeinfo name for CoolClass
	.section	.rdata$typeinfo name for CoolClass,"dr"
	.linkonce same_size
	.align 8
typeinfo name for CoolClass:
	.ascii "9CoolClass\0"
	.globl	typeinfo for Base
	.section	.rdata$typeinfo for Base,"dr"
	.linkonce same_size
	.align 8
typeinfo for Base:
	.quad	vtable for __cxxabiv1::__class_type_info 16
	.quad	typeinfo name for Base
	.globl	typeinfo name for Base
	.section	.rdata$typeinfo name for Base,"dr"
	.linkonce same_size
typeinfo name for Base:
	.ascii "4Base\0"
	.weak	__cxa_pure_virtual
	.def	__main;	.scl	2;	.type	32;	.endef
	.ident	"GCC: (Rev2, Built by MSYS2 project) 14.2.0"
	.def	operator new(unsigned long long);	.scl	2;	.type	32;	.endef
	.def	__cxa_pure_virtual;	.scl	2;	.type	32;	.endef