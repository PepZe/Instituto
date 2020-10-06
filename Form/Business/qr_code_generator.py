import pyqrcode
import png
from pyqrcode import QRCode


class qr_code:
    def __init__(self):
        pass

    def create(self, info, file_name):
        url = pyqrcode.create(info)
        url.png(file_name, scale=6)
