import os
import cv2
import numpy as np
from sklearn.mixture import GaussianMixture
from tensorflow import keras

def extract_features(frames):
    features = []

    # Calculate optical flow for consecutive frames
    for i in range(len(frames) - 1):
        frame1 = frames[i]
        frame2 = frames[i + 1]

        # Calculate optical flow
        flow = cv2.calcOpticalFlowFarneback(frame1, frame2, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        # Flatten the flow matrix and append it to the features
        flow_flat = flow.reshape(-1)
        features.append(flow_flat)

    return features


def main():
    # Load the saved MDT model
    mdt_model = keras.models.load_model('model.h5')

    # Specify the directory path containing the frames to predict
    frames_directory = 'D:/Data Set/Crowd Anomaly Detection/UCSD_Anomaly_Dataset/UCSDped1/Test/Test001'

    # Initialize an empty list to store the frames
    frames = []

    # Iterate over the files in the directory
    for filename in os.listdir(frames_directory):
        file_path = os.path.join(frames_directory, filename)

        # Check if the file is an image
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Read the frame using OpenCV
            frame = cv2.imread(file_path)

            # Preprocess the frame if needed

            # Append the frame to the list
            frames.append(frame)

    # Convert frames to numpy array
    frames = np.array(frames)

    # Extract features from the frames
    features = extract_features(frames)

    # Convert features to numpy array
    features = np.array(features)

    # Reshape features for prediction
    num_samples, num_frames, num_features = features.shape
    features_reshaped = features.reshape(num_samples * num_frames, num_features)

    # Predict using the MDT model
    predictions = mdt_model.predict(features_reshaped)

if __name__ == '__main__':
    main()
