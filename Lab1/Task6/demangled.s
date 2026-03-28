; https://demangler.com/
; CTRL+F KORAK#:

.file	"main.cpp"
	.intel_syntax noprefix
	.text
	.section	.text$Base::Base(),"x"
	.linkonce discard
	.align 2
	.globl	Base::Base()
	.def	Base::Base();	.scl	2;	.type	32;	.endef
	.seh_proc	Base::Base()
Base::Base():
.LFB23:
	push	rbp
	.seh_pushreg	rbp
	mov	rbp, rsp
	.seh_setframe	rbp, 0
	sub	rsp, 32
	.seh_stackalloc	32
	.seh_endprologue
	mov	QWORD PTR 16[rbp], rcx
	lea	rdx, vtable for Base[rip 16]	; KORAK3: adresa vtablea za Base se učitava u rdc
	mov	rax, QWORD PTR 16[rbp]	
	mov	QWORD PTR [rax], rdx	; KORAK3: te se ta adresa postavlja na adresu u rax (a to je početak objekta)
	mov	rax, QWORD PTR 16[rbp]
	mov	rcx, rax
	call	Base::metoda()	; KORAK4: poziva se Base::metoda()
	nop
	add	rsp, 32
	pop	rbp
	ret
	.seh_endproc
	.section .rdata,"dr"
.LC0:
	.ascii "ja sam bazna implementacija!\12\0"	; KORAK6: zapis stringa za baznu implementaciju
	.section	.text$Base::virtualnaMetoda(),"x"
	.linkonce discard
	.align 2
	.globl	Base::virtualnaMetoda()
	.def	Base::virtualnaMetoda();	.scl	2;	.type	32;	.endef
	.seh_proc	Base::virtualnaMetoda()
Base::virtualnaMetoda():
.LFB25:
	push	rbp
	.seh_pushreg	rbp
	mov	rbp, rsp
	.seh_setframe	rbp, 0
	sub	rsp, 32
	.seh_stackalloc	32
	.seh_endprologue
	mov	QWORD PTR 16[rbp], rcx
	lea	rax, .LC0[rip]	; KORAK6: učitavamo adresu stringa
	mov	rcx, rax	; KORAK6: postavljanje argumenta
	call	__mingw_printf	; poziv printf()
	nop
	add	rsp, 32
	pop	rbp
	ret
	.seh_endproc
	.section .rdata,"dr"
.LC1:
	.ascii "Metoda kaze: \0"
	.section	.text$Base::metoda(),"x"
	.linkonce discard
	.align 2
	.globl	Base::metoda()
	.def	Base::metoda();	.scl	2;	.type	32;	.endef
	.seh_proc	Base::metoda()
Base::metoda():
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
	mov	rax, QWORD PTR 16[rbp]	; KORAK5: učitavanje 'this' - Base objekt KORAK9, KORAK12: učitavanje 'this' - sada je to Derived objekt
	mov	rax, QWORD PTR [rax]	; KORAK5, KORAK9, KORAK12: učitavanje vtable pointera
	mov	rdx, QWORD PTR [rax]	; KORAK5, KORAK9, KORAK12: učitavanje adrese virtualne metode na prvom mjestu (virtualnaMetoda)
	mov	rax, QWORD PTR 16[rbp]	; KORAK5, KORAK9, KORAK12: ponovno učitavanje 'this' pointera
	mov	rcx, rax	; KORAK5, KORAK9, KORAK12: postavljamo 'this' kao argument
	call	rdx	; KORAK5: poziv metode u rdc (to je Base::virtualnaMetoda) ; KORAK9, KORAK12: poziv metode u rdc (sada je to Derived::virtualnaMetoda)
	nop
	add	rsp, 32
	pop	rbp
	ret
	.seh_endproc
	.section	.text$Derived::Derived(),"x"
	.linkonce discard
	.align 2
	.globl	Derived::Derived()
	.def	Derived::Derived();	.scl	2;	.type	32;	.endef
	.seh_proc	Derived::Derived()
