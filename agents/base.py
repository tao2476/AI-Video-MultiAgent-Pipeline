class BaseAgent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def run(self, input_data):
        raise NotImplementedError("Subclasses must implement run()")