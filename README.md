# Speech Emotion Recognition - Machine Learning Path
Bangkit 2023 Product-based Capstone

Team ID: C23-PS163
(ML) M169DKY4215 – Ade Puspaning Ayu Umbaran Putri – Universitas Gadjah Mada
(ML) M040DSX1471 – Dimas Wahyu Saputro – Institut Teknologi Sumatera
(ML) M353DSY3615 – Nur Ulfah Atiqah – Universitas Syiah Kuala

# Data Engineering
## Dataset Used
Dataset yang digunakan pada project ini adalah,
1. RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song): This dataset contains audio and visual recordings of individuals expressing emotional speech and singing. During the analysis, we observed that some sound samples required multiple plays to confirm the intended emotion, such as the "happy" sound.
2. TESS (Toronto emotional speech set): This dataset consists of audio recordings of emotional speech. It was noticed that some data points had high amplitude, similar to what was observed in the RAVDESS dataset. Data normalization will be performed later to address this issue.
3. CREMA-D (Crowd-sourced Emotional Multimodal Actors Dataset): This dataset includes crowd-sourced audio recordings of individuals expressing various emotions. It was observed that the quality of the recordings in this dataset varied significantly. Some recordings were clear and crisp, while others were muffled or echoed. Additionally, there were instances of significant silence in the recordings.
4. SAVEE (Surrey Audio-Visual Expressed Emotion): This dataset consists of high-quality audio recordings where individuals express different emotions. The waveform of the audio samples in this dataset is distinctly different for each emotion, which is beneficial for our model. It was also noticed that there is a very short silence period between the start and end of the recordings, which could potentially be trimmed to enhance the audio quality.
From our analysis, there are some strengths and weaknesses in each dataset. From our analysis, there are some strengths and weaknesses in each dataset. 

## Join Dataset
These datasets contain different types of emotions. When combined, the resulting dataset includes the following emotions:
1. female_angry       1096
2. female_happy       1096
3. female_fear        1096
4. female_sad         1096
5. female_disgust     1096
6. female_neutral     1056
7. female_surprise     496
8. male_angry          827
9. male_happy          827
10. male_fear           827
11. male_sad            827
12. male_disgust        827
13. male_neutral        839
14. male_surprise       156

## Data Augmentation
Data augmentation is performed to address the issue of imbalanced data. The following data augmentation techniques are applied:
1. Noise Injection
2. Shifting
3. Stretching
4. Pitching

## Feature Extraction
Feature extraction is conducted to transform the data into a simplified form that can be easily understood by the machine. The following feature extraction techniques are employed:
1. Zero Crossing Rate (ZCR): It measures the rate at which the audio signal changes its sign, which provides information about the frequency content and noisiness of the signal.
2. Chroma feature based on Short-Time Fourier Transform (Chroma_stft): It represents the 12 different pitch classes in the audio signal and provides information about the harmonic content and tonal characteristics.
3. Mel-frequency Cepstral Coefficients (MFCC): These coefficients capture the spectral shape of the audio signal by converting the power spectrum of the signal into a perceptually meaningful representation. They are commonly used in speech and music recognition tasks.
4. Root Mean Square (RMS) Value: It represents the average energy of the audio signal and provides information about the overall loudness.
5. Mel Spectrogram: It represents the power spectral density of the audio signal in mel-scale, which emphasizes frequencies important for human perception. It provides information about the spectral content of the audio.

# Machine Learning Model
1. LSTM (Long Short-Term Memory)
2. Conv1D-LSTM (Convolutional 1D Long Short-Term Memory)

# Model Architecture
add image files

# Model Deployment
We deploy the model using FastAPI by creating a python code that will load the required files and Keras h5 model. The code will also create a FastAPI instance and create a POST method that will receive the audio file and Get method return the prediction result and confidence.