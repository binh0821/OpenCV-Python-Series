import cv2

# Define output file and video parameters
output_filename = 'output_video.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for AVI (e.g., 'XVID', 'MJPG')
fps = 20.0
frame_size = (640, 480) # Adjust to your desired resolution

# Initialize video capture (e.g., from webcam)
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Get actual frame dimensions from the camera if needed
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# frame_size = (width, height)

# Initialize video writer
out = cv2.VideoWriter(output_filename, fourcc, fps, frame_size)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Optional: Display the frame
    cv2.imshow('Recording', frame)

    # Write the frame to the output video file
    out.write(frame)

    # Press 'q' to quit recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()