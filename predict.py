# import cv2
# import numpy as np

# # Load the trained model
# model = keras.models.load_model('trained_model.h5')

# # Load and preprocess a new image
# new_image = cv2.imread('new_image.jpg')
# new_image = cv2.resize(new_image, (224, 224))
# new_image = new_image / 255.0  # Normalize pixel values

# # Make a prediction
# predictions = model.predict(np.expand_dims(new_image, axis=0))

# # Get the predicted class
# predicted_class = np.argmax(predictions)

# # You can use the predicted_class to identify the object in the image based on your class labels.




import cv2
import numpy as np
from tensorflow import keras

# Load the trained model
model = keras.models.load_model('trained_model.h5')

# Define a function to capture and process new images
def capture_and_predict():
    # Open the webcam (you can change the camera index if needed)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        # Preprocess the captured frame
        if ret:
            # Resize and normalize the image
            image = cv2.resize(frame, (224, 224)) / 255.0

            # Make a prediction using the trained model
            predictions = model.predict(np.expand_dims(image, axis=0))

            # Get the predicted class label
            predicted_class = np.argmax(predictions)

            # Display the predicted class label on the frame
            class_name = str(predicted_class)  # Replace with your class labels
            cv2.putText(frame, class_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Display the frame with the prediction
            cv2.imshow('Prediction', frame)

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function to start capturing and predicting
capture_and_predict()
