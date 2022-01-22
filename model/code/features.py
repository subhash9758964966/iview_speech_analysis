import librosa
import numpy as np
def feature(files):
    X,sr = librosa.load(files)
    stft = np.abs(librosa.stft(X))
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sr, n_mfcc=40).T,axis=0)
    chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sr).T,axis=0)
    mel = np.mean(librosa.feature.melspectrogram(X, sr=sr).T,axis=0)
    contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sr).T,axis=0)
    tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X),sr=sr).T,axis=0)
    features = np.hstack([mfccs,chroma,mel,contrast,tonnetz])
    features = features.reshape(1,193)
    duration = len(X)/sr
    feature_result = {
        "feature" : features,
        "duration" : duration
    }
    

    return feature_result
