from z3 import *
def c1():
    result = data[0x4] * 0xef7a8c
    result = result + 0x9d865d8d
    result = result - (data[0x18] * 0x45b53c)
    result = result + 0x18baee57
    result = result - (data[0x0] * 0xe4cf8b)
    result = result + 0x6ec04422
    result = result - (data[0x8] * 0xf5c990)
    result = result + 0x6bfaa656
    result = result ^ (data[0x14] * 0x733178)
    result = result ^ 0x61e3db3b
    result = result ^ (data[0x10] * 0x9a17b8)
    result = result + 0x35d7fb4f
    result = result ^ (data[0xc] * 0x773850)
    result = result ^ 0x5a6f68be
    result = result ^ (data[0x1c] * 0xe21d3d)
    result = result ^ 0x5c911c23
    result = result + 0x7e9b8687
    result &= 0xffffffffffffffff
    return result

def c2():
    result = data[0x11] * 0x99aa81
    result = result + 0x8b1215af
    result = result ^ (data[0x5] * 0x4aba22)
    result = result + 0x598015bf
    result = result ^ (data[0x15] * 0x91a68a)
    result = result ^ 0x6df18e52
    result = result ^ (data[0x1] * 0x942fde)
    result = result + 0x15c825ee
    result = result - (data[0xd] * 0xfe2fbe)
    result = result + 0xd5682b64
    result = result - (data[0x1d] * 0xd7e52f)
    result = result + 0x798bd018
    result = result ^ (data[0x19] * 0xe44f6a)
    result = result + 0x1992adc2
    result = result + (data[0x9] * 0xaf71d6)
    result = result + 0x921121d3
    result = result + 0x1eeb7552
    result &= 0xffffffffffffffff
    return result

def c3():
    result = data[0xa] * 0x48c500
    result = result + 0x70255e44
    result = result - (data[0x1e] * 0x152887)
    result = result + 0x65f04e48
    result = result - (data[0xe] * 0xaa4247)
    result = result ^ 0x3d63ec69
    result = result ^ (data[0x16] * 0x38d82d)
    result = result ^ 0x872eca8f
    result = result ^ (data[0x1a] * 0xf120ac)
    result = result + 0x803dbdcf
    result = result + (data[0x2] * 0x254def)
    result = result ^ 0xee380db3
    result = result ^ (data[0x12] * 0x9ef3e7)
    result = result + 0x921556f5
    result = result + (data[0x6] * 0x69c573)
    result = result + 0x3653a3a3
    result = result + 0xc45c0f3
    result &= 0xffffffffffffffff
    return result

def c4():
    result = data[0xb] * 0x67dda4
    result = result + 0xf4753afc
    result = result + (data[0x1f] * 0x5bb860)
    result = result ^ 0xc1d47fc9
    result = result ^ (data[0x17] * 0xab0ce5)
    result = result + 0x544ff977
    result = result + (data[0x7] * 0x148e94)
    result = result + 0x634c1be7
    result = result - (data[0xf] * 0x9e06ae)
    result = result + 0x5239df9c
    result = result ^ (data[0x3] * 0xfb9de1)
    result = result ^ 0x4e3633f7
    result = result - (data[0x1b] * 0xa8a511)
    result = result ^ 0xa61f9208
    result = result + (data[0x13] * 0xd3468d)
    result = result + 0x4a5d7a48
    result = result + 0x109bee5e
    result &= 0xffffffffffffffff
    return result

def c5():
    result = data[0xc] * 0x640ba9
    result = result + 0x516c7a5c
    result = result - (data[0x0] * 0xf1d9e5)
    result = result + 0x8b424d6b
    result = result + (data[0x1c] * 0xd3e2f8)
    result = result + 0x3802be78
    result = result + (data[0x18] * 0xb558ce)
    result = result + 0xccbe7372
    result = result - (data[0x8] * 0x2f03a7)
    result = result ^ 0xe050b170
    result = result + (data[0x10] * 0xb8fa61)
    result = result ^ 0x1fc22df6
    result = result - (data[0x14] * 0xe0c507)
    result = result ^ 0xd8376e57
    result = result + (data[0x4] * 0x8e354e)
    result = result + 0x2d34cdf8
    result = result + 0xff187080
    result &= 0xffffffffffffffff
    return result

