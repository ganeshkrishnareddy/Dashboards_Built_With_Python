# Dashboard Bulit with Python

I built this project as part of a placement-drive task where I had to select multiple problem statements and deliver working web apps with separate deployments.

Project name used for submission: **Dashboard Bulit with Python**

Repository: https://github.com/ganeshkrishnareddy/Dashboards_Built_With_Python

## What is in this repository

This repo contains 4 deployable folders:

- `vercel_ps1` - Problem Statement 1: Intelligence Fusion Dashboard
- `vercel_ps3` - Problem Statement 3: Predictive Urban Growth Dashboard
- `vercel_ps4` - Problem Statement 4: Predictive Traffic Intelligence Dashboard
- `vercel_landing` - One landing page linking all three dashboards

I also kept a `backend` folder from an earlier login-enabled integration attempt, but the final public submission is served through the four Vercel folders listed above.

## Live links

- Landing Page: https://pgk-placement-drive.vercel.app
- PS1: https://pgk-ps1-intelligence.vercel.app
- PS3: https://pgk-ps3-urban-growth.vercel.app
- PS4: https://pgk-ps4-traffic-intel.vercel.app

## How I built this

1. I started by extracting and reviewing the problem statements from the PDF.
2. I selected three statements and created separate project folders for each solution.
3. I integrated the provided UI files and adapted each project for independent Vercel deployment.
4. I created custom aliases so each dashboard has its own clean URL.
5. I created an additional landing page that acts as an entry point to all three live apps.
6. I removed old temporary deployments and local artifacts that were no longer needed.
7. I disabled Vercel deployment protection (SSO/password) so links open publicly without login prompts.

## Run locally (optional)

For static Vercel folders, you can open the HTML directly or run any simple static server.

For backend demo app:

```powershell
cd backend
python -m pip install -r requirements.txt
python app.py
```

## About me

Done by me,

**P Ganesh Krishna Reddy**

- Phone: +91-8374622779
- Email: pganeshkrishnareddy@gmail.com
- Portfolio: https://pganeshkrishnareddy.vercel.app
- LinkedIn: https://linkedin.com/in/pganeshkrishnareddy
- GitHub: https://github.com/ganeshkrishnareddy
