# Placement Drive Task App

This app packages the provided pages with authentication and backend endpoints.

## Included Pages

- `/ps1` - Intelligence Fusion Dashboard
- `/ps3` - Urban Growth Analytics
- `/ps4` - Traffic Intelligence Dashboard

## Auth

- Login page: `/login`
- Demo credentials:
  - `demo@stratfuse.ai / Demo@123`
  - `admin@stratfuse.ai / Admin@123`

## Backend Demo APIs

- `/api/me`
- `/api/ps1/intel-nodes`
- `/api/ps3/growth-zones`
- `/api/ps4/predicted-hotspots`

## Run

```powershell
cd D:\WebApps\placement_drive_task\backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.
