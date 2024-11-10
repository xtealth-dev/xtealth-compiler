class IRGenerator:
    def __init__(self):
        self.ir_code = []
    
    def generate_ir(self, ast):
        for node in ast:
            if node[0] == 'IfStatement':
                self.ir_code.append('if ' + node[1])
        return self.ir_code
