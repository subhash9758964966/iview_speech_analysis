from model.code.features import feature
from model.code.sentiments import text_sentiment
import time
import os
import json
# def info(title):
    #print(time.time())
    #print(title)
    #print('module name:', __name__)
    #print('parent process:', os.getppid())
    #print('process id:', os.getpid())

def file_result(file, no_chunks, json_file):
    start_time_1 = time.time()
    
    feature_result = feature(file)
    senti_result = text_sentiment(file)
    file_result = {
            
                
            "file" : file,
            "no of chunks" : no_chunks,
            "duration" : feature_result["duration"],
            "Audio_text": senti_result["real text"],
            "total_words" : senti_result["words count"],
            "avg confident" : senti_result["avg confident"],
            "confidece" : senti_result["confident"],
            "polarity" : senti_result["polarity"],
            "sub_score" : senti_result["subjectivity"],
            "time_taken_run":time.time() - start_time_1
                
            
    }

    def write_json(data, filename='./assets/server_json/'+str(json_file)+'.json'): 
            with open(filename,'w') as f: 
                json.dump(data, f, indent=4) 
      
      
    with open('./assets/server_json/'+str(json_file)+'.json') as f: 
                data = json.load(f) 
                temp = data['overall_result'] 
                y = file_result 
                temp.append(y) 
      
    write_json(data)  
    ##print("time",(time.time()))

    # return file_result 



