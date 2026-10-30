from lab2_percepts import ClassroomAgent
from lab2_model import StatefulClassroomAgent, ReflexClassroomAgent, print_trace
def check_reflex_expected_modes():
    agent = ClassroomAgent()
    percepts = [(29, True), (29, True), (20, True), (26, True), (19, True), (29, False)]
    expected = ["COOL", "COOL", "IDLE", "IDLE", "WARM", "ECO"]
    got = [agent.act(*p) for p in percepts]
    assert got == expected, (got, expected)
    print("PASS reflex agent matches expected modes:", got)
def check_repeated_percepts():
    agent = StatefulClassroomAgent()
    first = agent.act(29, True)
    second = agent.act(29, True)
    assert first == (None, "COOL", True)
    assert second == ("COOL", "COOL", False)
    print("PASS repeated percept: first SEND, second NO-SEND")
def check_exact_boundaries():
    agent = StatefulClassroomAgent()
    assert agent.act(20, True)[1] == "IDLE"
    assert agent.act(26, True)[1] == "IDLE"
    print("PASS exact boundaries 20 C and 26 C are IDLE")
def check_mode_transition():
    agent = StatefulClassroomAgent()
    agent.act(24, True)
    prev, target, send = agent.act(19, True)
    assert (prev, target, send) == ("IDLE", "WARM", True)
    print("PASS mode transition IDLE -> WARM sends a command")
def check_empty_room_priority():
    agent = StatefulClassroomAgent()
    assert agent.act(29, False)[1] == "ECO"
    assert agent.act(15, False)[1] == "ECO"
    assert agent.act(15, False)[2] is False
    print("PASS empty room gives ECO regardless of temperature, no repeat")
def edge_case_noisy_sequence():
    noisy = [(25.9, True), (26.1, True), (25.9, True), (26.1, True), (25.9, True)]
    print()
    print_trace(noisy, "Edge case: noisy temperature around 26 C")
    agent = StatefulClassroomAgent()
    sends = sum(agent.act(*p)[2] for p in noisy)
    assert sends == len(noisy)
    print(f"Commands sent: {sends} of {len(noisy)} readings.")
    print("The agent chatters between IDLE and COOL because the thresholds are")
    print("sharp. Remembering the previous mode only suppresses identical")
    print("repeats; it does not add a dead band (hysteresis).")
def compare_reflex_vs_stateful():
    seq = [(29, True)] * 4 + [(24, True)] * 2 + [(29, False)] * 2
    reflex = ReflexClassroomAgent()
    stateful = StatefulClassroomAgent()
    reflex_commands = len([reflex.act(*p) for p in seq])
    stateful_commands = sum(stateful.act(*p)[2] for p in seq)
    assert stateful_commands < reflex_commands
    print()
    print(f"Comparison on {len(seq)} percepts: reflex sent {reflex_commands} commands, stateful sent {stateful_commands}.")
if __name__ == "__main__":
    check_reflex_expected_modes()
    check_repeated_percepts()
    check_exact_boundaries()
    check_mode_transition()
    check_empty_room_priority()
    compare_reflex_vs_stateful()
    edge_case_noisy_sequence()
    print("\nAll checks passed.")