def c6():
    result = data[0x11] * 0xa9b448
    result = result ^ 0x9f938499
    result = result + (data[0x5] * 0x906550)
    result = result + 0x407021af
    result = result ^ (data[0xd] * 0xaa5ad2)
    result = result ^ 0x77cf83a7
    result = result ^ (data[0x1d] * 0xc49349)
    result = result ^ 0x3067f4e7
    result = result + (data[0x9] * 0x314f8e)
    result = result + 0xcd975f3b
    result = result ^ (data[0x15] * 0x81968b)
    result = result + 0x893d2e0b
    result = result - (data[0x19] * 0x5ffbac)
    result = result ^ 0xf3378e3a
    result = result - (data[0x1] * 0xf63c8e)
    result = result + 0xe3e276d5
    result = result + 0x71a14c73
    result &= 0xffffffffffffffff
    return result

def c7():
    result = data[0x16] * 0xa6edf9
    result = result ^ 0x77c58017
    result = result - (data[0x12] * 0xe87bf4)
    result = result + 0x666428c0
    result = result - (data[0x2] * 0x19864d)
    result = result + 0xbe77b413
    result = result + (data[0x6] * 0x901524)
    result = result ^ 0x247bf095
    result = result ^ (data[0xa] * 0xc897cc)
    result = result ^ 0xeff7eea8
    result = result ^ (data[0xe] * 0x731197)
    result = result + 0x67a0d262
    result = result + (data[0x1e] * 0x5f591c)
    result = result + 0x316661f9
    result = result + (data[0x1a] * 0x579d0e)
    result = result + 0xcbd804e4
    result = result + 0x6ff28cb5
    result &= 0xffffffffffffffff
    return result

def c8():
    result = data[0x17] * 0x9afaf6
    result = result ^ 0xdb895413
    result = result + (data[0x13] * 0x7d1a12)
    result = result + 0x398603bc
    result = result + (data[0xb] * 0x4d84b1)
    result = result + 0xa30387dc
    result = result - (data[0xf] * 0x552b78)
    result = result ^ 0xf54a725e
    result = result ^ (data[0x7] * 0xf372a1)
    result = result + 0xb3aefc53
    result = result + (data[0x1f] * 0xb40eb5)
    result = result ^ 0x16fa70d2
    result = result ^ (data[0x3] * 0x9e5c18)
    result = result + 0x38784353
    result = result ^ (data[0x1b] * 0xf2513b)
    result = result + 0xa1fc09f0
    result = result + 0xfe291bf8
    result &= 0xffffffffffffffff
    return result

def c9():
    result = data[0x1c] * 0xac70b9
    result = result + 0xdae0a932
    result = result ^ (data[0x4] * 0xc42b6f)
    result = result ^ 0xbc03104c
    result = result - (data[0x0] * 0x867193)
    result = result + 0xdc48c63a
    result = result - (data[0xc] * 0x6d31fe)
    result = result ^ 0x4baeb6d0
    result = result - (data[0x10] * 0xaaae58)
    result = result + 0x328ede08
    result = result + (data[0x14] * 0x9faa7a)
    result = result + 0xbe0a2c9c
    result = result + (data[0x18] * 0x354ac6)
    result = result ^ 0xd8ad17f1
    result = result - (data[0x8] * 0x3f2acb)
    result = result + 0x74948177
    result = result + 0x9c3ec96d
    result &= 0xffffffffffffffff
    return result

def c10():
    result = data[0x1d] * 0xe9d18a
    result = result ^ 0xcb5557ea
    result = result ^ (data[0x19] * 0x8aa5b9)
    result = result ^ 0x9125a906
    result = result - (data[0x11] * 0x241997)
    result = result + 0x6e46fcb8
    result = result + (data[0x5] * 0xe3da0f)
    result = result + 0x442800ec
    result = result + (data[0xd] * 0xa5f9eb)
    result = result + 0xbde8f9af
    result = result + (data[0x15] * 0xd6e0fb)
    result = result + 0x36268dbd
    result = result + (data[0x1] * 0x8dc36e)
    result = result + 0xc54b7d21
    result = result ^ (data[0x9] * 0xb072ee)
    result = result + 0xd5e54e3f
    result = result + 0x40dfbc25
    result &= 0xffffffffffffffff
    return result

