class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.ast = []
    
    def parse(self):
        while self.tokens:
            token = self.tokens.pop(0)
            if token[0] == 'KEYWORD' and token[1] == 'if':
                self.ast.append(('IfStatement', self.parse_expression()))
    
    def parse_expression(self):
        return 'expression'
    
    def get_ast(self):
        return self.ast
