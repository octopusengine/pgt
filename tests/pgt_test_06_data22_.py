#!/usr/bin/env python
## test 2022/ok
import os, sys
from pgt.pygame_tools import PygameTools
from pgt.external_pgt import infilt_txt_normalize, img_infilt_hex, img_parse_hex, img_mx_red, parse_V1
from crypto_agama.agama_transform_tools import str_to_hex, hex_to_str, hash_sha256_str,short_str   # v: "0.3.2"
from crypto_agama.agama_cipher import xor_crypt
from dotenv import load_dotenv

pt = PygameTools(390, 620) #980
pi = pt.p

size_mx=(32,32)  #size_mx=(32,32) (64,64)
size_out=(32,32)  #size_out=(32,32) (64,64)
path_in = "img_data22" #"img_ai"
path_out = "img_data22"

def get_env_key(key='HASH_HEX'):
    print("[get_env_key] from .env")
    load_dotenv()  # take environment variables from .env.
    if not os.environ.get(key):
        print("You need to set NOSTR_KEY in .env file")
        sys.exit(1)
    return os.environ.get(key)

# ========================================================================
image_name = "root22" #"punk5x3_06"
print("[test] image", "*"*12, f"{path_in}/{image_name}.png")
psw = input("Your passphrase: ")
if psw=="env":
    hash_hex = get_env_key() # .env: HASH_HEX=abc...
else:
    hash_hex = hash_sha256_str(psw)

#-------------------------------------------------------------------------
#                   1         2         3         4         5         6         7         8    85=170
#          123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
txt_inf = "abc123---xor test%nsnad finalni---ale co kdyz text bude jeste o neco vice delsi? Ha?!---Co potom s tim?"
#txt_inf = "root22d.png%nagamapoint.com/root---32x32=1024/4=256---test root22dx%nshAgama END"
# 64 chars = 128 hexa = 128 x 4 = 512 bits
# ========================================================================
matrix_red = img_mx_red(pt,path_in,path_out,image_name)
print("[test] matrix_red1", "*"*12, f"{path_in}/{image_name}.png")
##pt.img_info(matrix_red)

print("--- sha256",hash_hex, len(hash_hex))
hash_hex6=hash_hex*4 # 4x64=256 x 4 = 1024
print("--- hash_hex",short_str(hash_hex6)," > ",len(hash_hex6))          

txt_inf_hex = str_to_hex(txt_inf)
print("--- src hex---",short_str(txt_inf_hex)," > ",len(txt_inf_hex))    

txt_inf_hex_norm = infilt_txt_normalize(txt_inf_hex,lenh=256)       # 256 ideal = 1024 bits
print("--- norm256---",short_str(txt_inf_hex_norm)," > ",len(txt_inf_hex_norm))     # 61626331323377777777777777777 192
#print("-hex_to_bin:",hex_to_bin(txt_inf_hex_norm))                 # 0b110000101100010011000110011000100110010001100110010110100101101001
               
d_hex = txt_inf_hex_norm
k_hex = hash_hex6
x_hex = xor_crypt(d_hex,k_hex)                                  
print("--- xor hex---",short_str(x_hex)," > ",len(x_hex))           
print("test", xor_crypt("616263","52589f") )                   

#x_hex_norm = infilt_txt_normalize(x_hex,lenh=256)
#print("---norm----",x_hex_norm, len(x_hex_norm))              
#print("---bin x4 ---",hex_to_bin4(x_hex))                     # 001100110011101011111100100111011010101001010
"""
--- sha256 52589fac986.......a01bc7d2f4b   > 64
--- hash_hex 52589fac9863...9a01bc7d2f4b   > 256
--- src hex--- 616263313233...3f2048613f21 > 170
--- norm256--- 616263313233...777777777777 > 256
--- xor hex--- 333afc9daa50...ed76cb0a583c > 256
"""
                        
d_hex = xor_crypt(x_hex,k_hex)
print("--- de xor---",short_str(d_hex)," > ",len(x_hex))            
# print("---d---",d_hex.lstrip("0"))
text = hex_to_str(d_hex)
print("--- textOk---",text)                                     # abc123wwwwwwwwwwwwwwwww
parse_V1(text.encode())

##matrix_new = img_infilt(pt, path_out,image_name,matrix_red, txt_inf, save=True)
#matrix_new = img_infilt_hex(pt, path_out,image_name,matrix_red, txt_inf_hex_norm, hex=True,save=True)
matrix_new = img_infilt_hex(pt, path_out,image_name,matrix_red, x_hex, hex=True,save=True,debug=False)

#================================ LOAD ========================================
psw = input("Your passphrase: ")
if psw=="env":
    hash_hex = get_env_key() # .env: HASH_HEX=abc...
else:
    hash_hex = hash_sha256_str(psw)
    
print("--- sha256",hash_hex, len(hash_hex))
hash_hex6=hash_hex*4 # 4x64=256 x 4 = 1024

pt.image_input_path = f"{path_out}/{image_name}mx{int(size_mx[0])}data.png"
matrix_new_load = pt.img_load(pt.image_input_path) 

print("= "*39)
print("LOAD and parse-xor:")
txt_inf_hex = img_parse_hex(matrix_new_load,len_bit_patt=890,hex=True,debug=False) # 768 // 890ok 900Err?

print("- txt_inf_hex:",short_str(txt_inf_hex)," > ",len(txt_inf_hex))
#txt_inf_hex_norm = infilt_txt_normalize(txt_inf_hex)
#print("---bin-4---",hex_to_bin4(txt_inf_hex_norm))                  # 0110000101100010011000110011000100110010001100

txt_inf_hex_norm = infilt_txt_normalize(txt_inf_hex,lenh=256)
print("--- normal ---",short_str(txt_inf_hex_norm)," > ",len(txt_inf_hex_norm) )
d_hex = txt_inf_hex_norm
k_hex = hash_hex6
x_hex = xor_crypt(d_hex,k_hex)
print("--- xor new---",short_str(x_hex)," > ",len(x_hex))

text = hex_to_str(x_hex,code="latin2")
print("---textOk---",text," > ",len(text)) 
text = text[:110]  # [:128] TODO - na konci je nejaky SENO
print("---textOk---",text," > ",len(text)) 
parse_V1(text.encode())
print("."*39)
