import boto3
import pandas as pd
import os

s3 = boto3.resource('s3',
                    aws_access_key_id="AKIAID4RJ55NEY2ZLHTQ",
                    aws_secret_access_key="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"
                    )
folder = '/home/fatema/Pictures/IMAGES/2018-11-13/'




def detect_faces(bucket, key, attributes=['ALL'], region="us-east-2"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.detect_faces(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key,

            }
        },
        Attributes=attributes,
    )
    return response['FaceDetails']


for filename in os.listdir(folder):
    BUCKET = "emotion-classify"
    KEY = "2018-11-13/" + filename
    #print(KEY)
    for face in detect_faces(BUCKET, KEY):
    # emotions
        score = []
        mood = []
        for emotion in face['Emotions']:
            score.append(emotion['Confidence'])
            mood.append(emotion['Type'])
        emotiondf = pd.DataFrame({'Emotions':mood,'Confidence Score':score})
        emotiondf.to_csv('/home/fatema/Desktop/Emotion/2018-11-13/'+ \
               os.path.splitext(filename)[0] +'.csv',\
                     columns=['Emotions','Confidence Score'],header=True,\
                     index=False)
        print(emotiondf)



