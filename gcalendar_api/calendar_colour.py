from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def main():
    # Credentials Check
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

        service = build("calendar", "v3", credentials=creds)

        # Call the Calendar API and get the list of Calendars for the user account
        colors = service.colors().get().execute()

        # Print available calendarListEntry colors.
        for id, color in colors['calendar'].iteritem():
            print ('colorId: %s' % id)
            print ('  Background: %s' % color['background'])
            print ('  Foreground: %s' % color['foreground'])
        # Print available event colors.
        for id, color in colors['event'].iteritem():
            print ('colorId: %s' % id)
            print ('  Background: %s' % color['background'])
            print ('  Foreground: %s' % color['foreground'])


if __name__ == "__main__":
    main()
