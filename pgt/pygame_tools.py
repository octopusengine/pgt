#!/usr/bin/env python

import os, random
import pygame as p
import pygame.camera as cam
from PIL import Image # convert_pil2pg
from time import sleep
import cairosvg
import qrcode
from io import BytesIO

__version__ = "0.1.6"

"""
pygame tools - for experimentation, testing and fun
"""

# basic colors
WHITE = (255, 255, 255)
SILVER = (64, 64, 64)
SILVER2 = (128, 128, 128)
BLACK2 = (10, 10, 10)
BLACK = (0, 0, 0)
GREEN = (0, 196, 0)
COLOR = GREEN
COLOR2 = (0, 128, 0)
RED = (255,0,0)
BLUE = (0,0,255)
ORANGE = (255,165,0)
DARKORANGE = (255,140,0)

X0 = 30
CHECKSIZE = 30

class PygameTools:
    def __init__(self, window_width=640, window_height=480, mode = 1):
        self.p = p
        self.width = window_width
        self.height = window_height
        self.mode = mode
        self.screen = p.display.set_mode((window_width, window_height))
        self.clock = p.time.Clock()
        self.timer = False
        self.background_image = None
        self.background_alpha = 128
        self.resize = 1
        self.alpha = 128
        self.label = "label"
        self.head = "test head"
        self.status = "status line"
        self.input_text = ""
        self.checkbox1 = False
        self.checkbox2 = False
        self.checkbox3 = False
        self.label_ch1 = "filter 1"
        self.label_ch2 = "filter 2"
        self.label_ch3 = "filter 3"
        self.image_input_path = ""
        self.image_output_path = ""
        self.images_source = "images_source"
        self.files = []
        self.contrast = 1.5
        self.image_in = None    # original / first
        self.image_out = None   # edited   / second
        self.delay = 0.01
        self.drawinputfield = False
        self.drawinfield_pos = (30,450)
        self.drawmatrix = False
        self.drawinput = False
        self.drawin_pos = (630,100)
        self.drawoutput = False
        self.drawout_pos = (630,100)
        self.drawedit = False
        self.drawsvg = False
        self.drawqr = False
        self.drawcheckbox = False
        self.ch1_pos = (X0,500)
        self.ch2_pos = (X0,540)
        self.ch3_pos = (X0,580)
        self.qrdata = "octopusengine test"
        self.qr_pos = (X0,100)
        self.svgx = 0
        self.filt_matrix = False
        self.filt_noise = False
        self.filt_onebit = False
        self.filt_reduce = False
        self.drawcam = False
        self.camera = None
        self.cam_pos = (X0,100)

        self.mouse_button_pressed = False
        p.init()
        #window = p.display.set_mode((window_width, window_height))
        p.display.set_caption(f"py_game_tool (ver. {__version__})")

        font_size, font_size1, font_size2 = 18, 39, 25
        self.font = p.font.SysFont("Grand9K Pixel", font_size)
        self.font1 = p.font.SysFont("Grand9K Pixel", font_size1)
        self.font2 = p.font.SysFont("Grand9K Pixel", font_size2)
        #self.font = p.font.SysFont("Arial", font_size)
        #font = p.font.SysFont(None, font_size) #Arial

        
    def print_info(self):
        print("ver.", p.ver)
        print(f"window setup: {self.width}x{self.height}")
        ## print(f"display.list_modes:",p.display.list_modes())


    def set_background_img(self, img_path="background.png"):
        self.background_image = self.img_load(img_path) # p.image.load(img_path)
        self.background_image = p.transform.scale(self.background_image, (self.width, self.height))


    def import_images(self):
        self.files = [file for file in os.listdir(self.images_source) if file.endswith(".png")]
        sorted_files = sorted(self.files)
        print(sorted_files)


    def convert_pil2pg(self,pil_image):
        #pil_image = Image.open('image.png')
        pil_image = pil_image.convert('RGB')
        pygame_surface = p.image.frombuffer(pil_image.tobytes(), pil_image.size, 'RGB')
        return pygame_surface


    def camera_init(self):
        print("camera init")
        cam.init()
        self.camera = cam.Camera(cam.list_cameras()[0])
        self.camera.start()


    def render_qrcode(self,data = "",box=10):
        if len(data)>1:
            self.qrdata = data
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=box, border=2)
        qr.add_data(self.qrdata)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Convert the QR code image to a byte array
        byte_array = BytesIO()
        qr_image.save(byte_array, format="PNG")
        byte_array.seek(0)

        # Create a Pygame surface from the byte array
        pygame_image = p.image.load_extended(byte_array)
        draw_image = p.transform.scale(pygame_image , (310,310))
        return draw_image


    def render_svg(self,x=0,y=0, alpha=32):
        svg_file = 'image.svg'
        angle = 45
        #renderPM.drawToFile(drawing, "image.png", fmt="PNG")
        cairosvg.svg2png(url=svg_file, write_to='image_temp.png')
        #cairosvg.svg2png(url=svg_file, write_to='image.png', output_height=500, output_width=500, rotate=angle)
        image = p.image.load('image_temp.png')
        #alpha = 128  # 50% transparency
        image.set_alpha(alpha)
        image = p.transform.scale(image , (32, 32))
        image2 = p.transform.scale(image , (320, 320))
        self.screen.blit(image, (x, y))
        self.screen.blit(image2, (x, y))
        return image


    def img_matrix(self, matrix_image, alpha=128, size_mx=(32,32),size_out=(256,256)): 
        if alpha>0:       
            matrix_image.set_alpha(alpha)
        
        rx = random.randint(0, 5)
        if rx>2:
            matrix_image = p.transform.scale(matrix_image , (size_mx)) # 32,32
        else:
            matrix_image = p.transform.scale(matrix_image , (64,64))
        matrix_image = p.transform.scale(matrix_image , (size_out))
        return matrix_image


    def img_add_noise(self, image, intensity):
        # Load the image
        img_surface = image # p.image.load(image).convert_alpha()

        # Get the width and height of the image
        width = img_surface.get_width()
        height = img_surface.get_height()

        # Iterate over each pixel in the image
        for x in range(width):
            for y in range(height):
                # Get the pixel color at (x, y)
                color = img_surface.get_at((x, y))

                # Add random noise to each color channel
                r = min(255, max(0, color.r + random.randint(-intensity, intensity)))
                g = min(255, max(0, color.g + random.randint(-intensity, intensity)))
                b = min(255, max(0, color.b + random.randint(-intensity, intensity)))

                # Set the modified pixel color
                img_surface.set_at((x, y), (r, g, b))

        return img_surface


    def img_fill(self, img_surface, col=(128,128,128,255)):
        width = img_surface.get_width()
        height = img_surface.get_height()

        # Iterate over each pixel in the image
        for x in range(width):
            for y in range(height):
                img_surface.set_at((x, y), (col))

        return img_surface


    def img_reduce(self, img_surface, red_col_min = (2,2,2), red_col_max = (252,252,252), even = True):
        width = img_surface.get_width()
        height = img_surface.get_height()

        # Iterate over each pixel in the image
        for x in range(width):
            for y in range(height):
                # Get the pixel color at (x, y)
                r, g, b, a = img_surface.get_at((x, y)) # color

                r = max(min(r, red_col_max[0]), red_col_min[0])
                g = max(min(g, red_col_max[1]), red_col_min[1])
                b = max(min(b, red_col_max[2]), red_col_min[2])

                if even:
                    if r % 2 != 0: r += 1
                    if g % 2 != 0: g += 1
                    if b % 2 != 0: b += 1

                img_surface.set_at((x, y), (r, g, b, a))

        return img_surface


    def img_to_onebit(self, image):
        # Load the image
        img_surface = image # p.image.load(image).convert_alpha()

        onebit_surface = p.Surface(img_surface.get_size(), p.SRCALPHA, 1)

        # Iterate over each pixel in the image
        for x in range(img_surface.get_width()):
            for y in range(img_surface.get_height()):
                # Get the pixel color at (x, y)
                color = img_surface.get_at((x, y))

                # Calculate the grayscale value of the pixel
                grayscale = (color.r + color.g + color.b) // 3

                # Set the color of the pixel in the one-bit surface based on the grayscale value
                if grayscale < 128:
                    onebit_surface.set_at((x, y), p.Color('black'))
                else:
                    onebit_surface.set_at((x, y), p.Color('white'))

        # Convert the image to black and white using a threshold of 128
        #img_surface.convert_threshold(128, p.Color('black'), p.Color('white'), (0, 0, 0, 255), (255, 255, 255, 255))
        return onebit_surface
        

    def img_data(self,image, format="RGB"):
        """
        image_in: img_ai/wai1_1.png (262x261)
        flags: 65536, bit size: 32
        RGB 262x261 205146
        """
        try:
            width, height = image.get_size()
            s = p.image.tobytes(image, format)
            print(format, f"{width}x{height}", len(s))
            return s
        except Exception as e:
            print(f"img_data Err: {e}")


    def img_to_gray(self, input_image):
        width, height = input_image.get_size()
        img_surface = input_image
        #grayscale_image = p.Surface((width, height))
        # Convert the image to grayscale
        ##grayscale_surface = p.Surface(img_surface.get_size()).convert_alpha()
        grayscale_surface = self.img_to_gray(img_surface)

        ###p.transform.threshold(grayscale_surface, img_surface, (0, 0, 0), (255, 255, 255), (128, 128, 128), 0, (0, 0, 0, 255))

        # Create a new surface with one-bit color depth
        onebit_surface = p.Surface(img_surface.get_size(), p.SRCALPHA, 1)

        # Iterate over each pixel in the grayscale surface
        for x in range(grayscale_surface.get_width()):
            for y in range(grayscale_surface.get_height()):
                # Get the pixel color at (x, y)
                color = grayscale_surface.get_at((x, y))

                # Set the color of the pixel in the one-bit surface based on the grayscale value
                if color.r < 128:
                    onebit_surface.set_at((x, y), p.Color('black'))
                else:
                    onebit_surface.set_at((x, y), p.Color('white'))

        return onebit_surface


    def draw_checkbox(self):
        p.draw.rect(self.screen, COLOR, (self.ch1_pos[0],self.ch1_pos[1], CHECKSIZE, CHECKSIZE), 2)
        p.draw.rect(self.screen, COLOR, (self.ch2_pos[0],self.ch2_pos[1], CHECKSIZE, CHECKSIZE), 2)
        p.draw.rect(self.screen, COLOR, (self.ch3_pos[0],self.ch3_pos[1], CHECKSIZE, CHECKSIZE), 2)

        if self.checkbox1:
            p.draw.rect(self.screen, COLOR2, (self.ch1_pos[0] + 2, self.ch1_pos[1] + 2, CHECKSIZE-4, CHECKSIZE-4))
        if self.checkbox2:
            p.draw.rect(self.screen, COLOR2, (self.ch2_pos[0] + 2, self.ch2_pos[1] + 2, CHECKSIZE-4, CHECKSIZE-4))
        if self.checkbox3:
            p.draw.rect(self.screen, COLOR2, (self.ch3_pos[0] + 2, self.ch3_pos[1] + 2, CHECKSIZE-4, CHECKSIZE-4))

        #labels
        self.draw_text(self.label_ch1, self.ch1_pos[0]+CHECKSIZE+5,self.ch1_pos[1])
        self.draw_text(self.label_ch2, self.ch2_pos[0]+CHECKSIZE+5,self.ch2_pos[1])
        self.draw_text(self.label_ch3, self.ch3_pos[0]+CHECKSIZE+5,self.ch3_pos[1])


    def draw_text(self, text, x, y, col = COLOR): # Function to draw label/text
        text_surface = self.font.render(text, True, col)
        self.screen.blit(text_surface, (x, y))


    def draw_text2(self, text, x, y, col = COLOR2):
        text_surface = self.font1.render(text, True, col)
        self.screen.blit(text_surface, (x, y))


    def draw_status(self):
        a = 15
        xi, yi =self.width, self.height - 3 * a
        xi,yi=10,50
        self.draw_text(self.status, xi,yi)


    def img_load(self, img_path):
        try:
            image = p.image.load(img_path)
            return image
        #except p.error:
        except Exception as e:
            print(f"img_load Err: {e}")


    def print_img_info(self):
        self.image_in = self.img_load(self.image_input_path)
        width, height = self.image_in.get_size()
        #mode = self.image_in.get_mode()
        flags = self.image_in.get_flags()
        color_format = p.display.get_surface().get_flags()

        depth = self.image_in.get_bitsize()
        print("image_in:",self.image_input_path,f"({width}x{height})")
        print("flags:",flags)
        print("bit size:",depth)
        #image_8bit = self.image_in.convert(8)
        #return p.image.tostring(image_8bit, "P") # RGB ok,
    
    """
        P, 8-bit palettized Surfaces
        RGB, 24-bit image
        RGBX, 32-bit image with unused space
        RGBA, 32-bit image with an alpha channel
        ARGB, 32-bit image with alpha channel first
        BGRA, 32-bit image with alpha channel, red and blue channels swapped
        RGBA_PREMULT, 32-bit image with colors scaled by alpha channel
        ARGB_PREMULT, 32-bit image with colors scaled by alpha channel, alpha channel first
    """
     
    def img_info(self, img):        
        width, height = img.get_size()
        flags = img.get_flags()
        color_format = p.display.get_surface().get_flags()

        depth = img.get_bitsize()
        print("image_info:"f"({width}x{height})")
        print("flags:",flags)
        print("bit size:",depth)
    

    def img_save(self, image, save_path="images/temp.png"):
        print(save_path)
        try:
            p.image.save(image, save_path)
            print("Image was successfully saved.")
        except p.error:
            print("Failed to save the image.")
        

    def draw_input_field(self):
        a = 18
        #xi, yi =10, self.height - 3 * a
        xi, yi = self.drawinfield_pos
        self.draw_text("New filename:",xi, yi, COLOR2)
        p.draw.rect(self.screen, SILVER, (xi, yi, 310, a*2))
        p.draw.rect(self.screen, BLACK2, (xi, yi, 310, a*2), 2)
        text_surface = self.font.render(self.input_text, True, COLOR)
        self.screen.blit(text_surface, (xi+5, yi+2))


    def draw_qr(self):
        qr_img = self.render_qrcode()
        self.screen.blit(qr_img, self.qr_pos)


    def draw_img_in(self):
        try:
            self.image_in = self.img_load(self.image_input_path)
            original_width, original_height = self.image_in.get_size()
            self.screen.blit(self.image_in, self.drawin_pos)
            ##self.screen.blit(p.transform.scale(image_edit, (current_width, current_height)), (window_width/2+100, y0))
        except Exception as e:
            print(f"draw_img_in Err: {e}")

    
    def draw_img_out(self):
        try:
            self.image_out = self.img_load(self.image_output_path)
            original_width, original_height = self.image_out.get_size()
            self.screen.blit(self.image_out, self.drawout_pos)
            ##self.screen.blit(p.transform.scale(image_edit, (current_width, current_height)), (window_width/2+100, y0))
        except Exception as e:
            print(f"draw_img_out Err: {e}")


    def draw_img(self, img, position=(30,100)):                      
        try:
            self.screen.blit(img, position)
        except Exception as e:
            print(f"draw_img Err: {e}")


    def draw_img_edit(self):
        # draw_text(f"icon {icon_w}x{icon_h} | {image_path}",x0, y0 -30, SILVER2)
        # window.fill((255, 255, 255))  # Clear the window content
                
        try:
            #original_width, original_height = self.image_in.get_size()
            #current_width, current_height = original_width * self.resize, original_height * self.resize
            
            #x self.image_out = self.img_to_gray(self.image_in) # image edit
            if self.filt_noise:
                self.image_out = self.img_add_noise(self.image_in, 32)
            if self.filt_onebit:
                self.image_out = self.img_to_onebit(self.image_in)
            if self.filt_reduce:
                self.image_out = self.img_reduce(self.image_in,(0,0,252))
            
            ##self.image_out = self.img_fill(self.image_in,(0,128,0,255))
            
            #self.image_out = p.transform.scale(self.image_out , (current_width, current_height))
            ##self.image_out = self.img_matrix(self.image_in,self.alpha,(32,32),(320,320))    
    
            #self.screen.blit(self.image_in, (630,100))
            self.screen.blit(self.image_out, (390,100))

            #image_nbit = self.image_in.convert(16)
            #self.screen.blit(image_nbit, (700,100))
            #return p.image.tostring(image_8bit, "P") # RGB ok,
    
            ##self.screen.blit(p.transform.scale(image_edit, (current_width, current_height)), (window_width/2+100, y0))
        except Exception as e:
            print(f"draw_img_edit Err: {e}")
    

    def draw_layer_back(self):
        self.screen.fill(BLACK)
        if self.background_image:
            self.screen.blit(self.background_image, (0, 0))
                #p.draw.rect(self.screen, BLACK, (0, 0, self.width, 390))
        opacity_over_bg = self.background_alpha
        rect_surface = p.Surface((self.width, 390), p.SRCALPHA)
        rect_surface.fill((0, 0, 0, opacity_over_bg))  # Set the fill color with opacity
        self.screen.blit(rect_surface, (0, 0))


    def draw_matrix_img(self, new = False):
        if new:
            ri = random.randint(0, len(self.files)-1) # random index
            iname = self.files[ri]
            self.label = iname
            print(ri,len(self.files), iname)
            self.image_input_path = self.images_source+"/"+iname
            
            self.image_in = self.img_load(self.image_input_path)

        self.image_mx = self.img_add_noise(self.image_in, 32)
        self.image_mx = self.img_matrix(self.image_mx,self.alpha,(32,32),(320,320))    
        self.screen.blit(self.image_mx, (35,100))


    def draw_camera(self):
        image_cam = self.camera.get_image()
        if self.filt_matrix:
            image_cam = self.img_matrix(image_cam,size_mx=(32,24),size_out=(320,256))
        if self.filt_noise:
            image_cam = self.img_add_noise(image_cam,20)
        self.screen.blit(image_cam, self.cam_pos)
        #p.display.flip()


    def draw_layer_main(self):
        if self.drawinputfield:
            self.draw_input_field()
        if self.drawinput: 
            #self.draw_img_in(position=self.drawin_pos)
            self.draw_img_in()
        if self.drawcheckbox:
            self.draw_checkbox()
        if self.drawoutput: 
            self.draw_img_out()
        if self.drawedit:
            self.draw_img_edit() 
        if self.drawqr:
            self.draw_qr()
        """
        if self.drawedit:
            self.draw_img_edit() 
            self.draw_img_in()
        """
        if self.drawcam:
            self.draw_camera()

        self.draw_text(self.label,10,20)
        self.draw_text2(self.head,self.width/2,20)
        self.draw_status()
                            

    def run(self,delay=0):
        if delay > 0:
            self.delay = delay
            self.timer = False
        running = True
        while running:
            for event in p.event.get():
                if event.type == p.QUIT:
                    running = False
            
                elif event.type == p.MOUSEMOTION:
                    if self.mouse_button_pressed:
                        # Get the mouse coordinates
                        mouse_x, mouse_y = event.pos

                        # Convert the coordinates to pixel position in the matrix
                        #pixel_x = (mouse_x - x0) // pixel_size 
                        #pixel_y = (mouse_y - y0) // pixel_size
                        self.status = (f"x: {mouse_x}  |  y: {mouse_y}  ")
                
                elif event.type == p.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        # Get the click coordinates
                        self.mouse_button_pressed = True
                        mouse_x, mouse_y = event.pos
                        #self.status = (f"x:{mouse_x}  |  y:{mouse_y}")
                        if self.ch1_pos[0] <= mouse_x <= self.ch1_pos[0] + CHECKSIZE and self.ch1_pos[1] <= mouse_y <= self.ch1_pos[1] + CHECKSIZE:
                            self.checkbox1 = not self.checkbox1
                            #self.filt_matrix = self.checkbox3
                            print("checkbox1",self.checkbox1)
                        if self.ch2_pos[0] <= mouse_x <= self.ch2_pos[0] + CHECKSIZE and self.ch2_pos[1] <= mouse_y <= self.ch2_pos[1] + CHECKSIZE:
                            self.checkbox2 = not self.checkbox2
                            self.filt_noise = self.checkbox2
                            print("checkbox2",self.checkbox2)
                        if self.ch3_pos[0] <= mouse_x <= self.ch3_pos[0] + CHECKSIZE and self.ch3_pos[1] <= mouse_y <= self.ch3_pos[1] + CHECKSIZE:
                            self.checkbox3 = not self.checkbox3
                            print("checkbox3",self.checkbox3)

                    elif event.button == 3:  # Right mouse button
                        # Get the click coordinates
                        mouse_x, mouse_y = event.pos
                        # Convert the coordinates to...

                elif event.type == p.MOUSEBUTTONUP:
                    if event.button == 1:  # Left mouse button
                        mouse_button_pressed = False

                elif event.type == p.KEYDOWN:
                    if event.key == p.K_l and p.key.get_mods() & p.KMOD_CTRL:
                        self.image_in = self.img_load(self.image_input_path)
                        self.draw_edit_img()

                    elif event.key == p.K_s and p.key.get_mods() & p.KMOD_CTRL:
                        #img = draw_edit_img()
                        self.img_save(self.image_out)
                    
                    elif event.key == p.K_n and p.key.get_mods() & p.KMOD_CTRL:
                        self.image_out = self.img_add_noise(self.image_in)

                    elif event.key == p.K_z and p.key.get_mods() & p.KMOD_CTRL:
                        self.resize +=.5
                        if self.resize > 4: 
                            self.resize = 4
                        self.status = (f"zoom {self.resize}x")
                        #draw_edit_img()

                    elif event.key == p.K_c and p.key.get_mods() & p.KMOD_CTRL:
                        self.contrast += 0.5
                        if self.contrast > 6: 
                            self.contrast = 1
                        self.status=f"zoom {str(self.contrast)}"
                        #draw_edit_img()
                    
                    elif event.key == p.K_a and p.key.get_mods() & p.KMOD_CTRL:
                        self.alpha += 32
                        if self.alpha > 255: 
                            self.alpha = 0
                        self.status=f"alpha {str(self.alpha)}"
                    

                    elif event.key == p.K_x and p.key.get_mods() & p.KMOD_CTRL:
                        self.resize -= .5
                        if self.resize == 0: 
                            self.resize = .5
                        self.status = (f"zoom {self.resize}x")
                        #draw_edit_img()
                    
                    elif event.key == p.K_t and p.key.get_mods() & p.KMOD_CTRL:
                        print("test")
                    
                    elif event.key == p.K_q and p.key.get_mods() & p.KMOD_CTRL:
                        print("quit")
                        running = False

                    elif event.key == p.K_RETURN:
                        # after Enter
                        #draw_status(f"input text: {input_text}")
                        if len(self.input_text) > 1:
                            #new_file = f"{path}/{input_text}.png"
                            img_name = self.input_text
                            print(self.input_text)
                            self.status = self.input_text
                            if self.drawqr:
                                self.qrdata = self.input_text

                            self.input_text = ""
                    elif event.key == p.K_BACKSPACE:
                            # del last char
                            self.input_text = self.input_text[:-1]
                    else:
                            # add char
                            self.input_text += event.unicode
                    
            # ========================== main seq, ===================
            self.draw_layer_back()
            self.draw_layer_main()

            self.alpha +=2
            if self.alpha>255:
                self.alpha = 128
                #sleep(1)
                if self.drawmatrix:
                    self.draw_matrix_img(True)
            else:
                if self.drawmatrix:
                    self.draw_matrix_img()
            if self.drawsvg:
                self.svgx +=2
                self.render_svg(self.svgx,32)
                if self.svgx > self.width:
                    self.svgx = 0

            p.display.flip()
            if self. timer:
                self.clock.tick(60)
            else:
                sleep(self.delay)
        #p.quit()
