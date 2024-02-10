from enum import Enum
from attrs import define
from typing import Any
import re


class TokenType(Enum):
    LEFT_PAREN = re.compile(r"^\(")
    RIGHT_PAREN = re.compile(r"^\)")
    LEFT_BRACE = re.compile(r"^\{")
    RIGHT_BRACE = re.compile(r"^}")
    COMMA = re.compile(r"^,")
    DOT = re.compile(r"^\.")
    MINUS = re.compile(r"^-")
    PLUS = re.compile(r"^\+")
    SEMICOLON = re.compile(r"^;")
    SLASH = re.compile(r"^/(?!/)")
    STAR = re.compile(r"^\*")
    BANG = re.compile(r"^!(?!=)")
    BANG_EQUAL = re.compile(r"^!=")
    EQUAL = re.compile(r"^=(?!=)")
    EQUAL_EQUAL = re.compile(r"^==")
    GREATER = re.compile(r"^>(?!=)")
    GREATER_EQUAL = re.compile(r"^>=")
    LESS = re.compile(r"^<(?!=)")
    LESS_EQUAL = re.compile(r"^<=")
    IDENTIFIER = re.compile(r"^[a-zA-Z_][a-zA-Z_0-9]*")
    COMMENT = re.compile(r"^//[\w|\W]+\n")
    STRING = re.compile(r"^\"(\\.|[^\"\\])*\"")
    NUMBER = re.compile(r"^([0-9]*[.])?[0-9]+")
    AND = re.compile(r"^and")
    CLASS = re.compile(r"^class")
    ELSE = re.compile(r"^else")
    FALSE = re.compile(r"^false")
    FUN = re.compile(r"^fun")
    FOR = re.compile(r"^for")
    IF = re.compile(r"^if")
    NIL = re.compile(r"^nil")
    OR = re.compile(r"^or")
    RETURN = re.compile(r"^return")
    SUPER = re.compile(r"^super")
    THIS = re.compile(r"^this")
    TRUE = re.compile(r"^true")
    VAR = re.compile(r"^var")
    WHILE = re.compile(r"^while")
    EOF = re.compile(r"")


KEYWORDS = [TokenType.AND, TokenType.OR, TokenType.CLASS, TokenType.ELSE, TokenType.FOR, TokenType.TRUE,
            TokenType.FALSE, TokenType.FUN, TokenType.NIL, TokenType.IF, TokenType.RETURN, TokenType.SUPER,
            TokenType.THIS, TokenType.VAR, TokenType.WHILE]

ONE_CHAR_TOKENS = [TokenType.LEFT_PAREN, TokenType.RIGHT_PAREN, TokenType.LEFT_BRACE, TokenType.RIGHT_BRACE,
                   TokenType.COMMA, TokenType.SEMICOLON, TokenType.DOT, TokenType.STAR, TokenType.PLUS, TokenType.MINUS]

TWO_CHAR_TOKENS = [TokenType.SLASH, TokenType.BANG, TokenType.BANG_EQUAL, TokenType.EQUAL, TokenType.EQUAL_EQUAL,
                   TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS, TokenType.LESS_EQUAL]


@define
class Token:
    type: TokenType
    name: str | None
    literal: Any
    line: int
