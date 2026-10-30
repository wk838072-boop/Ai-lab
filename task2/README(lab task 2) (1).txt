Lab 1: AI Environments, PEAS, and Agent Control

Course: Artificial Intelligence Lab
Name: Muhammad Waqar
Roll No: 212

Overview

This lab studies two AI systems—a delivery robot and an LLM-based
student-support agent—and classifies their operating environments. It
also extends a temperature-control program so that it remembers its
previous target mode and avoids sending the same control command
repeatedly.

Lab Tasks

Task 1: PEAS Specifications

Create two separate PEAS specifications, one for a delivery robot and
one for an LLM-based student-support agent.

PEAS stands for: - P — Performance Measure: How the system’s success is
evaluated. - E — Environment: The surroundings or context in which the
system operates. - A — Actuators: The mechanisms or actions the system
uses to affect its environment. - S — Sensors: The inputs or sources
from which the system receives information.

Include at least two concrete entries for each component where
appropriate. Explain one constraint or performance trade-off for each
system. State the operational assumptions, including which tools the
student-support agent is allowed to access. Include both specifications
in the .docx report.

Task 2: Environment Classification

Classify both systems from Task 1 using these dimensions: -
Observability: Fully observable or partially observable. - Action
outcomes: Deterministic or stochastic.

For each classification: - Give a justification. - Identify an example
of an observable or hidden variable. - Give an example of a predictable
or uncertain action outcome. - Explain the difference between the real
environment and a simplified simulator.

Make sure the classifications are based on clearly stated assumptions.

Task 3: Remember the Previous Control Mode

Extend the existing temperature-control code so it stores the previous
target mode and avoids sending repeated identical commands.

Requirements: - Keep the existing temperature thresholds. - Preserve
occupancy priority. - Store the previous target mode internally. -
Return both the target mode and whether a command should be sent.

Test the program with: 1. Repeated identical percepts. 2. The first
exact temperature boundary. 3. The second exact temperature boundary. 4.
A mode transition. 5. An empty-room case.

For every test, record: - Previous mode. - Percept (temperature and
occupancy). - Target mode. - Command sent or no command sent.

Project Files

Suggested project files: - README.md — this file. - Lab1_Report.docx —
PEAS specifications, environment classifications, assumptions, and test
results. - temperature_control.py — temperature-control implementation
with previous-mode memory. - output.txt — captured output from the
required tests.

Requirements

-   Python 3.8 or newer.
-   No extra libraries are required for the basic Python implementation.

How to Run

After saving the implementation as temperature_control.py, run:

    python temperature_control.py

Expected Learning Outcomes

After completing this lab, students should be able to: - Describe AI
agents using PEAS specifications. - Classify environments by
observability and action-outcome uncertainty. - Explain assumptions and
trade-offs in real systems and simplified simulators. - Implement
stateful control logic. - Test repeated inputs, boundary conditions,
mode transitions, and empty-room behavior.
