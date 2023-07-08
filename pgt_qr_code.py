#!/usr/bin/env python
from pgt.pygame_tools import PygameTools

pt = PygameTools(390, 520) #980

path = "img_ai"
img_name = "wai1_1"
pt.image_input_path = f"{path}/{img_name}.png"

pt.head = "QR code"
pt.drawqr = True
## print(pt.print_img_info())
pt.set_background_img()
pt.drawinputfield = True
## pt.import_images()

qr_img = pt.render_qrcode("octopusengine example 123")
pt.img_save(qr_img)

pt.run(delay=0.3)
