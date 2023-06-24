#!/usr/bin/env python
##test/ok
from pgt.pygame_tools import PygameTools
#from pgt.external_pgt import External_pgt # rename 

pt = PygameTools(390, 620) #980

path = "img_ai"
img_name = "wai1_1"
pt.image_input_path = f"{path}/{img_name}.png"
pt.head = "AI face"
pt.print_info()
print(pt.print_img_info())

pt.matrix_ai_face = True

##pt.set_background_img("img_ai/wai1.png")
pt.set_background_img()
#external_library = External_pgt(pt)
#external_library.external_test()

pt.import_images()

pt.run()