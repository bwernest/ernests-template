"""___Modules___________________________________________________________________________________"""

# Project
from ..utils import *

# Python
from lark import Tree, Token
from typing import List

"""___Classes___________________________________________________________________________________"""


class Transformer(ToolBox):

    def TreeToData(self, tree: Tree) -> any:
        self.add_log("Creating commands")
        tokens = self.GetTokens(tree)
        data = self.TokensToData(tokens)
        self.add_log("Saving binaryContent")
        return data

    def GetTokens(self, token: Token | List[Token]) -> List[Token]:
        tokens = []
        if isinstance(token, Token):
            tokens.append(token)
        elif isinstance(token, list):
            for item in token:
                tokens.extend(self.GetTokens(item))
        elif isinstance(token, Tree):
            tokens.append(self.GetTokenFromStr(token.data))
            tokens.extend(self.GetTokens(token.children))
        else:
            raise ValueError(f"Type unknown : {type(token)}")
        return tokens

    def GetTokenFromStr(self, str_token: str) -> Token:
        return Token(type="RULE", value=str_token)

    def TokensToData(self, tokens: List[Token]) -> any:
        token_lines = self.SplitTokensInLines(tokens)
        data: object = {}
        for token_line in token_lines:
            self.AddTokenLineToData(data, token_line)
        return data

    def SplitTokensInLines(self, tokens: List[Token]) -> List[List[Token]]:
        lines: List[List[Token]] = []
        for token in tokens[1:]:
            if token.type == "RULE":
                lines.append([])
            else:
                lines[-1].append(token)
        return lines

    def AddTokenLineToData(self, data: any, token_line: List[Token]) -> None:
        pass