def c11():
    result = data[0x1e] * 0xd14f3e
    result = result ^ 0xa06c215b
    result = result - (data[0x1a] * 0xc5ecbf)
    result = result + 0xb197c5c0
    result = result ^ (data[0x6] * 0x19ff9c)
    result = result ^ 0x66e7d06c
    result = result + (data[0x2] * 0xe3288b)
    result = result ^ 0x80af4325
    result = result ^ (data[0xa] * 0xcfb18c)
    result = result + 0x1ec37c6d
    result = result ^ (data[0x12] * 0xd208e5)
    result = result + 0xf96d2b51
    result = result + (data[0xe] * 0x42240f)
    result = result + 0x78cdd8c3
    result = result - (data[0x16] * 0x1c6098)
    result = result + 0x2c2ba3a6
    result = result + 0xf4c281a5
    result &= 0xffffffffffffffff
    return result

def c12():
    result = data[0xb] * 0x3768cc
    result = result ^ 0x19f61419
    result = result - (data[0x3] * 0x43be16)
    result = result + 0x566cc6a8
    result = result ^ (data[0xf] * 0xb7cca5)
    result = result + 0x6db0599e
    result = result + (data[0x1b] * 0xf6419f)
    result = result ^ 0xbd613538
    result = result ^ (data[0x13] * 0xae52fc)
    result = result + 0x717a44dd
    result = result - (data[0x17] * 0x5eeb81)
    result = result + 0xdd02182d
    result = result ^ (data[0x7] * 0xec1845)
    result = result ^ 0xef8e5416
    result = result + (data[0x1f] * 0x61a3be)
    result = result ^ 0x9288d4fa
    result = result + 0x7e4241fb
    result &= 0xffffffffffffffff
    return result

def c13():
    result = data[0x10] * 0x336e91
    result = result + 0xa1eb20e3
    result = result - (data[0x4] * 0xd45de9)
    result = result + 0xc7e538e6
    result = result + (data[0x8] * 0x76c8f8)
    result = result ^ 0xd8caa2cd
    result = result - (data[0x14] * 0x945339)
    result = result + 0x524d7efa
    result = result + (data[0xc] * 0x4474ec)
    result = result + 0x1b817d33
    result = result ^ (data[0x0] * 0x51054f)
    result = result ^ 0x3321c9b1
    result = result - (data[0x18] * 0xd7eb3b)
    result = result + 0x36f6829d
    result = result - (data[0x1c] * 0xad52e1)
    result = result ^ 0x6ce2191a
    result = result + 0xc64bcbd
    result &= 0xffffffffffffffff
    return result

def c14():
    result = data[0x1d] * 0x725059
    result = result ^ 0xa8b69f6b
    result = result + (data[0x11] * 0x6dcfe7)
    result = result ^ 0x653c249a
    result = result + (data[0x1] * 0x8f4c44)
    result = result ^ 0x68e87685
    result = result - (data[0x9] * 0xd2f4ce)
    result = result + 0x78dc723b
    result = result ^ (data[0xd] * 0xe99d3f)
    result = result + 0xed16797a
    result = result + (data[0x5] * 0xada536)
    result = result + 0x6a5fa557
    result = result - (data[0x19] * 0xe0b352)
    result = result ^ 0x43c00020
    result = result + (data[0x15] * 0x8675b6)
    result = result + 0x34a29213
    result = result + 0xdfe69582
    result &= 0xffffffffffffffff
    return result

