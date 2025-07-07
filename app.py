from flask import Flask, request, jsonify
from models import collection
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def github_webhook():
    data = request.json
    event = request.headers.get('X-GitHub-Event')

    print(f"Received {event} event")

    author = data.get('pusher', {}).get('name', 'Unknown')
    timestamp = datetime.now(pytz.utc).strftime('%d %B %Y - %I:%M %p UTC')
    from_branch = None
    to_branch = None
    action_type = None

    if event == 'push':
        to_branch = data.get('ref', '').split('/')[-1]
        action_type = 'push'
    elif event == 'pull_request':
        action = data['action']
        if action == 'opened':
            from_branch = data['pull_request']['head']['ref']
            to_branch = data['pull_request']['base']['ref']
            action_type = 'pull_request'
    elif event == 'pull_request' and data['action'] == 'closed' and data['pull_request']['merged']:
        from_branch = data['pull_request']['head']['ref']
        to_branch = data['pull_request']['base']['ref']
        action_type = 'merge'

    if action_type:
        collection.insert_one({
            'author': author,
            'timestamp': timestamp,
            'from_branch': from_branch,
            'to_branch': to_branch,
            'action': action_type
        })

    return jsonify({'msg': 'Event received'}), 200

@app.route('/events', methods=['GET'])
def get_events():
    events = list(collection.find().sort('_id', -1))
    for e in events:
        e['_id'] = str(e['_id'])
    return jsonify(events)

@app.route('/')
def home():
    return "Welcome to GitHub Webhook Receiver!"


if __name__ == '__main__':
    app.run(debug=True)
