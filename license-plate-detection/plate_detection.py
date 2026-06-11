import cv2
import pytesseract
import matplotlib.pyplot as plt

# Jalur Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def detect_plate_number(image_path):

    # Muat gambar
    image = cv2.imread(image_path)

    if image is None:
        print("Gambar tidak ditemukan!")
        return

    # Konversi ke grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Canny Edge Detection
    edges = cv2.Canny(blurred, 100, 200)

    # Cari kontur
    contours, _ = cv2.findContours(
        edges.copy(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Urutkan berdasarkan luas
    contours = sorted(
        contours,
        key=cv2.contourArea,
        reverse=True
    )

    plate_contour = None

    for contour in contours:

        epsilon = 0.02 * cv2.arcLength(contour, True)

        approx = cv2.approxPolyDP(
            contour,
            epsilon,
            True
        )

        # Cari objek dengan 4 titik sudut
        if len(approx) == 4:
            plate_contour = approx
            break

    if plate_contour is not None:

        # Kotak hijau pada plat
        cv2.drawContours(
            image,
            [plate_contour],
            -1,
            (0, 255, 0),
            3
        )

        # Ambil area plat
        x, y, w, h = cv2.boundingRect(plate_contour)

        plate_image = gray[y:y+h, x:x+w]

        # Threshold
        _, thresh = cv2.threshold(
            plate_image,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        # OCR
        plate_number = pytesseract.image_to_string(
            thresh,
            config='--psm 8'
        )

        # Tampilkan gambar dengan kotak hijau
        plt.figure(figsize=(10, 6))
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title("Detected License Plate")
        plt.axis("off")
        plt.show()

        return plate_number.strip()

    else:
        plt.figure(figsize=(10, 6))
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title("License Plate Not Detected")
        plt.axis("off")
        plt.show()

        return "License plate not detected"


# Jalur gambar
image_path = "car.jpg"

# Jalankan deteksi
plate_number = detect_plate_number(image_path)

print("Detected Plate Number:", plate_number)