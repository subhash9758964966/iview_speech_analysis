from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from textblob import TextBlob
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def text_sentiment(file):
    # 
    apikey = "2Er2VM52mxifdyT1_ONwrivo9ABHqPd_v-mFzAB-ueH3"
    url = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/10975018-ddad-4aee-a868-acfa67bfc1ec"

    authenticator = IAMAuthenticator(apikey)
    stt = SpeechToTextV1(authenticator = authenticator)
    stt.set_service_url(url)

    with open(file, mode="rb")  as wav:
        response = stt.recognize(audio=wav, model='en-GB_NarrowbandModel', content_type='audio/wav', inactivity_timeout=360)
        real_text = []
        confident = []
        for items in response.result["results"]:
            for alternatives in items["alternatives"]:
                #print(alternatives["transcript"])
                real_text.append(alternatives["transcript"])
                confident.append(alternatives["confidence"])
#           for transcript in alternatives["transcript"]:

        real_text = '. '.join(real_text)
    
        word_counts = len(real_text.split())
        
        from nltk.tokenize import word_tokenize
        from nltk.corpus import stopwords
        # stop = stopwords.words('english')
        text = real_text.lower()
        text_tokens = word_tokenize(text)

        text = [word for word in text_tokens if not word in stopwords.words()]


        text = (" ").join(text)
        exclude = set(string.punctuation)
        text = ''.join(ch for ch in text if ch not in exclude)
        #print(text)
        #print("length is ", len(confident))
        avg_confident = sum(confident)/len(confident)
        def senti(x):                         ##function for textblob
            return TextBlob(x).sentiment
        score = senti(text)
        score = str(score)    
        pol_score, sub_score = score.split(",", 1)         
        pol_score = pol_score.replace("Sentiment(polarity=", "")   
        sub_score = sub_score.replace(" subjectivity=", "")
        sub_score = sub_score.replace(")", "")
        result_senti = {
                        "real text": real_text, 
                        "polarity":pol_score, 
                        "subjectivity":sub_score,  
                        "words count":word_counts, 
                        "avg confident":avg_confident, 
                        "confident":confident
                         }
        
        return result_senti

