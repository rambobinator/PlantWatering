# coding: utf8
import qrcode
from PIL import Image, ImageDraw, ImageFont


# Default font
FONT_PATH = "fonts/asimov.otf"

# Made for 300dpi printer:
# that's mean no more than 88 qr in standard A4 paper
STANDARD_A4 = (2400, 3300)
QR_SIZE = 300
_QR_LIMIT = (STANDARD_A4[0] / QR_SIZE, STANDARD_A4[1] / QR_SIZE)


class batch_qrcode:
    """ Class used to batch qrcode"""

    def __init__(self, values = None, base_url = ""):
        self.values = values
        self.base_url = base_url
        self.images = []
        self.qr = qrcode.QRCode(
            version = None,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 5,
            border = 4)
        self.fnt = ImageFont.truetype(FONT_PATH, 16)
        self.qr.make(fit=True)

    def create_images(self):
        if not self.values:
            return
        for id in self.values:
            self.qr.clear()
            self.qr.add_data("{}/{}".format(self.base_url, id))
            img = self.qr.make_image()
            img = img.resize((QR_SIZE, QR_SIZE))
            d = ImageDraw.Draw(img)
            title_value = id.split('-')
            d.text((50, 0), "{}-{}".format( title_value[0][:30],
                                            title_value[1]),
                                            font=self.fnt)
            self.images.append(img)

    def create_sheet(self,  filename = "default",
                            file_extension = ".png",
                            file_type = "PNG",
                            background_color = (255, 255, 255, 255)):
        if not self.values:
            return
        final_images = [Image.new('RGB', STANDARD_A4, background_color)]
        x = 0
        y = 0
        file_id = 0
        for image in self.images:
            final_images[file_id].paste(image, (x * QR_SIZE, y * QR_SIZE))
            x += 1
            if (x >= _QR_LIMIT[0]):
                x = 0
                y += 1
            if y >= _QR_LIMIT[1]:
                x = 0
                y = 0
                file_id += 1
                final_images.append(Image.new('RGB',
                                    STANDARD_A4,
                                    background_color))
        for i, final_img in enumerate(final_images):
            filename_base = "{}{}{}".format(filename, i, file_extension)
            final_img.save(filename_base, file_type)
