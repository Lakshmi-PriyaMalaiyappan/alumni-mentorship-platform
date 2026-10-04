# AI-Powered Smart Alumni Mentorship & Career Intelligence Platform

Final Year Project – Department of CSE

## Problem
Students lack personalized career guidance, and alumni networks are unstructured. Mentor selection is random and placement teams have no analytics on alumni outcomes.

## Solution
A web platform that
1. **Matches** students with the most suitable alumni mentors using AI (TF-IDF + cosine similarity on profiles),
2. **Analyses skill gaps** between a student's skills and a target role,
3. Provides **career insights** from alumni data (planned) and a mentorship management + analytics dashboard (planned).

## Tech Stack
- Backend: Python, FastAPI, scikit-learn
- Frontend: HTML/JS (React planned for Phase II)
- Database: MongoDB / PostgreSQL (planned for Phase II; sample in-memory data now)

## Project Structure
```
backend/app/main.py       REST API
backend/app/matching.py   AI mentor matching
backend/app/skillgap.py   Skill-gap analyzer
backend/app/data.py       Sample alumni data and role requirements
frontend/index.html       Simple demo UI
docs/                     Diagrams and UI screens
```

## Run the backend
```
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```
API docs: http://127.0.0.1:8000/docs

## Run the frontend
Open `frontend/index.html` in a browser (backend must be running).

## API
- `GET  /alumni` – list alumni
- `GET  /roles` – list target roles
- `POST /match` – `{ "skills": [...], "interests": [...], "target_role": "...", "top_n": 3 }`
- `POST /skill-gap` – `{ "target_role": "...", "skills": { "React": 70 } }`

## Status
Phase I: architecture, UML and ER design, UI prototype, matching and skill-gap prototype.
Phase II (planned): database, authentication, session booking, feedback, career analytics dashboard, deployment.

## Team
- Lakshmipriya Malaiyappan – [module]
- [Member 2] – [module]
- [Member 3] – [module]

Guide: [Guide name]
