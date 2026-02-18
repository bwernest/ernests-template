"""___Modules___________________________________________________________________________________"""

# Project
from .grammar import grammar
from .transformer import Transformer
from ..utils import *

# Python
from lark import Lark, Tree
import os
import pickle

"""___Classes___________________________________________________________________________________"""


class Parser(Transformer):

    def GetData(self, file: str, **machins) -> any:
        self.del_log()
        self.add_log("=" * 80 + "\n" + "=" * 32 + f"  {self.project_title} {self.project_version}  Log  " + "=" *
                     32 + "\n" + "=" * 80 + "\n", disp=False, time=False)
        txt = self.read_txt(file)
        tree = self.parse(txt)
        data = self.TreeToData(tree)
        return data

    def parse(self, txt: str, lines: int = 0, force_scrap: bool = False) -> Tree:

        # Checks if parsing is needed
        if force_scrap or not os.path.isfile(self.paths["pickle"]):
            self.add_log("Parsing file", disp=True)
            if lines > 0:
                txt = "\n".join(txt.split("\n")[:min(lines, len(txt.split("\n")))])
            parser = Lark(grammar)
            ast = parser.parse(txt)
        else:
            self.add_log("Opening pickled file", disp=True)
            with open(self.paths["pickle"], "rb") as file:
                ast = pickle.load(file)

        # Saves pickle
        with open(self.paths["pickle"], "wb") as file:
            pickle.dump(ast, file)
        return ast
