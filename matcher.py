# matcher.py - Student Scholarship Information System (MVP matching engine)
# Group B11 | PBL Progress Report - II | Rule-based eligibility matching

# Weights from Progress Report I (total = 100)
WEIGHTS = {"income": 30, "marks": 25, "category": 20, "course": 15, "state": 10}

# Sample Scheme X: a made-up scheme used only to explain the logic
SCHEME_X = {
    "name": "Sample Scheme X",
    "max_income": 250000,                      # family income up to Rs 2.5 lakh
    "min_marks": 75,                           # at least 75% in last exam
    "categories": {"SC", "ST", "OBC"},
    "courses": {"BTech"},
    "states": {"Uttar Pradesh"},
}

def match(student, scheme):
    """Return (status, score, failed_rules) for one student and one scheme."""
    passed = {
        "income":   student["income"] <= scheme["max_income"],
        "marks":    student["marks"] >= scheme["min_marks"],
        "category": student["category"] in scheme["categories"],
        "course":   student["course"] in scheme["courses"],
        "state":    student["state"] in scheme["states"],
    }
    score = sum(w for rule, w in WEIGHTS.items() if passed[rule])
    failed = [rule for rule, ok in passed.items() if not ok]
    # All rules are mandatory: any failed rule means "Not eligible".
    # The score is still shown, only for the student's information.
    status = "Eligible" if not failed else "Not eligible"
    return status, score, failed

if __name__ == "__main__":
    profiles = {
        "A": dict(category="OBC",     income=240000, marks=82, state="Uttar Pradesh", course="BTech"),
        "B": dict(category="General", income=400000, marks=90, state="Uttar Pradesh", course="BTech"),
        "C": dict(category="SC",      income=180000, marks=70, state="Delhi",         course="BTech"),
    }
    for name, p in profiles.items():
        status, score, failed = match(p, SCHEME_X)
        print(f"Profile {name}: {status}, score {score}, failed: {failed or 'none'}")
