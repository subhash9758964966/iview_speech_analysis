import io
from pydub import AudioSegment
import sys
from model.code.chunks import chunk
from model.code.chunks_results import preprocess_chunk_audio
import json
import time
import glob
import os
import json
import librosa


def index(val1, json_file, dir_of_interest):
        print("val1 is ")
        sound = AudioSegment.from_mp3(file = val1)
        sound.export("test.wav", format="wav")
        path_data = "./model/output/"+ json_file
        X,sr = librosa.load("test.wav")
        print("LENGTH OF THE AUDIO IS", len(X)/sr)
        len_audio = len(X)/sr
        if not os.path.exists(path_data):
            os.makedirs(path_data)
        no_of_chunks = chunk("test.wav", path_data)
        print("Chunks is created")

        # start_time = time.time()
        preprocess_chunk_audio("test.wav", no_of_chunks, json_file, dir_of_interest)
        # overall_result_run_time = (time.time() - start_time)
        # result[0]["total_result_run_time"] = overall_result_run_time

        # chunk_time = []
        # for chunk_num in result[0]["chunks"]:
        #     chunk_time.append(chunk_num["time_to_run_code"])

        # result[0]["chunks_time_list"] = chunk_time
        # result[0]["sum_from_chunks_time_list"] = sum(result[0]["chunks_time_list"])


        all_files_chunks = os.listdir(path_data)
        for file_chunks in all_files_chunks:
            os.remove(path_data+"/"+file_chunks)
        os.rmdir(path_data)
        os.remove("test.wav")
        return no_of_chunks, len_audio 
    
    
def result_fun(val1):
            print("YES")
            # val1 = str(sys.argv[1])
            start_time = time.time()

            chunks_dict = {
                # "overall_result":[],
                "chunks":[]
            }

            import hashlib
            # json_file_name = hashlib.md5(b(val1+str(time.time()).encode('utf-8')))
            file_name = val1+str(time.time())
            json_file_name = hashlib.sha256(str(file_name).encode('utf-8')).hexdigest()
            FILE_DIR = os.path.dirname(os.path.abspath(__file__))
            # absolute path to this file's root directory
            PARENT_DIR = os.path.join(FILE_DIR, os.pardir) 
            print("File Directory is ", FILE_DIR)
            print("Parent directory is ", PARENT_DIR)
            dir_of_interest = os.path.join(PARENT_DIR, 'assets/')
           
            print("Parent directory is ", PARENT_DIR)
            print("dir_of_interest is ", dir_of_interest)
            #print("json_file_name", json_file_name)
            with open(str(dir_of_interest)+json_file_name+ '.json', 'w') as fp:
                json.dump(chunks_dict, fp)
            print("Subhash 1 Yes")

            no_chunks, len_audio = index(val1, json_file_name, dir_of_interest)

            with open(str(dir_of_interest)+str(json_file_name)+'.json') as f: 
                    data = json.load(f) 


            os.remove(str(dir_of_interest)+str(json_file_name)+'.json')
            # os.remove(val1)
            response={
                "response":200,
                "message":"data from the modal",
                "Audio length " :  len_audio,
                "total chunks" : no_chunks,
                "Data":data,
                "time":(time.time() - start_time)
            }
            print(json.dumps(response))
            
            return response
  
# val1 = str(sys.argv[1])       
# result_wwe  = result_fun(val1)# val1 = str(sys.argv[1]) 
# print(val1)