from madlibs_games import vampires, spywords
import random

if __name__ == "__main__":
    m = random.choice([vampires, spywords])
    m.madlib()