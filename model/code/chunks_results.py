import os
from model.code.features import feature
from model.code.predict_emotion import prediction_emotion
from model.code.predict_gender import prediction_gender
from model.code.sentiments import text_sentiment
import time
import json
import datetime
import glob
# def info(title):
#     print(time.time())
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
# def preprocess_chunk_audio(voice_file):

def preprocess_chunk_audio(file, no_chunks, json_file):
    # info("Hi")
    result = {"1":"Neutral", "2": "calm", "3":"happy", "4":"sad", "5":"angry", "6":"fearful", "7":"disgust", "8":"surprise"}
    result_gender = {"0": "Female", "1":"Male"}
    path_data = "model/output/"
    directories = os.listdir(path_data)
    directories = os.listdir("model/output/"+str(directories[0]))
    print("directries is :", directories)
   
    # for files in voice_file:
    # chunk_list_result = []
    print("my_list is ", directories)
    
    for files in directories:
        start_time = time.time()
        feature_result = feature("./model/output/"+json_file+'/'+files)

        y_preds_index = prediction_emotion(feature_result["feature"])
        gender_preds = prediction_gender(feature_result["feature"])
        print("gender is      ", gender_preds)
        senti_result = text_sentiment("./model/output/"+json_file+'/'+files)

        res_dic = {
            
            "file" : files,
            "duration" : feature_result["duration"],
            "gender": result_gender[str(gender_preds)],
            "emotion" : result[str(y_preds_index+1)],
            "Audio_text": senti_result["real text"],
            "total_words" : senti_result["words count"],
            "avg confident" : senti_result["avg confident"],
            "confidece" : senti_result["confident"],
            "polarity" : senti_result["polarity"],
            "sub_score" : senti_result["subjectivity"],
             "time_to_run_code":(time.time() - start_time)
            
        }
        print("dict is ", dict)

        # with open('file_result.txt', 'a') as outfile:
        #      outfile.write(json.dumps(res_dic))
        #      outfile.write(",")
        #      outfile.close()
        


        def write_json(data, filename='./assets/server_json/'+str(json_file)+'.json'): 
            with open(filename,'w') as f: 
                json.dump(data, f, indent=4) 
      
      
        with open('./assets/server_json/'+str(json_file)+'.json') as f: 
                data = json.load(f) 
                temp = data['chunks'] 
                y = res_dic 
                temp.append(y) 
                # print("Y  :", y)
      
        write_json(data)  



        
    #     chunk_list_result.append(res_dic)  
    
    # #print(chunk_list_result)
    #print("................................",time.time(),".......................................")    
    # return chunk_list_result
    # Process_Queue.put(chunk_list_result)
       

