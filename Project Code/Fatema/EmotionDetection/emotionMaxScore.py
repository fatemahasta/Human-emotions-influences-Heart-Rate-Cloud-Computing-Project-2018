import boto3
import pandas as pd
import os

basePath = '/home/fatema/Desktop/Emotion/'
folder = '2018-11-13'
fullPath = basePath+folder+'/'

maxRows = []
fileNames = []

columns = ['Time','Emotion','Confidence Score']
final_df = pd.DataFrame(columns=columns)

for filename in os.listdir(fullPath):
  dataFrame = pd.read_csv(fullPath+filename)

  maxConfidenceRow = dataFrame.loc[dataFrame['Confidence Score'].idxmax()]
  maxConfidenceEmotion = maxConfidenceRow['Emotions']
  maxConfidenceScore = maxConfidenceRow['Confidence Score']
  maxConfidenceTime = filename.replace('_', ':')
  maxConfidenceTime1 = maxConfidenceTime.replace(".csv","")
  maxConfidenceDf = pd.DataFrame({'Time':maxConfidenceTime1,'Emotion':maxConfidenceEmotion,'Confidence Score':maxConfidenceScore}, index=[0])

  final_df = final_df.append(maxConfidenceDf, ignore_index=True)

print(final_df)

final_df.to_csv('/home/fatema/Desktop/EmotionMaxScore/'+folder+'.csv', index=False)