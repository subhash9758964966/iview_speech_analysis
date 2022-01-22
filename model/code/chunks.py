from pydub import AudioSegment
from pydub.silence import split_on_silence
def split(filepath):
        sound = AudioSegment.from_file(filepath)
        dBFS = sound.dBFS
        chunks = split_on_silence(sound,
                    min_silence_len=1500,
                    silence_thresh=dBFS-16)
        return chunks

def chunk(file, dir):
    print("Thia ia Subhash")
    chunks = split(file)
    target_length = 3*1000
    output_chunks = []
    for chunk in chunks:       
            if len(chunk) < target_length:
                   continue
            else:
                output_chunks.append(chunk)
            
    for i, sound in enumerate(output_chunks):
        path = dir + '/chunks'+str(i)
        sound.export(out_f=path,format="wav")
    
   
    return len(output_chunks)