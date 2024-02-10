from scanner import Scanner, TokenType


class TestScanner:

    def test_definition(self):
        scanner = Scanner('var benedict = Brunch("ham", "English muffin");')
        tokens = list(scanner.scan())
        types = [TokenType.VAR, TokenType.IDENTIFIER, TokenType.EQUAL, TokenType.IDENTIFIER, TokenType.LEFT_PAREN,
                 TokenType.STRING, TokenType.COMMA, TokenType.STRING, TokenType.RIGHT_PAREN, TokenType.SEMICOLON]
        for token, ttype in zip(tokens, types):
            assert token.type == ttype

    def test_class(self):
        code = """class Breakfast {
                    serve(who) {
                        print "Enjoy your " + this.meat + " and " +
                        this.bread + ", " + who + ".";
                    }
                //...
                }"""
        scanner = Scanner(code)
        tokens = list(scanner.scan())
        types = [TokenType.CLASS, TokenType.IDENTIFIER, TokenType.LEFT_BRACE, TokenType.IDENTIFIER,
                 TokenType.LEFT_PAREN, TokenType.IDENTIFIER, TokenType.RIGHT_PAREN, TokenType.LEFT_BRACE,
                 TokenType.IDENTIFIER, TokenType.STRING, TokenType.PLUS, TokenType.THIS, TokenType.DOT,
                 TokenType.IDENTIFIER, TokenType.PLUS, TokenType.STRING, TokenType.PLUS, TokenType.THIS,
                 TokenType.DOT, TokenType.IDENTIFIER, TokenType.PLUS, TokenType.STRING, TokenType.PLUS,
                 TokenType.IDENTIFIER, TokenType.PLUS, TokenType.STRING, TokenType.SEMICOLON, TokenType.RIGHT_BRACE,
                 TokenType.RIGHT_BRACE, TokenType.EOF]
        for token, ttype in zip(tokens, types):
            assert token.type == ttype

    def test_for(self):
        code = """
        for (var a = 1; a < 10; a = a + 1) {
            print(a);
        }
        """
        scanner = Scanner(code)
        tokens = list(scanner.scan())
        types = [TokenType.FOR, TokenType.LEFT_PAREN, TokenType.VAR, TokenType.IDENTIFIER, TokenType.EQUAL,
                 TokenType.NUMBER, TokenType.SEMICOLON, TokenType.IDENTIFIER, TokenType.LESS, TokenType.NUMBER,
                 TokenType.SEMICOLON, TokenType.IDENTIFIER, TokenType.EQUAL, TokenType.IDENTIFIER, TokenType.PLUS,
                 TokenType.NUMBER, TokenType.RIGHT_PAREN, TokenType.LEFT_BRACE, TokenType.IDENTIFIER,
                 TokenType.LEFT_PAREN, TokenType.IDENTIFIER, TokenType.RIGHT_PAREN, TokenType.SEMICOLON,
                 TokenType.RIGHT_BRACE, TokenType.EOF]
        for token, ttype in zip(tokens, types):
            assert token.type == ttype
