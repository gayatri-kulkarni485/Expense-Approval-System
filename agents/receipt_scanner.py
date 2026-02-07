import pytesseract
from PIL import Image

class ReceiptScannerAgent:
    def scan(self, image_path: str) -> str:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text