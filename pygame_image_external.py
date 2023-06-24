#!/usr/bin/env python
from pgt.pygame_tools import PygameTools
from pgt.external_pgt import External_pgt # rename 

pt = PygameTools(980, 620)

path = "img_ai"
img_name = "wai1_1"
image_path = f"{path}/{img_name}.png"
pt.image_input_path = image_path
pt.print_info()
print(pt.print_img_info())
pt.set_background_img("img_ai/wai1.png")

external_library = External_pgt(pt)
external_library.external_test()

pt.run()