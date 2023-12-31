#!/usr/bin/env python
from pgt.pygame_tools import PygameTools
#from pgt.external_pgt import External_pgt # rename 

pt = PygameTools(390, 890) #980
pt.drawmatrix = True
pt.drawedit = True
pt.drawsvg = True
pt.drawinputfield = True
path = "img_ai"
img_name = "wai1_1"
pt.image_input_path = f"{path}/{img_name}.png"
pt.head = "AI face"

pt.drawcam = True
pt.cam_pos = (30,500)
pt.filt_noise = True
pt.filt_matrix = True
pt.camera_init()

## pt.print_info()
## print(pt.print_img_info())

#pt.img_load(pt.image_input_path)
pt.set_background_img()
pt.drawedit = True
pt.drawinput = True
pt.filt_noise = True
#pt.filt_reduce = True
pt.import_images()
pt.alpha = 196
pt.run()
