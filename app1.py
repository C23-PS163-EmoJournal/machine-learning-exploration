from flask import Flask, jsonify, make_response, request

import tensorflow as tf
from tensorflow.keras.models import model_from_json
from tensorflow.keras import Sequential
import numpy as np
import librosa
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import joblib

app = Flask(__name__)

json_file = open('/Users/dimasws/Downloads/cnnlstmmodel001.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new modela
loaded_model.load_weights("/Users/dimasws/Downloads/cnnlstmmodel001.h5")
# print("Loaded model from disk")

#loading our scaler
scaler = joblib.load('/Users/dimasws/Downloads/scaler.joblib')

#loading our encoder
encoder= joblib.load('/Users/dimasws/Downloads/encoder.joblib')
# print('load scaler encoder done')

def extract_features(data, sample_rate):
    # ZCR
    result = np.array([])
    zcr = np.mean(librosa.feature.zero_crossing_rate(y=data).T, axis=0)
    result=np.hstack((result, zcr)) # stacking horizontally

    # Chroma_stft
    stft = np.abs(librosa.stft(data))
    chroma_stft = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
    result = np.hstack((result, chroma_stft)) # stacking horizontally

    # MFCC
    mfcc = np.mean(librosa.feature.mfcc(y=data, sr=sample_rate).T, axis=0)
    result = np.hstack((result, mfcc)) # stacking horizontally

    # Root Mean Square Value
    rms = np.mean(librosa.feature.rms(y=data).T, axis=0)
    result = np.hstack((result, rms)) # stacking horizontally

    # MelSpectogram
    mel = np.mean(librosa.feature.melspectrogram(y=data, sr=sample_rate).T, axis=0)
    result = np.hstack((result, mel)) # stacking horizontally
    
    return result

def get_predict_feat(path):
    d, sample_rate= librosa.load(path, offset=0.6)
    res=extract_features(d, sample_rate)
    result=np.array(res)
    result=np.reshape(result,newshape=(1,162))
    i_result = scaler.transform(result)
    final_result=np.expand_dims(i_result, axis=2)

    return final_result

def prediction(path1):
    res=get_predict_feat(path1)
    predictions=loaded_model.predict(res)
    y_pred = encoder.inverse_transform(predictions)
    return y_pred[0][0], predictions.max()
    # print(predictions.max())
    # print(y_pred[0][0])    

@app.route("/api/audio", methods=['GET', 'POST'])
def predict():
    emotion, confidence = prediction(request.files['file'])
    
    message = jsonify({
        "message": "Predict success",
        "Emotion": emotion,
        "Confidence": str(confidence)
    })
    return make_response(message, 200)


@app.route("/")
def welcome():
    return "Welcome to Emotion Recognition API"

if __name__ == "__main__":
    app.run(debug=True, port=6767)