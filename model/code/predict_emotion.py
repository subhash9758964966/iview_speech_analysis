from model.code.model_str import emotion_model
import numpy as np
def prediction_emotion(features):

    h5_model_file = "./model/weight/mlp_relu_adadelta_model.h5"
    model = emotion_model()
    model.load_weights(h5_model_file)
    

    y_preds_index = np.argmax(model.predict(features))
   
    return y_preds_index
