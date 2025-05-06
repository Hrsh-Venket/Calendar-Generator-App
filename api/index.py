from flask import Flask, jsonify, request
import os

# Import your scripts as modules
import generate_calendar_prompt as gen_prompt
import generate_calendar_events as gen_events
import create_calendar_events as create_events

app = Flask(__name__)

@app.route('/prompt', methods=['POST'])
def build_prompt():
    """
    Triggers Part 1: fetch today's events & tasks, build and return the raw prompt.
    Returns the combined prompt text.
    """
    # Ensure required files exist
    if not os.path.isfile('credentials.json'):
        return jsonify(error="Missing credentials.json"), 400
    if not os.path.isfile('prompt_end.txt'):
        return jsonify(error="Missing prompt_end.txt"), 400

    # Run the prompt builder
    output = gen_prompt.main(return_string=True)
    return jsonify(prompt=output)

@app.route('/generate-events', methods=['POST'])
def generate_events():
    """
    Triggers Part 2: reads prompt.txt, calls Gemini, and returns structured events.
    Expects GEMINI_API_KEY in env.
    """
    key = os.getenv('GEMINI_API_KEY')
    if not key:
        return jsonify(error="GEMINI_API_KEY not set"), 400

    events = gen_events.main(return_objects=True)
    return jsonify(events=[e.dict() for e in events])

@app.route('/create-events', methods=['POST'])
def create_calendar_events():
    """
    Triggers Part 3: reads events.json and creates them in Google Calendar.
    Returns list of created event URLs.
    """
    if not os.path.isfile('events.json'):
        return jsonify(error="Missing events.json. Run /generate-events first."), 400

    results = create_events.main(return_links=True)
    return jsonify(created=results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')