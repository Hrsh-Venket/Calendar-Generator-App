# (Original script with tweak to return objects)
import os, sys, json
from google import genai
from pydantic import BaseModel
from datetime import datetime

# definitions...

class CalendarEvent(BaseModel):
    # fields...

# helper functions...

def main(return_objects=False):
    key = os.getenv('GEMINI_API_KEY') or sys.exit()
    prompt = open('prompt.txt').read()
    client = genai.Client(api_key=key)
    resp = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt],
        config={
            'response_mime_type': 'application/json',
            'response_schema': list[CalendarEvent]
        }
    )
    events = resp.parsed
    with open(OUTPUT_FILE, 'w') as f:
        json.dump([e.dict() for e in events], f, default=str, indent=2)
    if return_objects:
        return events
    print(f"Wrote {len(events)} events to {OUTPUT_FILE}")