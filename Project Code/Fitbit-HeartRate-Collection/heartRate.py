import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd
import datetime
CLIENT_ID = '22D4L8'
CLIENT_SECRET = 'c53da07fa1809ef85eb76a2a76161993'

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
print(ACCESS_TOKEN)
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
print(REFRESH_TOKEN)
auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))
yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
today = str(datetime.datetime.now().strftime("%Y%m%d"))

fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date='2018-10-26', detail_level='1sec')
print(fit_statsHR)
time_list = []
val_list = []
for i in fit_statsHR['activities-heart-intraday']['dataset']:
    val_list.append(i['value'])
    time_list.append(i['time'])
heartdf = pd.DataFrame({'Heart Rate':val_list,'Time':time_list})
print(heartdf)

heartdf.to_csv('/home/fatema/Desktop/Heart/heart'+ \
               '2018-10-26' +'.csv', \
               columns=['Time','Heart Rate'], header=True, \
               index = False)

