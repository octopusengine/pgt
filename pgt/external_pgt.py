from pgt.pygame_tools import PygameTools
from crypto_agama.agama_image_tools import print_rgb, infilt_patt, parse_patt                       # v: "0.2.5"
from crypto_agama.agama_transform_tools import str_to_hex, hex_to_bin, bin_to_str,bin_normalize8    # v: "0.3.2"

__version__ = "0.0.3"

DEBUG = False
"""
...
"""


class External_pgt:
    def __init__(self, pygame_instance):
        self.pygame_instance = pygame_instance

    def process_image_x(self, image_path):
        image = self.pygame_instance.load_image(image_path)
        processed_image = self.pygame_instance.img_matrix(image)
        return processed_image

    def convert_to_gray_x(self, image_path):
        image = self.pygame_instance.load_image(image_path)
        gray_image = self.pygame_instance.img_to_gray(image)
        return gray_image

    def external_test(self):
        print("external_test")
    # Další metody externí knihovny


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


def img_infilt(pt,path_out,image_name,matrix_red,txt_inf,save=True,s_mx=(32,32),ch_="R"):
    pattern = hex_to_bin(str_to_hex(txt_inf),to_string=True)
    #matrix_new = infilt_patt(matrix_red,pattern,ch="B")
    matrix_new = infilt_patt(matrix_red,pattern,ch=ch_)
    if save:
        pt.img_save(matrix_new,f"{path_out}/{image_name}mx{int(s_mx[0])}data.png") # infilt
    return matrix_new


def img_parse(matrix_new,len_bit_patt=300,ch_="R"):
    pp = bin_normalize8(parse_patt(matrix_new,len_bit_patt,ch=ch_))
    #print("parse_patt", "*"*12)
    if DEBUG: print(pp, " > ",len(pp), " /8 > ",len(pp)/8)
    txt = bin_to_str(pp)
    return txt
