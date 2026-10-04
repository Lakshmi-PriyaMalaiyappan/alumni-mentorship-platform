def analyse_gap(required, student_skills):
    """Compare student skill levels (0-100) with the levels required for a role."""
    gaps, total = [], 0
    for skill, need in required.items():
        have = student_skills.get(skill, 0)
        total += min(have, need) / need
        gaps.append({"skill": skill, "current": have, "required": need, "gap": max(need - have, 0)})
    gaps.sort(key=lambda g: g["gap"], reverse=True)
    return {"readiness_percent": round(total / len(required) * 100, 1), "gaps": gaps,
            "focus_on": [g["skill"] for g in gaps if g["gap"] > 0][:3]}
