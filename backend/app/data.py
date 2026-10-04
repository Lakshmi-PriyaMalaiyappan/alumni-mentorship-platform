# Sample data for the prototype (replaced by a database in Phase II)
ALUMNI = [
    {"id": 1, "name": "Priya R.", "role": "Software Engineer", "company": "TechCorp", "domain": "Software Development",
     "skills": ["React", "Node.js", "System Design", "SQL"]},
    {"id": 2, "name": "Arun K.", "role": "Data Scientist", "company": "DataWorks", "domain": "Data Science",
     "skills": ["Python", "Machine Learning", "SQL", "Statistics"]},
    {"id": 3, "name": "Meena S.", "role": "Product Manager", "company": "CloudNine", "domain": "Product",
     "skills": ["Product Strategy", "Analytics", "Communication"]},
    {"id": 4, "name": "Ravi V.", "role": "DevOps Engineer", "company": "InfraLabs", "domain": "Cloud and DevOps",
     "skills": ["AWS", "Docker", "CI/CD", "Linux"]},
    {"id": 5, "name": "Sneha N.", "role": "UX Designer", "company": "DesignHub", "domain": "Design",
     "skills": ["Figma", "User Research", "Prototyping"]},
]

# Skill level (0-100) expected for each target role
ROLE_REQUIREMENTS = {
    "Full Stack Developer": {"React": 90, "Node.js": 85, "SQL": 80, "System Design": 70, "Git": 70},
    "Data Scientist": {"Python": 90, "Machine Learning": 85, "SQL": 75, "Statistics": 80},
    "DevOps Engineer": {"Linux": 85, "Docker": 85, "CI/CD": 80, "AWS": 80},
}
