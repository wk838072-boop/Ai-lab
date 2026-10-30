# Lab 1: Introduction to AI and Paradigms

**Course:** Artificial Intelligence Lab\
**Name:** Muhammad Waqar\
**Roll No:** 212

## Overview

This lab explores Artificial Intelligence concepts through a
scholarship-screening example. It includes an AI history timeline, an
extended rule-based checker, a comparison between symbolic and
threshold-based systems, and a discussion of why fluent conversation is
not sufficient evidence of general intelligence.

All thresholds and example values are synthetic lab assumptions. A
`Review` result only sends an application for human review; it does not
make a final scholarship award decision.

## Tasks

### Task 1: AI History Timeline

Create a chronological timeline containing at least five AI milestones.
Each entry must include: - Year or period - Historical event -
One-sentence explanation of its significance - Source or reference

The timeline must include an AI-winter period and a modern compute/data
milestone. This is a historical research task, not a model-training
exercise.

### Task 2: Extended Rule-Based Scholarship Checker

Retain the original conditions: - `score >= 70` - Documents must be
complete.

Add two explicit conditions: - `has_recommendation_letter == True` -
`gpa >= 2.5`

Prepare exactly four core test cases: 1. A passing case where all
conditions are satisfied. 2. A case that fails the recommendation-letter
condition. 3. A case that fails the GPA condition. 4. A boundary case
using `score = 70` and `gpa = 2.5`.

For each test case, print: - Input values - Expected result - Actual
result - Reason for the result

Explain why the four test cases were selected. State clearly that all
thresholds are synthetic lab assumptions.

### Task 3: Conversational Test vs General Intelligence

Write a focused comparison using the scholarship-screening example.
Explain: - What a conversational test, such as the Turing Test,
observes. - Why passing a conversational test does not prove general
intelligence. - An example of fluent but incorrect reasoning. - One
additional test for measuring reliable task performance.

Support historical claims with appropriate sources.

## Project Files

-   `lab1_compare.py` --- compares symbolic rule-based decisions with
    threshold-based decisions.
-   `lab1_rules.py` --- implements the extended rule-based checker with
    two additional conditions and four core test cases.
-   `output.txt` --- contains the captured program output.
-   `Lab1_Report.docx` --- contains the report, timeline, test results,
    comparison, reflection, and references.

## Requirements

-   Python 3.8 or newer
-   No additional Python libraries required

## How to Run

Open a terminal in the project directory and execute:

``` bash
python lab1_compare.py
python lab1_rules.py
```

## Expected Learning Outcomes

After completing this lab, students should be able to: - Identify
important milestones in AI history and cite sources. - Implement
transparent, rule-based decision systems. - Test program behavior using
normal and boundary cases. - Compare symbolic and threshold-based
approaches. - Distinguish convincing conversation from reliable task
performance. - Recognize the importance of clear assumptions and human
review.
