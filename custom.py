import cv2
import time
import os

capture_folder = 'box_dataset'
try:
    os.makedirs(capture_folder, exist_ok=True)
except OSError as e:
    raise Exception(f"Failed to create directory '{capture_folder}': {e}")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise Exception("Could not open video device")
delay_seconds = 4
image_count = 0

def capture_frame(cap, capture_folder, image_count):
    ret, frame = cap.read()
    if not ret:
        return False, image_count
    image_path = os.path.join(capture_folder, f"box_{image_count:04}.jpg")
    cv2.imwrite(image_path, frame)
    print(f"Captured: {image_path}")
    return True, image_count + 1

def main_loop(cap, capture_folder, delay_seconds):
    image_count = 305
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Press 's' to capture, 'q' to quit", frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            success, image_count = capture_frame(cap, capture_folder, image_count)
            if not success:
                break
            time.sleep(delay_seconds)  # Add delay after capturing the image
        elif key == ord('q'):
            break

try:
    main_loop(cap, capture_folder, delay_seconds)
finally:
    cap.release()
    cv2.destroyAllWindows()