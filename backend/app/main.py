from typing import Dict, List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .data import ALUMNI, ROLE_REQUIREMENTS
from .matching import match_mentors
from .skillgap import analyse_gap

app = FastAPI(title="Alumni Mentorship & Career Intelligence API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


class MatchRequest(BaseModel):
    skills: List[str] = []
    interests: List[str] = []
    target_role: str = ""
    top_n: int = 3


class GapRequest(BaseModel):
    target_role: str
    skills: Dict[str, int]


@app.get("/alumni")
def alumni():
    return ALUMNI


@app.get("/roles")
def roles():
    return list(ROLE_REQUIREMENTS)


@app.post("/match")
def match(req: MatchRequest):
    return match_mentors(req.dict(), ALUMNI, req.top_n)


@app.post("/skill-gap")
def skill_gap(req: GapRequest):
    if req.target_role not in ROLE_REQUIREMENTS:
        raise HTTPException(404, "Unknown role")
    return analyse_gap(ROLE_REQUIREMENTS[req.target_role], req.skills)
