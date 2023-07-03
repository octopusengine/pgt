from pgt.pygame_tools import PygameTools
from crypto_agama.agama_image_tools import print_rgb, infilt_patt, parse_patt                       # v: "0.2.5"
from crypto_agama.agama_transform_tools import str_to_hex, hex_to_bin, hex_to_bin4, bin_to_hex,bin_to_str,bin_normalize8    # v: "0.3.2"

__version__ = "0.1.0"

DEBUG = False
"""
...
"""


class External_pgt:
    def __init__(self, pygame_instance):
        self.pygame_instance = pygame_instance
    """    
    def process_image_x(self, image_path):
        image = self.pygame_instance.load_image(image_path)
        processed_image = self.pygame_instance.img_matrix(image)
        return processed_image

    def convert_to_gray_x(self, image_path):
        image = self.pygame_instance.load_image(image_path)
        gray_image = self.pygame_instance.img_to_gray(image)
        return gray_image
    """

    def external_test(self):
        print("external_test")



def img_mx_red(pt, path,path_out,image_name,noise=True,save=True,s_mx=(32,32),s_out=(32,32)):
    pt.image_input_path = f"{path}/{image_name}.png"
    ##pt.print_info()
    ##print(pt.print_img_info())

    load_img = pt.img_load(pt.image_input_path)
    matrix_img = pt.img_matrix(load_img, alpha=128, size_mx=s_mx,size_out=s_out)
    if noise:
        matrix_img = pt.img_add_noise(matrix_img, intensity=3)
    
    pt.img_save(matrix_img,f"{path_out}/{image_name}mx{int(s_mx[0])}.png") # resize
    pt.img_info(matrix_img)
    ##print_rgb(matrix_img, width=8, height=8, xy=False)

    matrix_red = pt.img_reduce(matrix_img)
    if save:
        pt.img_save(matrix_red,f"{path_out}/{image_name}mx{int(s_mx[0])}red.png") # reduce
    ##print_rgb(matrix_red, width=8, height=8, xy=False)

    return matrix_red


# 3x64=192 // 192x4=768 // 768/2=384 ok
# 1024/2? = 512
# 6x64=384 // 384/2*8=1536 !!!
# 5x64=320 // > 1280!?
def infilt_txt_normalize(hex,lenh=512,debug=False):
    resid = lenh-len(hex)
    if debug: print("infilt_txt_normalize - resid",resid)
    if resid > 0:
        hex = str(hex) + "7"*resid # "w"=0x77
    else:
        print(f"infilt_txt_normalize Err. (Len>{lenh})")
    return hex


def img_infilt_hex(pt,path_out,image_name,matrix_red,txt_inf,save=True,s_mx=(32,32),hex=True,ch_="R",debug=False):
    if hex:
        pattern = hex_to_bin4(txt_inf)
    else:    
        pattern = hex_to_bin(str_to_hex(txt_inf),to_string=True)
    #matrix_new = infilt_patt(matrix_red,pattern,ch="B")
    if debug: print("DEBUG img_infilt_hex:",pattern,len(pattern),len(pattern)/8)                           
    matrix_new = infilt_patt(matrix_red,pattern,ch=ch_)
    if save:
        pt.img_save(matrix_new,f"{path_out}/{image_name}mx{int(s_mx[0])}data.png") # infilt
    return matrix_new


def img_parse_hex(img,len_bit_patt=1024,hex=False,ch_="R", debug=False):
    if debug: print("DEBUG img_parse_hex - bin:")
    #print(parse_patt(matrix_new,len_bit_patt,ch=ch_))
    pp = bin_normalize8(parse_patt(img,len_bit_patt,ch=ch_))
    #print("parse_patt", "*"*12)
    if debug: print("pp",pp, " > ",len(pp), " /8 > ",len(pp)/8)
    if hex:
        r = bin_to_hex(pp,to_string=True)
    else:
        r = bin_to_str(pp)
    return r 


def img_infilt(pt,path_out,image_name,matrix_red,txt_inf,save=True,s_mx=(32,32),ch_="R"):
    pattern = hex_to_bin(str_to_hex(txt_inf),to_string=True)
    #matrix_new = infilt_patt(matrix_red,pattern,ch="B")
    matrix_new = infilt_patt(matrix_red,pattern,ch=ch_)
    if save:
        pt.img_save(matrix_new,f"{path_out}/{image_name}mx{int(s_mx[0])}data.png") # infilt
    return matrix_new


def img_parse(matrix_new,len_bit_patt=300,hex=False,ch_="R"):
    pp = bin_normalize8(parse_patt(matrix_new,len_bit_patt,ch=ch_))
    #print("parse_patt", "*"*12)
    if DEBUG: print(pp, " > ",len(pp), " /8 > ",len(pp)/8)
    if hex:
        r = bin_to_hex(pp)[2:]
    else:
        r = bin_to_str(pp)
    return r


def parse_V1(text):
    print("="*39)
    text = text.decode()
    #text = text.replace(b'%n', b'\n')
    text = text.replace('---', '%n'+'-'*16+'%n')
    text = text.replace('%n', '\n')
    print(text.rstrip("w"))
    print("="*39)
    return text #.rstrip("w")
