#!/usr/bin/env python
from pgt.pygame_tools import PygameTools
from crypto_agama.agama_image_tools import margin_cut_image


#image_name = "punk5x3"
image_path = "img_test" #"img_ai"
#input_image = "wai2.png"
img_name ="64x"

pt = PygameTools(320, 620) #980
pi = pt.p

pt.image_input_path = f"{image_path}/{img_name}.png"
print("image_input_path:",pt.image_input_path)
img = pt.img_load(pt.image_input_path)
pt.img_info(img)

pt.drawin_pos = (100,100)
pt.drawinput = True
pt.drawinputfield = True
#pt.drawedit = True

pt.drawoutput = True
pt.drawout_pos = (100,300)

#cut_image(image_path,"punk5x3",m=5,n=3)

#pil_image = margin_cut_image(image_path,img_name,mx=10,mx2=5,my=10,my2=3,save=True)
pil_image = margin_cut_image(image_path,img_name,mx=10,save=True)
pygame_surface = pt.convert_pil2pg(pil_image)

pt.image_output_path = f"{image_path}/{img_name}m5t.png"
pt.img_save(pygame_surface, save_path=pt.image_output_path)
pt.img_info(pygame_surface)

#pt.set_background_img()
pt.run()
