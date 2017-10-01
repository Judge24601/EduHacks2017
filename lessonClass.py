def __init__(self, name, gates, task, completionState):
    self.name = name #string
    self.gates = gates #string list
    self.task = task #string
    self.completionState = completionState #string

    self.completed = False

def checkCompletion(gatesOutput):
    if gatesOutput == self.completionState:
        return True
    else:
        return False
