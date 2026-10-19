from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("best.pt")
results = model.predict(source="0", show=True)

# from ultralytics import YOLO
# import cv2

# # 1. Load the trained YOLOv11 facial emotion model
# model = YOLO("best.pt")

# # 2. Loop through multiple camera indices to find your active webcam
# cap = None
# for index in [0, 1, 2, -1]:
#     print(f"Attempting to open camera index: {index}...")
#     # Using CAP_DSHOW on Windows handles hardware locking issues much better
#     cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
#     if cap.isOpened():
#         print(f"Successfully connected to camera index: {index}!")
#         break
#     cap.release()

# if cap is None or not cap.isOpened():
#     print("\nError: Could not open any webcam index.")
#     print("Please check Windows Privacy Settings -> Camera -> Allow desktop apps to access your camera.")
#     exit()

# print("Starting live emotion detection... Press 'q' to quit.")

# # 3. Stream frames manually
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Failed to grab frame.")
#         break

#     # Run inference on the current frame
#     results = model.predict(source=frame, conf=0.5, stream=True)

#     # Plot the bounding boxes and emotion labels onto the frame
#     annotated_frame = frame
#     for result in results:
#         annotated_frame = result.plot()

#     # Display the live window
#     cv2.imshow("Facial Emotion Detection (YOLOv11)", annotated_frame)

#     # Break the loop if the user presses the 'q' key
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # 4. Clean up resources
# cap.release()
# cv2.destroyAllWindows()
