from .tokens import Token, TokenType, ONE_CHAR_TOKENS, TWO_CHAR_TOKENS, KEYWORDS


class Scanner:

    def __init__(self, data: str):
        self.line = 0
        self.pos = 0
        self.data = data

    def scan(self):
        while self.pos < len(self.data):
            if self.data[self.pos] in [" ", "\t", "\n"]:
                if self.data[self.pos] == "\n":
                    self.line += 1
                self.pos += 1
                continue
            token = self.parse()
            if token.type != TokenType.COMMENT:
                yield token
        yield Token(TokenType.EOF, None, None, self.line)

    def parse(self) -> Token:
        for token in ONE_CHAR_TOKENS:
            if token.value.match(self.data[self.pos]) is not None:
                self.pos += 1
                return Token(token, None, None, self.line)
        for token in TWO_CHAR_TOKENS:
            if token.value.match(self.data[self.pos:]) is not None:
                self.pos += 2
                return Token(token, None, None, self.line)
        for token in KEYWORDS:
            if (match := token.value.match(self.data[self.pos:])) is not None:
                self.pos += match.span()[1]
                return Token(token, None, None, self.line)
        if (match := TokenType.NUMBER.value.match(self.data[self.pos:])) is not None:
            self.pos += match.span()[1]
            return Token(TokenType.NUMBER, None, float(match.group()), self.line)
        if (match := TokenType.STRING.value.match(self.data[self.pos:])) is not None:
            self.pos += match.span()[1]
            return Token(TokenType.STRING, None, match.group()[1:-1], self.line)
        if (match := TokenType.IDENTIFIER.value.match(self.data[self.pos:])) is not None:
            self.pos += match.span()[1]
            return Token(TokenType.IDENTIFIER, match.group(), "", self.line)
        if (match := TokenType.COMMENT.value.match(self.data[self.pos:])) is not None:
            self.pos += match.span()[1]
            return Token(TokenType.COMMENT, match.group(), "", self.line)
        raise SyntaxError(f"Syntax error on line {self.line}.")
