test_array =[0x179fd,0x2f386,0x4751a,0x5d2cd,0x7230b,0x8917b,0xa0de8,0xb7d00,0xd0742,0xe7b7b,0xff3a3,0x1164ea,0x12ce52,0x14492b,0x15ec1e,0x176fbd,0x190732,0x1a5a58,0x1bc75d,0x1d572b,0x1ecdf1,0x205671,0x21b636,0x22f442,0x243e47,0x25a19e,0x26ec62,0x285d0b,0x29e558,0x2b5f19,0x2cd429,0x2e4b8f]


cmove_array = [0x17a07, 0x2f390, 0x47524, 0x5d2d7, 0x72315, 0x89185, 0xa0df2, 0xb7d0a, 0xd074c, 0xe7b85, 0xff3ad, 0x1164f4, 0x12ce5c, 0x144935, 0x15ec28, 0x176fc7, 0x19073c, 0x1a5a62, 0x1bc767, 0x1d5735, 0x1ecdfb, 0x20567b, 0x21b640, 0x22f44c, 0x243e51, 0x25a1a8, 0x26ec6c, 0x285d15, 0x29e562, 0x2b5f23, 0x2cd433, 0x2e4b99]


base = get_qword(0x14089B8E0)
for i in range(len(test_array)):
    idaapi.create_insn(base+test_array[i])
    add_bpt(base+test_array[i],0,BPT_DEFAULT);
for i in range(len(cmove_array)):
    idaapi.create_insn(base + cmove_array[i])
    add_bpt(base + cmove_array[i], 0, BPT_DEFAULT)
    
for i in range(len(test_array)+len(cmove_array)):  
    ida_dbg.continue_process()
    idaapi.wait_for_next_event(WFNE_SUSP, -1)
    if(idc.print_insn_mnem(get_reg_value("rip"))=="cmovnz"):
        set_reg_value(get_reg_value("rip")+idaapi.create_insn(get_reg_value("rip"))+idaapi.create_insn(get_reg_value("rip")+idaapi.create_insn(get_reg_value("rip"))),"rip")
    else:
        offset = get_reg_value("rip")-base
        value_final = get_reg_value(print_operand(get_reg_value("rip"),0))
        print(hex(value_final),end=",")  
        
f.close()