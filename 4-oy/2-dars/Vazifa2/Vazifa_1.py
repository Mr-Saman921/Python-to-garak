from PIL import Image, ImageFilter
import os
class ImageChanger:
    def __init__(self, filename):
        self.filename = filename
        self.image = Image.open(filename)

    def save_image(self, output_filename):
        self.image.save(output_filename)

    def resize(self, size):
        self.image = self.image.resize(size)
        self.save_image(f'resized_{self.filename}')

    def crop(self, size):
        self.image = self.image.crop((0, 0, size[0], size[1]))
        self.save_image(f'cropped_{self.filename}')

    def blur(self, radius=2):
        self.image = self.image.filter(ImageFilter.GaussianBlur(radius))
        self.save_image(f'blurred_{self.filename}')

    def black(self):
        self.image = self.image.convert('L')
        self.save_image(f'black_{self.filename}')

    def passport_formatter(self):
        self.image = self.image.resize((3, 4))
        self.save_image(f'passport_{self.filename}')

    @staticmethod
    def merge_images(image1, image2, output_filename):
        img1 = Image.open(image1)
        img2 = Image.open(image2)
        (width1, height1) = img1.size
        (width2, height2) = img2.size
        result_width = width1 + width2
        result_height = max(height1, height2)
        result = Image.new('RGB', (result_width, result_height))
        result.paste(im=img1, box=(0, 0))
        result.paste(im=img2, box=(width1, 0))
        result.save(output_filename)

file_path = r"/4-oy/2-dars/picture.jpg"
if os.path.isfile(file_path):
    img_changer = ImageChanger("picture.jpg")
    img_changer.resize((800, 600))
    img_changer.crop((400, 400))
    img_changer.blur(5)
    img_changer.passport_formatter()
    img_changer.black()
    img_changer.merge_images("picture.jpg", "resized_picture.jpg", "merged_picture.jpg")
else:
    print(f"The file does not exist at {file_path}")
