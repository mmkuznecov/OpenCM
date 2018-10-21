import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
#out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))

while cap.isOpened():
	ret, frame = cap.read()
 	if ret:
        	out.write(frame)
        	if cv2.waitKey(1) and 0xFF == ord('q'):
        		break
	else:
        	break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
