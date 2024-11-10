import re

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
    
    def tokenize(self):
        token_patterns = [
            ('NUMBER', r'\d+'),
            ('STRING', r'\"[^\"]*\"'),
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z_0-9]*'),
            ('OPERATOR', r'[+\-*/=<>]'),
            ('KEYWORD', r'\b(if|else|while|return)\b'),
            ('WHITESPACE', r'\s+')
        ]
        
        for regex_name, pattern in token_patterns:
            for match in re.finditer(pattern, self.source_code):
                self.tokens.append((regex_name, match.group()))
    
    def get_tokens(self):
        return self.tokens
