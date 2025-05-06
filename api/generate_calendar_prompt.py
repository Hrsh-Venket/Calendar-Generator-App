# (Same as your original script, with one small tweak to return string)
import os, sys, json
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly',
          'https://www.googleapis.com/auth/tasks.readonly']
TOKEN_PATH = 'token.json'
CREDENTIALS_PATH = 'credentials.json'
PROMPT_END_FILE = 'prompt_end.txt'
OUTPUT_PROMPT = 'prompt.txt'

# ... keep all helper functions as-is ...

def main(return_string=False):
    # Authenticate and fetch
    cal_svc, tasks_svc = get_services()
    events = fetch_todays_events(cal_svc)
    tasks = fetch_tasks(tasks_svc)
    custom = open(PROMPT_END_FILE).read()
    full = build_full_prompt(events, tasks, custom)
    with open(OUTPUT_PROMPT, 'w') as f:
        f.write(full)
    if return_string:
        return full
    print(f"Wrote prompt to {OUTPUT_PROMPT}")