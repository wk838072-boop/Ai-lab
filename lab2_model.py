HIGH = 26
LOW = 20
def decide_mode(temp, occupied):
    if not occupied:
        return "ECO"
    if temp > HIGH:
        return "COOL"
    if temp < LOW:
        return "WARM"
    return "IDLE"
class ReflexClassroomAgent:
    def act(self, temp, occupied):
        return decide_mode(temp, occupied)
class StatefulClassroomAgent:
    def __init__(self):
        self.prev_mode = None
    def act(self, temp, occupied):
        target = decide_mode(temp, occupied)
        previous = self.prev_mode
        send_command = target != previous
        self.prev_mode = target
        return previous, target, send_command
def print_trace(percepts, title):
    agent = StatefulClassroomAgent()
    print(title)
    print(f"{'step':<5}{'prev mode':<11}{'percept':<16}{'target':<8}outcome")
    print("-" * 56)
    for step, percept in enumerate(percepts, 1):
        previous, target, send = agent.act(*percept)
        outcome = "SEND" if send else "NO-SEND"
        print(f"{step:<5}{str(previous):<11}{str(percept):<16}{target:<8}{outcome}")
    print()
if __name__ == "__main__":
    sequence = [(29, True), (29, True), (20, True), (26, True), (19, True), (29, True), (29, False), (19, False)]
    print_trace(sequence, "Stateful agent: complete mode-transition trace")
    reflex = ReflexClassroomAgent()
    sends = len(sequence)
    stateful = StatefulClassroomAgent()
    sends_stateful = sum(stateful.act(*p)[2] for p in sequence)
    print("Reflex agent commands sent :", sends, "of", len(sequence))
    print("Stateful agent commands sent:", sends_stateful, "of", len(sequence))
