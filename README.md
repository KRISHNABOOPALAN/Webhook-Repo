# GitHub Activity Tracker (Developer Assessment Task)

This project captures GitHub repository activities (`push`, `pull_request`, `merge`) using webhooks and stores them in MongoDB Atlas. A minimal frontend polls the backend every 15 seconds to display recent events.

---

## 🚀 Project Structure

github-activity-tracker/
│
├── webhook-repo/ # Flask backend for webhook handling
│ ├── app.py
│ ├── config.py
│ ├── models.py
│ ├── requirements.txt
│ └── .env # MongoDB URI stored here (not committed)
│
├── frontend/ # Simple UI polling Flask every 15s
│ ├── index.html
│ └── script.js



---

## 🧑‍💻 Features

- Flask API to receive GitHub webhook events
- Stores push, pull request, and merge events in MongoDB Atlas
- UI auto-refreshes events every 15 seconds
- Simple JSON schema:
  ```json
  {
    "author": "Krish",
    "to_branch": "main",
    "from_branch": "feature-1",
    "action": "push | pull_request | merge",
    "timestamp": "7 July 2025 - 11:45 PM UTC"
  }


### Clone the repo

git clone https://github.com/your-username/github-activity-tracker.git
cd github-activity-tracker/webhook-repo

### Install Python dependencies

pip install -r requirements.txt


### Setup .env

MONGO_URI=mongodb+srv://<username>:<encoded-password>@cluster0.mongodb.net/github_events?retryWrites=true&w=majority


### Run
python app.py
Runs on: http://localhost:5000


### Testing
Use curl (PowerShell format):

Push Event:
curl -Method POST http://localhost:5000/webhook `
  -Headers @{ "Content-Type" = "application/json"; "X-GitHub-Event" = "push" } `
  -Body '{ "pusher": { "name": "Krish" }, "ref": "refs/heads/main" }'

 Pull Request
 curl -Method POST http://localhost:5000/webhook `
  -Headers @{ "Content-Type" = "application/json"; "X-GitHub-Event" = "pull_request" } `
  -Body '{ "action": "opened", "pull_request": { "head": { "ref": "feature-1" }, "base": { "ref": "main" } }, "pusher": { "name": "Krish" } }'


Merge Event

curl -Method POST http://localhost:5000/webhook `
  -Headers @{ "Content-Type" = "application/json"; "X-GitHub-Event" = "pull_request" } `
  -Body '{ "action": "closed", "pull_request": { "merged": true, "head": { "ref": "feature-1" }, "base": { "ref": "main" } }, "pusher": { "name": "Krish" } }'


### Frontend
Open frontend/index.html in your browser

Every 15 seconds it fetches latest events from /events API


### Technologies
Flask (Python)

MongoDB Atlas (Cloud DB)

Bootstrap 5 (UI)

JavaScript (Polling)

