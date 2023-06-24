
"""
...
"""

class External_pgt:
    def __init__(self, pygame_instance):
        self.pygame_instance = pygame_instance

    def process_image_x(self, image_path):
        image = self.pygame_instance.load_image(image_path)
        processed_image = self.pygame_instance.img_matrix(image)
        return processed_image

    def convert_to_gray_x(self, image_path):
        image = self.pygame_instance.load_image(image_path)
        gray_image = self.pygame_instance.img_to_gray(image)
        return gray_image

    def external_test(self):
        print("external_test")
    # Další metody externí knihovny