def c15():
    result = data[0x2] * 0x4a5e95
    result = result + 0x5ed7a1f1
    result = result + (data[0x16] * 0x3a7b49)
    result = result ^ 0x87a91310
    result = result - (data[0x6] * 0xf27038)
    result = result ^ 0xf64a0f19
    result = result + (data[0x1e] * 0xa187d0)
    result = result + 0x44338ca3
    result = result - (data[0x12] * 0xfc991a)
    result = result ^ 0xf9ddd08f
    result = result - (data[0x1a] * 0x4e947a)
    result = result + 0xa656e8d2
    result = result ^ (data[0xe] * 0x324ead)
    result = result + 0x6965859c
    result = result - (data[0xa] * 0x656b1b)
    result = result + 0x8c112443
    result = result + 0x3e24bb39
    result &= 0xffffffffffffffff
    return result

def c16():
    result = data[0xb] * 0x251b86
    result = result + 0xa751192c
    result = result - (data[0x7] * 0x743927)
    result = result ^ 0xf851da43
    result = result ^ (data[0x1f] * 0x9a3479)
    result = result ^ 0x335087a5
    result = result ^ (data[0x3] * 0x778a0d)
    result = result ^ 0x4bfd30d3
    result = result - (data[0x1b] * 0x7e04b5)
    result = result + 0xa2abfb6b
    result = result ^ (data[0x13] * 0xf1c3ee)
    result = result + 0x460c48a6
    result = result + (data[0xf] * 0x883b8a)
    result = result + 0x7b2ffbdc
    result = result + (data[0x17] * 0x993db1)
    result = result + 0xa98b27fa
    result = result + 0xddf7842c
    result &= 0xffffffffffffffff
    return result

def c17():
    result = data[0x10] * 0xbae081
    result = result + 0x2359766f
    result = result ^ (data[0x18] * 0xc2483b)
    result = result + 0xea986a57
    result = result - (data[0x1c] * 0x520ee2)
    result = result ^ 0xa6ff8114
    result = result + (data[0x8] * 0x9864ba)
    result = result + 0x42833507
    result = result - (data[0x0] * 0x7cd278)
    result = result ^ 0x360be811
    result = result ^ (data[0x4] * 0xbe6605)
    result = result + 0xb36d8573
    result = result + (data[0x14] * 0x3bd2e8)
    result = result + 0xb790cfd3
    result = result - (data[0xc] * 0x548c2b)
    result = result + 0x2a0e04cc
    result = result + 0xdecd786e
    result &= 0xffffffffffffffff
    return result

def c18():
    result = data[0x11] * 0xfb213b
    result = result + 0x988c29bd
    result = result ^ (data[0x9] * 0xde6876)
    result = result ^ 0x8649fde3
    result = result ^ (data[0x1d] * 0x629ff7)
    result = result ^ 0xa0eeb203
    result = result - (data[0x19] * 0xdbb107)
    result = result ^ 0x94aa6b62
    result = result - (data[0x1] * 0x262675)
    result = result + 0x2030ab78
    result = result + (data[0x5] * 0xd691c5)
    result = result + 0xa4c118ba
    result = result - (data[0xd] * 0xcafc93)
    result = result + 0xeee421de
    result = result - (data[0x15] * 0x81f945)
    result = result + 0x6ffcc3f8
    result = result + 0x9cb62931
    result &= 0xffffffffffffffff
    return result

def c19():
    result = data[0xa] * 0x52f44d
    result = result ^ 0x33b3d0e4
    result = result ^ (data[0x1e] * 0xe6e66e)
    result = result + 0xd8a28650
    result = result - (data[0x6] * 0xf98017)
    result = result ^ 0x456e6c1d
    result = result - (data[0xe] * 0x34fcb0)
    result = result ^ 0x28709cd8
    result = result ^ (data[0x2] * 0x4d8ba9)
    result = result + 0xb5482f53
    result = result ^ (data[0x12] * 0x6c7e92)
    result = result + 0x2af1d741
    result = result + (data[0x16] * 0xa4711e)
    result = result ^ 0x22e79af6
    result = result + (data[0x1a] * 0x33d374)
    result = result + 0xee8102f2
    result = result + 0x6c86bd72
    result &= 0xffffffffffffffff
    return result

