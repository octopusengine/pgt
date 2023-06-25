#!/usr/bin/env python
##test/ok
from pgt.pygame_tools import PygameTools
from pgt.external_pgt import External_pgt # rename 

pt = PygameTools(980, 620) #980

path = "img_ai"
img_name = "wai1_1"
image_path = f"{path}/{img_name}.png"
pt.image_input_path = image_path
pt.print_info()
print(pt.print_img_info())
##pt.set_background_img("img_ai/wai1.png")
pt.drawedit = True

##pt.import_images()
pt.drawmatrix = True

pt.run()