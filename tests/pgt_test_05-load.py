#!/usr/bin/env python
##test/ok
from pgt.pygame_tools import PygameTools
from pgt.external_pgt import External_pgt # rename 
#from pgt.data_lib import print_rgb, parse8, infilt_patt, parse_patt
from crypto_agama.agama_transform_tools import bin_to_str,bin_normalize8 # v: "0.3.2"
from crypto_agama.agama_image_tools import print_rgb, parse_patt         # v: "0.2.5"

pt = PygameTools(390, 620) #980
pe = External_pgt(pt)
pi = pt.p

# pt.img_save(matrix_new,"images/mx32data.png")
#load_img = pt.img_load("images/mx32.png")
load_img = pt.img_load("images/mx32data.png")
#load_img = pt.img_load("images/mx32red.png")
pt.img_info(load_img)
print("."*39)
#print_rgb(load_img, 0, True)
print_rgb(load_img, all=True, width=8, height=8)
print("."*39)
#print(load_img.get_at((0,0)))

print("[test5] load", "*"*12)
#matrix_new = infilt_patt(matrix_red,pattern)
#pt.img_save(matrix_new,"images/mx32data.png")
pp = bin_normalize8(parse_patt(load_img))

print("[test] parse_patt", "*"*12)
print(pp, " > ",len(pp), " /8 > ",len(pp)/8)

print("[test] bin_to_str", "*"*12)
txt1 = bin_to_str(pp)
print(txt1," > ",len(txt1))
