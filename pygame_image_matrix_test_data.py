#!/usr/bin/env python
##test/ok
from pgt.pygame_tools import PygameTools
from pgt.external_pgt import External_pgt # rename 

pt = PygameTools(390, 620) #980
pe = External_pgt(pt)
pi = pt.p

path, img_name = "img_ai", "wai1_1"
pt.image_input_path = f"{path}/{img_name}.png"
pt.print_info()
print(pt.print_img_info())
pe.external_test()

# pt.matrix_ai_face = False
load_img = pt.load_image(pt.image_input_path)
test_img = pt.img_to_gray(load_img)
matrix_img = pt.img_matrix(test_img, alpha=128, size_mx=(32,32),size_out=(32,32))
s =pt.img_data(matrix_img) # RGB 32x32 3072 / 1024 3B/px = 24 bit
print(s[0:32])
## pt.set_background_img()
## pt.import_images()
## pt.run()
x, y = 0, 0
pixel_color = matrix_img.get_at((x, y))
print(pixel_color)
matrix_img.set_at((x,y),(12,13,15,32))
pixel_color = matrix_img.get_at((x, y))
print(pixel_color)

print("-"*39)

image = matrix_img
#image_8bit = pt.p.Surface(image.get_size(), pt.p.SRCALPHA, 8)
#image_8bit.blit(image, (0, 0))
image_8bit = image.convert()

s = pt.img_data(image_8bit) # RGB 32x32 3072 / 1024 3B/px = 24 bit
