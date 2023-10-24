class SumBlock:
    def __init__(self):
        self.input1 = 0
        self.input2 = 0

    def set_inputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def execute(self):
        result = self.input1 + self.input2
        return result

