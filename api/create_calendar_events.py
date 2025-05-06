# (Original script with tweak to return created links)
import os, sys, pickle, json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# definitions...

def main(return_links=False):
    svc = get_calendar_service()
    evts = json.load(open('events.json'))
    links = []
    for ev in evts:
        created = create_event(svc, ev)
        links.append(created.get('htmlLink'))
    if return_links:
        return links
    print(f"Created {len(links)} events")