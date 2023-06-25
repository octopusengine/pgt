#!/usr/bin/env python
from pgt.pygame_tools import PygameTools
#from pgt.external_pgt import External_pgt # rename 

pt = PygameTools(390, 520) #980
pt.drawmatrix = True
pt.drawedit = True
path = "img_ai"
img_name = "wai1_1"
pt.image_input_path = f"{path}/{img_name}.png"
pt.head = "AI face"
## pt.print_info()
## print(pt.print_img_info())

#pt.img_load(pt.image_input_path)
pt.set_background_img()
pt.import_images()
pt.run()
