import cv2
from Face import Face
from Message import Message
from time import sleep

cap = cv2.VideoCapture(0) 

text_position = (10, 30)
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 1
colour = (255, 255, 255)

face = Face("faces")
message = Message()

while(True):
    ret, frame = cap.read()
    name = face.get_name(frame, source_type="video")
    
    if name:
        cv2.putText(frame, name, text_position, font, scale, colour)
        message.update(name)
        
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
    sleep(1)

cap.release()
cv2.destroyAllWindows()
