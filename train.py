import os
import cv2
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# Define the path to your training data
train_data_dir = 'Datasets/Train/'

# Load and preprocess the training data
def load_and_preprocess_data(data_dir):
    image_data = []
    labels = []
    class_names = sorted(os.listdir(data_dir))
    num_classes = len(class_names)

    for class_index, class_name in enumerate(class_names):
        class_dir = os.path.join(data_dir, class_name)
        for image_filename in os.listdir(class_dir):
            image_path = os.path.join(class_dir, image_filename)
            image = cv2.imread(image_path)
            image = cv2.resize(image, (224, 224))
            image = image / 255.0  # Normalize pixel values
            image_data.append(image)
            labels.append(class_index)

    return np.array(image_data), np.array(labels), num_classes

train_data, train_labels, num_classes = load_and_preprocess_data(train_data_dir)

# Create a neural network model
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
num_epochs = 10  
batch_size = 32 
# Train the model (you should also split the data into training and validation sets)
model.fit(train_data, train_labels, epochs=num_epochs, batch_size=batch_size)

# Save the trained model
model.save('trained_model.h5')
