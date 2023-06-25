#!/usr/bin/env python
from pgt.pygame_tools import PygameTools
#from pgt.external_pgt import External_pgt # rename 

pt = PygameTools(390, 520) #980

path = "img_ai"
img_name = "wai1_1"
pt.image_input_path = f"{path}/{img_name}.png"

#image.svg
pt.head = "QR code"
pt.drawqr = True
## pt.print_info()
## print(pt.print_img_info())
pt.set_background_img()
pt.matrix_ai_face = False
## pt.import_images()

qr_img = pt.render_qrcode("octopusengine example 123")
#qr_img = pt.render_qrcode("abc")

pt.img_save(qr_img)

pt.run()
