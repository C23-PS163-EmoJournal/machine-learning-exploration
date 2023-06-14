# Speech Emotion Recognition - Machine Learning Path
Bangkit 2023 Product-based Capstone

Team ID: C23-PS163
(ML) M169DKY4215 – Ade Puspaning Ayu Umbaran Putri – Universitas Gadjah Mada
(ML) M040DSX1471 – Dimas Wahyu Saputro – Institut Teknologi Sumatera
(ML) M353DSY3615 – Nur Ulfah Atiqah – Universitas Syiah Kuala

# Data Engineering
## Dataset yang digunakan
Dataset yang digunakan pada project ini adalah,
1. RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song)
We had to play it 3 or 4 times to finally be convienced that it is indeed a happy sound. 
2. TESS (Toronto emotional speech set)
Notice the amplitute is pretty high too on a few data points? We saw that on the RAVDESS dataset too. We will have to normalize the data later.
3. CREMA-D (Crowd-sourced Emotional Multimodal Actors Dataset)
I noticed with this CREMA-D dataset is that its is highly varied in its quality. Some are crisp clear and some are really muffled or echoey. Also there's lots of silence as well.
4. SAVEE (Surrey Audio-Visual Expressed Emotion)
Good quality audio. We can see that the wave form is distinctively different from the fear one. So that's good for our model. I did notice that there's a very short silence period between start and end. We could potentially trim it later to enhance the quality.
From our analysis, there are some strengths and weaknesses in each dataset. From our analysis, there are some strengths and weaknesses in each dataset. 

## Join Dataset
Keempat dataset di atas memiliki banyak jenis emosi yang berbeda-beda, sehingga ketika ingin digunakan dan digabungkan, harus dilakukan preprocessing terlebih dahulu. Ketika dibuat menjadi satu dataset, maka akan terdapat emosi di bawah ini,
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
Data augmentation dilakukan untuk mengatasi masalah ketidakseimbangan data. Data augmentation yang dilakukan adalah,
1. Noise Injection
2. Shifting
3. Stretching
4. Pitching

## Feature Extraction
Feature extraction dilakukan untuk mengubah data menjadi bentuk yang lebih sederhana dan mudah dipahami oleh mesin. Feature extraction yang dilakukan adalah,
1. Zero Crossing Rate (ZCR): It measures the rate at which the audio signal changes its sign, which provides information about the frequency content and noisiness of the signal.
2. Chroma feature based on Short-Time Fourier Transform (Chroma_stft): It represents the 12 different pitch classes in the audio signal and provides information about the harmonic content and tonal characteristics.
3. Mel-frequency Cepstral Coefficients (MFCC): These coefficients capture the spectral shape of the audio signal by converting the power spectrum of the signal into a perceptually meaningful representation. They are commonly used in speech and music recognition tasks.
4. Root Mean Square (RMS) Value: It represents the average energy of the audio signal and provides information about the overall loudness.
5. Mel Spectrogram: It represents the power spectral density of the audio signal in mel-scale, which emphasizes frequencies important for human perception. It provides information about the spectral content of the audio.

# Machine Learning Model
1. LSTM
2. Conv1D-LSTM

# Model Architecture
add image files

# Model Deployment
We deploy the model using FastAPI by creating a python code that will load the required files and Keras h5 model. The code will also create a FastAPI instance and create a POST method that will receive the audio file and Get method return the prediction result and confidence.