Derived::Derived():
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
	call	Base::Base()	; KORAK2: poziva se konstruktor Base klase prije 
	lea	rdx, vtable for Derived[rip 16]	; KORAK7: nakon povratka iz konstruktora za Base (i obavljanja metoda unutar njega), postavlja se vtable za Derived
	mov	rax, QWORD PTR 16[rbp]
	mov	QWORD PTR [rax], rdx
	mov	rax, QWORD PTR 16[rbp]
	mov	rcx, rax
	call	Base::metoda()	; KORAK8; poziv Base::metoda()
	nop
	add	rsp, 32
	pop	rbp
	ret
	.seh_endproc
	.section .rdata,"dr"
	.align 8
.LC2:
	.ascii "ja sam izvedena implementacija!\12\0"	; KORAK10, KORAK13: zapis stringa za derived implementaciju
	.section	.text$Derived::virtualnaMetoda(),"x"
	.linkonce discard
	.align 2
	.globl	Derived::virtualnaMetoda()
	.def	Derived::virtualnaMetoda();	.scl	2;	.type	32;	.endef
	.seh_proc	Derived::virtualnaMetoda()
Derived::virtualnaMetoda():
.LFB30:
	push	rbp
	.seh_pushreg	rbp
	mov	rbp, rsp
	.seh_setframe	rbp, 0
	sub	rsp, 32
	.seh_stackalloc	32
	.seh_endprologue
	mov	QWORD PTR 16[rbp], rcx
	lea	rax, .LC2[rip]	; KORAK10, KORAK13: učitavanje stringa
	mov	rcx, rax	; KORAK10, KORAK13: postavljanje stringa kao argumenta
	call	__mingw_printf	; KORAK10, KORAK13: poziv printf()
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
	call	operator new(unsigned long long)
.LEHE0:
	mov	rbx, rax
	mov	edi, 1
	mov	rcx, rbx
.LEHB1:
	call	Derived::Derived()	; KORAK1: poziva se konstruktor za Derived
.LEHE1:
	mov	QWORD PTR -8[rbp], rbx
	mov	rax, QWORD PTR -8[rbp]	; KORAK11: dobivamo objekt 'pd' - pokazivač
	mov	rcx, rax	; KORAK11: postavljamo taj pokazivač kao argument
.LEHB2:
	call	Base::metoda()	; KORAK11: poziv
	mov	eax, 0
	jmp	.L11
.L10:
	mov	rsi, rax
	test	dil, dil
	je	.L9
	mov	edx, 8
	mov	rcx, rbx
	call	operator delete(void*, unsigned long long)
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
	.globl	vtable for Derived
	.section	.rdata$vtable for Derived,"dr"
	.linkonce same_size
	.align 8
vtable for Derived:
	.quad	0
	.quad	typeinfo for Derived
	.quad	Derived::virtualnaMetoda()
	.globl	vtable for Base
	.section	.rdata$vtable for Base,"dr"
	.linkonce same_size
	.align 8
vtable for Base:
	.quad	0
	.quad	typeinfo for Base
	.quad	Base::virtualnaMetoda()
	.globl	typeinfo for Derived
	.section	.rdata$typeinfo for Derived,"dr"
	.linkonce same_size
	.align 8
typeinfo for Derived:
	.quad	vtable for __cxxabiv1::__si_class_type_info 16
	.quad	typeinfo name for Derived
	.quad	typeinfo for Base
	.globl	typeinfo name for Derived
	.section	.rdata$typeinfo name for Derived,"dr"
	.linkonce same_size
	.align 8
typeinfo name for Derived:
	.ascii "7Derived\0"
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
	.def	__gxx_personality_seh0;	.scl	2;	.type	32;	.endef
	.def	__main;	.scl	2;	.type	32;	.endef
	.ident	"GCC: (Rev2, Built by MSYS2 project) 14.2.0"
	.def	operator new(unsigned long long);	.scl	2;	.type	32;	.endef
	.def	operator delete(void*, unsigned long long);	.scl	2;	.type	32;	.endef
	.def	_Unwind_Resume;	.scl	2;	.type	32;	.endef