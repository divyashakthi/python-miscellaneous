pip_install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDENTIALS_FILE = 'path_to_file/credentials.json'

def get_calendar_service():
   creds = None
   if os.path.exists('token.pickle'):
       with open('token.pickle', 'rb') as token:
           creds = pickle.load(token)
   if not creds or not creds.valid:
       if creds and creds.expired and creds.refresh_token:
           creds.refresh(Request())
       else:
           flow = InstalledAppFlow.from_client_secrets_file(
               CREDENTIALS_FILE, SCOPES)
           creds = flow.run_local_server(port=0)
           
       with open('token.pickle', 'wb') as token:
           pickle.dump(creds, token)

   service = build('calendar', 'v3', credentials=creds)
   return service

from cal_setup import get_calendar_service

def main():
   service = get_calendar_service()
   print('Getting list of calendars')
   calendars_result = service.calendarList().list().execute()
   calendars = calendars_result.get('items', [])

   if not calendars:
       print('No calendars found.')
   for calendar in calendars:
       summary = calendar['summary']
       id = calendar['id']
       primary = "Primary" if calendar.get('primary') else ""
       print("%s\t%s\t%s" % (summary, id, primary))

if __name__ == '__main__':
   main()

import datetime
from cal_setup import get_calendar_service

def main():
   service = get_calendar_service()
   now = datetime.datetime.utcnow().isoformat() + 'Z' 
   print('Getting List o 10 events')
   events_result = service.events().list(
       calendarId='primary', timeMin=now,
       maxResults=10, singleEvents=True,
       orderBy='startTime').execute()
   events = events_result.get('items', [])

   if not events:
       print('No upcoming events found.')
   for event in events:
       start = event['start'].get('dateTime', event['start'].get('date'))
       print(start, event['summary'])

if __name__ == '__main__':
   main()
