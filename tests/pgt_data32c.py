#!/usr/bin/env python
##test/ok
from pgt.pygame_tools import PygameTools
from crypto_agama.agama_image_tools import print_rgb, infilt_patt, parse_patt                       # v: "0.2.5"
from crypto_agama.agama_transform_tools import str_to_hex, hex_to_bin, bin_to_str,bin_normalize8    # v: "0.3.2"
from pgt.external_pgt import img_parse, img_infilt, img_mx_red

pt = PygameTools(390, 620) #980
pi = pt.p

size_mx=(32,32)  #size_mx=(32,32) (64,64)
size_out=(32,32)  #size_out=(32,32) (64,64)
path_in = "img_cut" #"img_ai"
path_out = "img_data"
#path, img_name = "img_ai", "wai1_1"

# ========================================================================
image_name = "32" #"punk5x3_06"
matrix_red = img_mx_red(pt,path_in,path_out,image_name)

print("[test] matrix_red1", "*"*12, f"{path_in}/{image_name}.png")
pt.img_info(matrix_red)

#---------------------------------------------------------------------------
#                   1         2         3         4         5         6
#          123456789012345678901234567890123456789012345678901234567890
txt_inf = "king punk test1 king punk test2 king punk test3 more asdfghjkl etc END"
matrix_new = img_infilt(pt, path_out,image_name,matrix_red, txt_inf, save=True)
# img_infilt(pt,path_out,image_name,matrix_red,txt_inf,save=True,s_mx=(32,32)):
#---------------------------------------------------------------------------
pt.image_input_path = f"{path_out}/{image_name}mx{int(size_mx[0])}data.png"
matrix_new_load = pt.img_load(pt.image_input_path) 

print("parse:")
print("="*30)
txt1 = img_parse(matrix_new_load,len_bit_patt=70*8) #2000
print(txt1," > ",len(txt1))
