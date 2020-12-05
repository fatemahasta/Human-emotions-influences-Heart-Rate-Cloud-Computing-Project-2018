import pandas as pd
import os

basePath = 'C:\\Users\\Shreya\\Desktop\\Cloud Computing\\Project\\shreyaa\\'
folder = 'heart_rate'
fullPath = basePath+folder+'/'

maxRows = []
fileNames = []

columns = ['Date','Max Heart Rate','Min Heart Rate']
final_df = pd.DataFrame(columns=columns)

for filename in os.listdir(fullPath):
  dataFrame = pd.read_csv(fullPath+filename)

  maxhrRow = dataFrame.loc[dataFrame['Heart Rate'].idxmax()]
  minhrRow = dataFrame.loc[dataFrame['Heart Rate'].idxmin()]
  maxhrScore = maxhrRow['Heart Rate']
  minhrScore = minhrRow['Heart Rate']
  changehr = filename.replace("%Y-%m-%d", "%m/%d/%Y")
  hrdate = changehr.replace(".csv","")
  hrdf = pd.DataFrame({'Date':hrdate,'Max Heart Rate':maxhrScore,'Min Heart Rate':minhrScore}, index=[0])

  final_df = final_df.append(hrdf, ignore_index=True)

print(final_df)

final_df.to_csv('C:\\Users\\Shreya\\Desktop\\Cloud Computing\\Project\\shreyaa\\'+folder+'.csv', index=False)