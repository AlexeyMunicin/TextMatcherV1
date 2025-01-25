import pytesseract
import cv2

class TextMatcher:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract\tesseract.exe'

    def preprocess_image(self, image_path):
        # Чтение изображения
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError("Image not found")
        
        # Преобразование в оттенки серого
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Применяем пороговую бинаризацию (Otsu) для выделения текста
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        
        # Удаление шума с помощью медианного размытия
        denoised = cv2.medianBlur(binary, 3)
        
        # Применяем Гауссово размытие для дополнительного удаления шума
        blurred = cv2.GaussianBlur(denoised, (5, 5), 0)
        
        return blurred

    def extract_text(self, image_path, lang="eng+rus"):
        # Предобработка изображения
        preprocess_image = self.preprocess_image(image_path)

        # Конфигурация Tesseract
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(preprocess_image, lang=lang, config=custom_config)
        return text
