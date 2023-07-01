#!/usr/bin/env python
## test/ok
from pgt.pygame_tools import PygameTools
from pgt.external_pgt import External_pgt # rename 
#from pgt.data_lib import parse_patt
from crypto_agama.agama_image_tools import print_rgb, infilt_patt, parse_patt                       # v: "0.2.5"
from crypto_agama.agama_transform_tools import str_to_hex, hex_to_bin, bin_to_str,bin_normalize8    # v: "0.3.2"

pt = PygameTools(390, 620) #980
pe = External_pgt(pt)
pi = pt.p

print("[test0] load", "*"*12)
path, img_name = "img_ai", "wai1_1"
pt.image_input_path = f"{path}/{img_name}.png"
##pt.print_info()
##print(pt.print_img_info())

load_img = pt.img_load(pt.image_input_path)
matrix_img = pt.img_matrix(load_img, alpha=128, size_mx=(32,32),size_out=(32,32))
pt.img_save(matrix_img,"images/mx32.png") # resize
##pt.img_info(matrix_img)
##print_rgb(matrix_img, width=8, height=8)

matrix_red = pt.img_reduce(matrix_img)
pt.img_save(matrix_red,"images/mx32red.png") # reduce

print("[test1] matrix_red1", "*"*12, "images/mx32red.png")
pt.img_info(matrix_red)
##print_rgb(matrix_red, width=8, height=8)

# -------------------- 02 -------------------------------------
pattern_ = "001101010011010100110101001101010011010111111"
txt_inf = "basic red_ch 1bit abc128"
pattern = hex_to_bin(str_to_hex(txt_inf),to_string=True)

print("[test2] infilt_patt", "*"*12, "images/mx32red.png")
print(pattern, len(pattern))
#matrix_new = infilt_patt(matrix_red,pattern,ch="B")
matrix_new = infilt_patt(matrix_red,pattern)
     
print("--- img_save")
print("obj",matrix_new)
pt.img_info(matrix_new)
##print_rgb(matrix_new)
pt.img_save(matrix_new,"images/mx32data.png")

print("src:")
print(pattern)
print("parse:")
print("="*30)
##print(parse8(matrix_new))
"""
101000000000000000000000 > 10100000 [len 8]
"""
#pp = parse_patt(matrix_new).rstrip('0')
pp = bin_normalize8(parse_patt(matrix_new))

print("[test] parse_patt", "*"*12)
print(pp, " > ",len(pp), " /8 > ",len(pp)/8)
print("="*30,"src. pattern:")
print(pattern," > ", len(pattern)," /8 > ",len(pattern)/8)

print("[test] bin_to_str", "*"*12)
txt1 = bin_to_str(pp)
print(txt1," > ",len(txt1))

"""
...
--- img_save
obj <Surface(32x32x32 SW)>
image_info:(32x32)
flags: 65536
bit size: 32
images/mx32data.png
Image was successfully saved.
src:
11000010110001001100011001000000110101001100101011001000...00111000
parse:
==============================
[test] parse_patt ************
11000010110001001100011001000000110101001100101011001000...00111000  >  215  /8 >  26.875
============================== src. pattern:
111010000100000011000010110001001100011001100010011001000111000  >  191  /8 >  23.875
[test] bin_to_str ************
b'basic red_ch 1bit abc128'  >  24
"""