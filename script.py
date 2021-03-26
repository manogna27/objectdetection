import numpy as np
import cv2

if __name__ == '__main__':

	#opens camera
    camera = cv2.VideoCapture(0)
    while True:
        _, img = camera.read()

        height, width = img.shape[:2]

        cv2.imshow('Object Detection', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    camera.release()
    cv2.destroyAllWindows()
