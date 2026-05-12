# Fraud Alert Summarization and Prioritization Dashboard

A full-stack web application for banking fraud alert triage. The project provides a secure login flow, role-based navigation, an alerts dashboard for analysts, an admin dashboard for user/system management, and a RAG lab for document-grounded AI experimentation.

The main goal is to help fraud analysts quickly understand large volumes of technical fraud alerts by showing clear summaries, severity ranking, risk indicators, and drill-down details.

## What This Project Does

- Lets users log in securely.
- Shows an Alerts page after login.
- Allows analysts to upload alert datasets in JSON or XML format.
- Displays alert severity, summaries, risk indicators, and original alert details.
- Opens a popup with full alert properties when an alert is clicked.
- Shows a severity distribution chart for the alert queue.
- Gives admins an extra Admin Dashboard tab for users, logs, stats, and usage.
- Includes a RAG Lab for asking questions against indexed documents.

## Tech Stack

Frontend:

- React: builds the browser user interface.
- Vite: runs and builds the frontend quickly.
- React Router: handles pages like `/login`, `/alerts`, `/dashboard`, and `/rag-lab`.
- CSS/Tailwind setup: the app uses a custom dark "cyber-terminal" style with shared CSS variables.

Backend:

- Flask: Python web server and API.
- Flask-JWT-Extended: login tokens and authentication.
- Flask-SQLAlchemy: database models and queries.
- SQLite: local database stored in `backend/hackathon.db`.
- Flask-CORS: allows frontend/backend communication during development.

AI / RAG:

- OpenAI API support.
- ChromaDB for vector storage.
- PDF/document ingestion from `llm/documents`.

Data:

- `fraud_alerts.json`: sample/generated fraud alert input.
- `fraud_alert_generator.py`: Python script for generating alert data.
- `kaggle_dataset/`: supporting fraud/transaction datasets.

## Project Structure

```text
hackathon_template_repo/
  backend/                 Flask backend API
    app.py                 Starts the backend server
    routes.py              API routes for login, users, logs, alert upload, etc.
    db.py                  Database models and default users
    config.py              Backend configuration
    requirements.txt       Python dependencies

  frontend/                React frontend
    src/pages/AlertsPage.jsx
    src/pages/AdminDashboard.jsx
    src/pages/LoginPage.jsx
    src/pages/RagLab.jsx
    src/services/api.js
    package.json

  llm/                     RAG/document files
    documents/             Put source documents here
    rag/                   RAG service code

  kaggle_dataset/          Dataset files
  fraud_alert_generator.py Alert generator script
  fraud_alerts.json        Example generated alerts
```

## Prerequisites

Install these before running the project:

- Python 3.10 or newer
- Node.js 18 or newer
- npm, which comes with Node.js

To check if they are installed, open PowerShell and run:

```powershell
python --version
node --version
npm --version
```

## How To Run The Project

You need two terminals:

- Terminal 1 runs the backend.
- Terminal 2 runs the frontend.

### 1. Open The Project Folder

```powershell
cd "C:\Users\mrari\Desktop\Project folder AI Fridays\fraud alert system\hackathon_template_repo"
```

### 2. Start The Backend

From the project root:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
python backend\app.py
```

If successful, the backend runs at:

```text
http://127.0.0.1:5000
```

Keep this terminal open.

### 3. Start The Frontend

Open a new PowerShell terminal and run:

```powershell
cd "C:\Users\mrari\Desktop\Project folder AI Fridays\fraud alert system\hackathon_template_repo\frontend"
npm install
npm run dev
```

If successful, Vite will show a local URL similar to:

```text
http://127.0.0.1:5173
```

Open that URL in your browser.

## Login Details

The backend creates default users when it starts.

Admin user:

```text
Username: admin
Password: admin123
```

Viewer user:

```text
Username: viewer
Password: viewer123
```

Admin users can access:

- Alerts
- Admin Dashboard

Viewer users can access:

- Alerts

## Main Pages

### Login Page

The first page users see. After login, users are sent to the Alerts page.

### Alerts Page

This is the main fraud analyst workspace.

It includes:

- Alert upload section for JSON/XML files
- Severity filter
- Search box
- Sort dropdown
- Severity KPI cards
- Severity mix chart
- Ranked alert queue
- Alert drill-down panel
- Popup modal with full alert properties
- Feedback buttons for generated summaries

Expected alert fields include:

```text
alert_id
timestamp
account_id
transaction_amount
transaction_type
location
device_info
alert_type
severity_score
severity_label
alert_description
risk_indicators
investigation_outcome
```

### Admin Dashboard

Only admins can access this page.

It includes:

- User statistics
- User management
- System logs
- LLM usage/cost summary

### RAG Lab

Used for document-based AI question answering.

You can place documents in:

```text
llm/documents
```

Then use the RAG page to ask questions against indexed content.

## Uploading Alert Data

On the Alerts page:

1. Choose file type: JSON or XML.
2. Select your generated alert file.
3. Click `Upload Dataset`.
4. The frontend sends the file to the backend for processing.

Example JSON shape:

```json
[
  {
    "alert_id": "ALERT-1001",
    "timestamp": "2026-05-12T10:30:00",
    "account_id": "ACC-12345",
    "transaction_amount": 75000,
    "transaction_type": "transfer",
    "location": "Mumbai, India",
    "device_info": "Chrome / Windows",
    "alert_type": "large transfer",
    "severity_score": 91,
    "severity_label": "Critical",
    "alert_description": "Large transfer from new device with IP mismatch.",
    "risk_indicators": ["IP mismatch", "new device", "high amount"],
    "investigation_outcome": "pending"
  }
]
```

## Useful Commands

Run frontend lint:

```powershell
cd frontend
npm run lint
```

Build frontend for production:

```powershell
cd frontend
npm run build
```

Run backend syntax check:

```powershell
python -m py_compile backend\routes.py
```

## Troubleshooting

If frontend login fails:

- Make sure the backend is running on `http://127.0.0.1:5000`.
- Make sure the frontend was started with `npm run dev`.
- Check that `frontend/vite.config.js` still proxies `/api` to `http://127.0.0.1:5000`.

If PowerShell blocks virtual environment activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

If `npm install` fails:

- Check Node.js is installed.
- Delete `frontend/node_modules` and run `npm install` again.

If Python packages fail to install:

- Confirm your virtual environment is activated.
- Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

## Notes For Future Improvements

- Store uploaded alert records in a database table.
- Connect uploaded alerts directly to the frontend alert queue.
- Add real AI summarization for uploaded alert descriptions.
- Add export options for analyst reports.
- Add more charts for false positives, fraud outcomes, and transaction type distribution.

## Quick Start Summary

Terminal 1:

```powershell
cd "C:\Users\mrari\Desktop\Project folder AI Fridays\fraud alert system\hackathon_template_repo"
.\venv\Scripts\Activate.ps1
python backend\app.py
```

Terminal 2:

```powershell
cd "C:\Users\mrari\Desktop\Project folder AI Fridays\fraud alert system\hackathon_template_repo\frontend"
npm run dev
```

Browser:

```text
http://127.0.0.1:5173
```
