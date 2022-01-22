from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, Conv1D, MaxPooling1D, AveragePooling1D, BatchNormalization, Input, Flatten, Dropout, Activation

def emotion_model():
    model = Sequential()

    model.add(Dense(193,input_dim =193,kernel_initializer='normal',activation ='relu'))

    model.add(Dense(400,kernel_initializer='normal',activation ='relu'))

    model.add(Dropout(0.2))

    model.add(Dense(200,kernel_initializer='normal',activation ='relu'))

    model.add(Dropout(0.2))

    model.add(Dense(100,kernel_initializer='normal',activation ='relu'))

    model.add(Dropout(0.2))

    model.add(Dense(8,kernel_initializer='normal',activation ='softmax'))
    
    return model

def gender_model():
    model_gender = Sequential()

    model_gender.add(Dense(193, input_shape=(193,), activation = 'relu'))
    model_gender.add(Dropout(0.1))

    model_gender.add(Dense(128, activation = 'relu'))
    model_gender.add(Dropout(0.25))  

    model_gender.add(Dense(128, activation = 'relu'))
    model_gender.add(Dropout(0.5))    

    model_gender.add(Dense(2, activation = 'softmax'))
   
    return model_gender





