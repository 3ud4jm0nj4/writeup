def handle(base, exception_offset):
    start_offset = exception_offset
    end_offset = start_offset + 1
    unwind_offset = end_offset  + get_wide_byte(base + end_offset) + 1
    unwind_offset += unwind_offset & 1
    unwind_info =  base + unwind_offset
    #print('UnwindInfo: ' + hex(unwind_info))
    flags = (get_wide_byte(unwind_info) & 0xf8) >> 3 
    #print('FLAG: ' + hex(flags)) 
    sizeofprolog = get_wide_byte(unwind_info + 1) 
    #print('Size of prolog: ' + hex(sizeofprolog))
    countofcode = get_wide_byte(unwind_info + 2)
    #print('COUNT OF CODE: ' + hex(countofcode))
    frame = get_wide_byte(unwind_info + 3)
    fram_reg = frame & 0xf 
    #print('FRAME REG: ' + hex(fram_reg))
    framoffset = (frame & 0xf0) >> 4
    #print('FRAME_OFFSET: ' + hex(framoffset))
    unwindcode = unwind_info + 4
    i = 0
    while i < countofcode:
        k = 0
        #print('Uwincode address: ' + (hex(unwindcode)))
        code_offset = get_wide_byte(unwindcode)
        code = get_wide_byte(unwindcode + 1)
        opcode = (code & 0xf) 
        #print('OPCODE: ' + hex(opcode) + ': ', end='')
        opinfo = (code & 0xf0) >> 4
        if opcode == UWOP_PUSH_NONVOL:
            insn = 'pop ' + regs[opinfo]
            #print(insn)
            exception_offset += patch_asm(base + exception_offset, insn)
            k = 1
        elif opcode == UWOP_ALLOC_LARGE:
            if opinfo != 0:
                insn = 'add rsp, ' + hex(get_wide_dword(unwindcode + 2))
                #print(insn)
                exception_offset += patch_asm(base + exception_offset, insn)
                k = 3
            else:
                insn = 'add rsp, ' + hex(get_wide_word(unwindcode + 2) * 8)
                #print(insn)
                exception_offset += patch_asm(base + exception_offset, insn)
                k = 2
        elif opcode == UWOP_ALLOC_SMALL:
            insn = 'add rsp, ' + hex(8 * (opinfo + 1))
            #print(insn)
            exception_offset += patch_asm(base + exception_offset, insn)
            k = 1
        elif opcode == UWOP_SET_FPREG:
            reg = regs[fram_reg]
            delta = framoffset * 16
            if delta:
                insn = 'mov rsp, ' + reg + ' - ' + hex(delta) +']'
            else:
                insn = 'mov rsp, ' + reg 
            #print(insn)
            exception_offset += patch_asm(base + exception_offset, insn)
            k = 1
        elif opcode == UWOP_SAVE_NONVOL:
            reg = regs[opinfo]
            offset = get_wide_word(unwindcode + 2)
            insn = 'mov ' + reg + ', [rsp + ' + hex(offset) +']'
            #print(insn)
            exception_offset += patch_asm(base + exception_offset, insn)
            k = 2
        elif opcode == UWOP_SAVE_NONVOL_FAR:
            reg = regs[opinfo]
            offset = get_wide_dword(unwindcode + 2)
            insn = 'mov ' + reg + ', [rsp + ' + hex(offset) +']' 
            #print(insn)
            exception_offset += patch_asm(base + exception_offset, insn)
            k = 3
        elif opcode == UWOP_EPILOG:
            k = 1
        elif opcode == UWOP_SPARE_CODE:
            k = 2
        elif opcode == UWOP_PUSH_MACHFRAME:
            insn = 'add rsp, ' + hex(opinfo * 8)
            #print(insn)
            exception_offset += patch_asm(base + exception_offset, insn)
            insn = 'mov rip, [rsp]'
            #print(insn)
            insn = 'mov rsp, [rsp + 0x18]'
            exception_offset += patch_asm(base + exception_offset, insn)
            #print(insn)
            k = 1
        i += k
        unwindcode += k * 2
    countofcode *= 2
    countofcode += countofcode % 4
    handler = base +  get_wide_dword(unwind_info + 4 + countofcode)
    # delta = handler - base - exception_offset - 5
    # patch_byte(base + exception_offset, 0xe9)
    # patch_dword(base + exception_offset + 1, delta)
    # create_insn(base + exception_offset)
    set_cmt(base + start_offset, hex(unwind_info) + ', ' + hex(handler), 0)
    return handler