def c20():
    result = data[0x1b] * 0x65ac37
    result = result + 0x15e586b0
    result = result ^ (data[0x1f] * 0xc6dde0)
    result = result ^ 0x2354cad4
    result = result ^ (data[0xf] * 0x154abd)
    result = result ^ 0xfee57fd5
    result = result ^ (data[0x13] * 0xa5e467)
    result = result + 0x315624ef
    result = result ^ (data[0x17] * 0xb6bed6)
    result = result + 0xad7a4f5b
    result = result - (data[0x7] * 0x832ae7)
    result = result + 0xe961bedd
    result = result + (data[0xb] * 0xc46330)
    result = result + 0xb561e29b
    result = result ^ (data[0x3] * 0x3f8467)
    result = result ^ 0x95a6a1c4
    result = result + 0xeef1cae7
    result &= 0xffffffffffffffff
    return result

def c21():
    result = data[0x18] * 0xb74a52
    result = result ^ 0x8354d4e8
    result = result ^ (data[0x4] * 0xf22ecd)
    result = result + 0xcb340dc5
    result = result + (data[0x14] * 0xbef4be)
    result = result ^ 0x60a6c39a
    result = result ^ (data[0x8] * 0x7fe215)
    result = result + 0xb14a7317
    result = result - (data[0x10] * 0xdb9f48)
    result = result + 0x4356fa0e
    result = result - (data[0x1c] * 0xbb4276)
    result = result + 0x6df1ddb8
    result = result ^ (data[0x0] * 0xa3fbef)
    result = result + 0x4c22d2d3
    result = result ^ (data[0xc] * 0xc5e883)
    result = result ^ 0x50a6e4c9
    result = result + 0x271a433a
    result &= 0xffffffffffffffff
    return result

def c22():
    result = data[0xd] * 0x4b2d02
    result = result ^ 0x4b59b93a
    result = result - (data[0x9] * 0x84bb2c)
    result = result ^ 0x42d5652c
    result = result ^ (data[0x19] * 0x6f2d21)
    result = result + 0x1020133a
    result = result + (data[0x1d] * 0x5fe38f)
    result = result + 0x9d7f84e0
    result = result + (data[0x15] * 0xea20a5)
    result = result ^ 0x60779ceb
    result = result ^ (data[0x11] * 0x5c17aa)
    result = result ^ 0x1aaf8a2d
    result = result - (data[0x5] * 0xb9feb0)
    result = result + 0x5241fd05
    result = result - (data[0x1] * 0x782f79)
    result = result + 0x303ed7ca
    result = result + 0xb77294fa
    result &= 0xffffffffffffffff
    return result

def c23():
    result = data[0x6] * 0x608d19
    result = result + 0xd1119d14
    result = result - (data[0xe] * 0xbe18f4)
    result = result ^ 0xb86f9b72
    result = result ^ (data[0x1e] * 0x88dec9)
    result = result + 0xaf5cd797
    result = result ^ (data[0x12] * 0xb68150)
    result = result + 0xc2f8c45b
    result = result + (data[0x16] * 0x4d166c)
    result = result + 0xbb1e1039
    result = result - (data[0x2] * 0x495e3f)
    result = result + 0xe727b98e
    result = result - (data[0xa] * 0x5caba1)
    result = result + 0xe5c3093f
    result = result + (data[0x1a] * 0x183a4d)
    result = result + 0x35fc681f
    result = result + 0x997b5ce3
    result &= 0xffffffffffffffff
    return result

def c24():
    result = data[0xb] * 0xffd0ca
    result = result + 0x70d93118
    result = result ^ (data[0x7] * 0xbf2b59)
    result = result + 0xc76bad6e
    result = result + (data[0x17] * 0x29df01)
    result = result + 0xeef034a2
    result = result ^ (data[0x1b] * 0xbbda1d)
    result = result + 0x5923194e
    result = result - (data[0x1f] * 0x5d24a5)
    result = result + 0x7eeff867
    result = result + (data[0xf] * 0x3dc505)
    result = result + 0x9645116f
    result = result ^ (data[0x13] * 0x4e25a6)
    result = result + 0x2468b30a
    result = result - (data[0x3] * 0xae1920)
    result = result ^ 0xd3db6142
    result = result + 0x44850ff1
    result &= 0xffffffffffffffff
    return result

