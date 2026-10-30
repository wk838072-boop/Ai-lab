SCORE_THRESHOLD = 70
GPA_THRESHOLD = 2.5


def rule_based_extended(score, documents_complete, has_recommendation_letter, gpa):
    if score < SCORE_THRESHOLD:
        return "Hold", f"score {score} is below {SCORE_THRESHOLD}"
    if not documents_complete:
        return "Hold", "documents are incomplete"
    if not has_recommendation_letter:
        return "Hold", "recommendation letter is missing"
    if gpa < GPA_THRESHOLD:
        return "Hold", f"gpa {gpa} is below {GPA_THRESHOLD}"
    return "Review", "all conditions met"


test_cases = [
    ("pass_case", 85, True, True, 3.4, "Review",
     "Normal application that meets every condition."),
    ("fail_recommendation", 85, True, False, 3.4, "Hold",
     "Isolates new condition 1: only the recommendation letter is missing."),
    ("fail_gpa", 85, True, True, 2.0, "Hold",
     "Isolates new condition 2: only the gpa is too low."),
    ("boundary", 70, True, True, 2.5, "Review",
     "Tests >= at the exact threshold values (score 70, gpa 2.5)."),
]

print("Thresholds are synthetic lab assumptions (score >= 70, gpa >= 2.5).")
print("=" * 60)

all_passed = True
for name, score, docs, rec, gpa, expected, why in test_cases:
    actual, reason = rule_based_extended(score, docs, rec, gpa)
    status = "PASS" if actual == expected else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"Case: {name}")
    print(f"  Input    : score={score}, documents_complete={docs}, "
          f"recommendation={rec}, gpa={gpa}")
    print(f"  Expected : {expected}")
    print(f"  Actual   : {actual}")
    print(f"  Reason   : {reason}")
    print(f"  Why chosen: {why}")
    print(f"  Result   : {status}")
    print("-" * 60)

print("All test cases passed." if all_passed else "Some test cases FAILED.")
