import cv2
import os
import face_recognition
from datetime import datetime

class FaceCaptureApp:
    def __init__(self):
        # Initialize webcam
        self.camera = cv2.VideoCapture(0)

        # Create a directory to store captured faces
        self.output_directory = "captured_faces"
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

        # Initialize a set to keep track of captured face filenames
        self.captured_faces_set = set(os.listdir(self.output_directory))

    def capture_faces(self):
        ret, frame = self.camera.read()

        # Convert the frame to RGB format (required for face_recognition)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces in the frame
        face_locations = face_recognition.face_locations(rgb_frame)

        for face_location in face_locations:
            top, right, bottom, left = face_location

            # Crop and save the detected face
            face_image = frame[top:bottom, left:right]
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            face_filename = f"captured_face_{timestamp}.jpg"

            # Check if the face is already captured
            if face_filename not in self.captured_faces_set:
                self.captured_faces_set.add(face_filename)
                face_filepath = os.path.join(self.output_directory, face_filename)
                cv2.imwrite(face_filepath, face_image)
                print(f"Face saved as {face_filepath}")
            else:
                print(f"Face {face_filename} already captured")

    def run(self):
        while True:
            # Capture a frame from the webcam
            ret, frame = self.camera.read()

            # Display the captured frame
            cv2.imshow('Face Capture App', frame)

            # Capture faces when detected
            self.capture_faces()

            key = cv2.waitKey(1)

            # Exit the loop when 'q' is pressed
            if key & 0xFF == ord('q'):
                break

    def cleanup(self):
        self.camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = FaceCaptureApp()
    try:
        app.run()
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        pass
    finally:
        app.cleanup()