def c25():
    result = data[0x4] * 0xf56c62
    result = result ^ 0x6c7d1f41
    result = result + (data[0x10] * 0x615605)
    result = result + 0x5b52f6ee
    result = result + (data[0x14] * 0x828456)
    result = result ^ 0x6f059759
    result = result - (data[0x1c] * 0x50484b)
    result = result + 0x84e222af
    result = result ^ (data[0x8] * 0x89d640)
    result = result + 0xfd21345b
    result = result - (data[0x18] * 0xe4b191)
    result = result + 0xfe15a789
    result = result ^ (data[0x0] * 0x8c58c1)
    result = result ^ 0x4c49099f
    result = result + (data[0xc] * 0xa13c4c)
    result = result ^ 0x27c5288e
    result = result + 0xff6724f5
    result &= 0xffffffffffffffff
    return result

def c26():
    result = data[0x1] * 0x73aaf0
    result = result ^ 0xa04e34f1
    result = result + (data[0x1d] * 0xf61e43)
    result = result + 0xd09b66f3
    result = result + (data[0x19] * 0x8cb5f0)
    result = result + 0xc11c9b4b
    result = result ^ (data[0x11] * 0x4f53a8)
    result = result + 0x9b9a98d2
    result = result + (data[0x9] * 0xb2e1fa)
    result = result ^ 0x77c07fd8
    result = result - (data[0x15] * 0xb8b7b3)
    result = result + 0x77d3eadf
    result = result + (data[0xd] * 0x13b807)
    result = result ^ 0x758dd142
    result = result ^ (data[0x5] * 0xdd40c4)
    result = result + 0xbb68781a
    result = result + 0x4fa227c4
    result &= 0xffffffffffffffff
    return result

def c27():
    result = data[0xe] * 0xca894b
    result = result + 0xa34fe406
    result = result + (data[0x12] * 0x11552b)
    result = result + 0x3764ecd4
    result = result ^ (data[0x16] * 0x7dc36b)
    result = result + 0xb45e777b
    result = result ^ (data[0x1a] * 0xcec5a6)
    result = result ^ 0x2d59bc15
    result = result + (data[0x1e] * 0xb6e30d)
    result = result ^ 0xfab9788c
    result = result ^ (data[0xa] * 0x859c14)
    result = result + 0x41868e54
    result = result + (data[0x6] * 0xd178d3)
    result = result + 0x958b0be3
    result = result ^ (data[0x2] * 0x61645c)
    result = result + 0x9dc814cf
    result = result + 0x847feabe
    result &= 0xffffffffffffffff
    return result

def c28():
    result = data[0x1b] * 0x7239e9
    result = result + 0x89f1a526
    result = result - (data[0x3] * 0xf1c3d1)
    result = result + 0x10d75f98
    result = result ^ (data[0xb] * 0x1b1367)
    result = result ^ 0x31e00d5a
    result = result ^ (data[0x13] * 0x8038b3)
    result = result + 0xb5163447
    result = result + (data[0x1f] * 0x65fac9)
    result = result + 0xe04a889a
    result = result - (data[0x17] * 0xd845ca)
    result = result + 0x5482e3a8
    result = result + (data[0xf] * 0xb2bbbc)
    result = result ^ 0x3a017b92
    result = result ^ (data[0x7] * 0x33c8bd)
    result = result + 0x540376e3
    result = result + 0x4f17f36d
    result &= 0xffffffffffffffff
    return result

def c29():
    result = data[0x0] * 0x53a4e0
    result = result + 0x9f9e7fc2
    result = result - (data[0x10] * 0x9bbfda)
    result = result + 0x69b383f1
    result = result - (data[0x18] * 0x6b38aa)
    result = result + 0x68ece860
    result = result + (data[0x14] * 0x5d266f)
    result = result + 0x5a4b0e60
    result = result - (data[0x8] * 0xedc3d3)
    result = result ^ 0x93e59af6
    result = result - (data[0x4] * 0xb1f16c)
    result = result ^ 0xe8d2b9a9
    result = result + (data[0xc] * 0x1c8e5b)
    result = result + 0x977c6d7d
    result = result + (data[0x1c] * 0x78f67b)
    result = result + 0xac22677
    result = result + 0xb154dea3
    result &= 0xffffffffffffffff
    return result

