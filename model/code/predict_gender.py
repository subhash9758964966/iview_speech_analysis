from model.code.model_str import gender_model
import numpy as np
def prediction_gender(features):

    h5_model_file = "./model/weight/gender_model.h5"
    model = gender_model()
    model.load_weights(h5_model_file)
    

    # gender_preds = model.predict(features)
    # gender_preds = model.predict(features)
    gender_preds= np.argmax(model.predict(features))
    
    return gender_preds
