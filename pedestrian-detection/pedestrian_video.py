import cv2
import imutils

# Menginisialisasi HOG People Detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(
    cv2.HOGDescriptor_getDefaultPeopleDetector()
)

# Membaca video
cap = cv2.VideoCapture('vid.mp4')

while cap.isOpened():

    # Membaca frame video
    ret, image = cap.read()

    if ret:

        # Resize frame
        image = imutils.resize(
            image,
            width=min(400, image.shape[1])
        )

        # Deteksi pejalan kaki
        (regions, _) = hog.detectMultiScale(
            image,
            winStride=(4, 4),
            padding=(4, 4),
            scale=1.05
        )

        # Gambar kotak merah
        for (x, y, w, h) in regions:
            cv2.rectangle(
                image,
                (x, y),
                (x + w, y + h),
                (0, 0, 255),
                2
            )

        # Tampilkan hasil
        cv2.imshow("Video Pedestrian Detection", image)

        # Tekan Q untuk keluar
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()