def c30():
    result = data[0x11] * 0x87184c
    result = result + 0x8d5ea528
    result = result ^ (data[0x19] * 0xf6372e)
    result = result + 0x16ad4f89
    result = result - (data[0x15] * 0xd7355c)
    result = result + 0x44df01cb
    result = result ^ (data[0x5] * 0x471dc1)
    result = result ^ 0x572c95f4
    result = result - (data[0x1] * 0x8c4d98)
    result = result + 0x6b9af38c
    result = result - (data[0xd] * 0x5ceea1)
    result = result ^ 0xf703dcc1
    result = result - (data[0x1d] * 0xeb0863)
    result = result + 0xad3bc09d
    result = result ^ (data[0x9] * 0xb6227f)
    result = result + 0xb95195e9
    result = result + 0xcea17ee8
    result &= 0xffffffffffffffff
    return result

def c31():
    result = data[0x1e] * 0x8c6412
    result = result ^ 0xc08c361c
    result = result ^ (data[0xe] * 0xb253c4)
    result = result + 0x21bb1147
    result = result + (data[0x2] * 0x8f0579)
    result = result + 0x596ee7a
    result = result - (data[0x16] * 0x7ac48a)
    result = result + 0xbb787dd5
    result = result + (data[0xa] * 0x2737e6)
    result = result ^ 0xa2bb7683
    result = result - (data[0x12] * 0x4363b9)
    result = result ^ 0x88c45378
    result = result ^ (data[0x6] * 0xb38449)
    result = result + 0xdf623f88
    result = result + (data[0x1a] * 0x6e1316)
    result = result + 0x1343dee9
    result = result + 0x1c966ad9
    result &= 0xffffffffffffffff
    return result

def c32():
    result = data[0x13] * 0x390b78
    result = result + 0x7d5deea4
    result = result - (data[0xf] * 0x70e6c8)
    result = result + 0x915cc61e
    result = result ^ (data[0x1b] * 0xd8a292)
    result = result + 0xd772913b
    result = result - (data[0x17] * 0x978c71)
    result = result + 0x1a27a128
    result = result + (data[0x1f] * 0x9a14d4)
    result = result + 0x49698f34
    result = result ^ (data[0x7] * 0x995144)
    result = result + 0x2d188cbe
    result = result ^ (data[0xb] * 0x811c39)
    result = result + 0xd22fca9b
    result = result ^ (data[0x3] * 0x9953d7)
    result = result ^ 0x80877669
    result = result + 0x6bddb88
    result &= 0xffffffffffffffff
    return result


data = [BitVec(f'data{i}', 8) for i in range(32)]

s = Solver()


s.add(c1() == 0)
s.add(c2() == 0)
s.add(c4() == 0)
s.add(c3() == 0)
s.add(c5() == 0)
s.add(c6() == 0)
s.add(c7() == 0)
s.add(c8() == 0)
s.add(c9() == 0)
s.add(c10() == 0)
s.add(c11() == 0)
s.add(c12() == 0)
s.add(c13() == 0)
s.add(c14() == 0)
s.add(c15() == 0)
s.add(c16() == 0)
s.add(c17() == 0)
s.add(c18() == 0)
s.add(c19() == 0)
s.add(c20() == 0)
s.add(c21() == 0)
s.add(c22() == 0)
s.add(c23() == 0)
s.add(c24() == 0)
s.add(c25() == 0)
s.add(c26() == 0)
s.add(c27() == 0)
s.add(c28() == 0)
s.add(c29() == 0)
s.add(c30() == 0)
s.add(c31() == 0)
s.add(c32() == 0)

def print_all_sat(solver):
    solutions = []
    while solver.check() == sat:
        model = solver.model()
        result = ''.join(chr(model[byte].as_long()) for byte in data)
        print("SAT Solution:")
        print(result)
        exclusion = Or([byte != model[byte] for byte in data])
        solver.add(exclusion)

print_all_sat(s)