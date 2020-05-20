import cv2
from gpiozero import LED

image = "face.png"
#image = "dog.png"
cascade_file = "haarcascade_frontalface_default.xml"
alarm = LED(4)
cascade = cv2.CascadeClassifier(cascade_file)
image = cv2.imread(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face = cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

if len(face):
    print("Found a face!")
    alarm.blink()
    for (x, y, w, h) in face:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Face found", image)
else:
    cv2.imshow("Found this", image)
    
cv2.waitKey(0)
cv2.destroyAllWindows()
alarm.off()