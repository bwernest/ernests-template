"""___Modules_______________________________________________________________"""

# Project
from engine.engine.engine import Engine
from engine.parser.main import *

# Python
import cProfile
import pstats

"""___Execution_____________________________________________________________"""

with cProfile.Profile() as pr:
	engine = Engine("prod")
	engine.start()

pr.dump("profil.prof")
