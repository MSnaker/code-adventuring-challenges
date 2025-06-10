"""
    Author: Marco Bissaro
    E-mail: marco.bissaro@dorbit.space
    Create date: 2025-05-29 17:17:32
    Last edit date: 2025-05-29 17:17:32

The purpose of this code is to solve Advent of code problems.
"""

import argparse
import os
import json
        
parser = argparse.ArgumentParser(description=__doc__, 
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("--year", "-y",
                    dest="year",
                    help="Year to solve for.")
parser.add_argument("--day", "-d",
                    dest="day",
                    help="Day to solve for.")
parser.add_argument("--debug", 
                    dest="debug",
                    help="Argument to enable debug mode.",
                    action="store_true")
args = parser.parse_args()


try:
    match int(args.year):
        case 2015:
            from solver.solver2015 import Solver as ThisYearSolver
        # case '2016':
        #     import solvers.s2016
        # case '2017':
        #     import solvers.s2017
        # case '2018':
        #     import solvers.s2018
        # case '2019':
        #     import solvers.s2019
        # case '2020':
        #     import solvers.s2020
        case _:
            raise NotImplementedError
except ValueError:
    raise ValueError(f"Invalid year: {args.year}. Please provide a valid year as an integer.")


class Solver(ThisYearSolver):
    """
    The Solver class defines a solver for the advent of code challenges.
    Depending on the year given as input, the class' solver object will be a solver from
    the solvers package."""
    
    def __init__(self, year: int, day: int, *args, **kwargs) -> None:
        super().__init__()
        self.year = year
        self.day = day
        
    def set_input(self, input_file: str) -> None:
        with open(input_file, 'r', encoding='UTF-8') as file:
            self.input = file.read()
            
    def get_solver_functions(self) -> None:
        self.solvefirst = getattr(self, f"d{self.day}_p1")
        self.solvesecond = getattr(self, f"d{self.day}_p2")
        
def main():
    print("Hello Hello Hello!")
    print(f'Solving Advent of Code for year {args.year}!')
    print(f'The day is {args.day}!')
    
    solverinho = Solver(year=int(args.year), day=int(args.day))
    if args.debug:
        filepath = os.path.join(os.getcwd(), "input", args.year, args.day, "tests.json")
        with open(filepath, 'r') as jsontests:
            tests = json.load(jsontests)
    else:
        filepath = os.path.join(os.getcwd(), "input", args.year, args.day, "input")
        if not os.path.isfile(filepath): raise FileNotFoundError
        solverinho.set_input(filepath)

    solverinho.get_solver_functions()

    if args.debug:
        for problem, test_cases in tests.items():
            for test_case in test_cases:
                solverinho.input = test_case["input"]
                print(f"Testing with input {solverinho.input}")
                print(f"Expected result: {test_case['result']}")
                match problem:
                    case "p1":
                        solverinho.solvefirst()
                        print(f"First problem solves as {solverinho.first_sol}")
                    case "p2":
                        solverinho.solvesecond()
                        print(f"Second problem solves as {solverinho.second_sol}")
        return

    try:
        solverinho.solvefirst()
    except NotImplementedError:
        pass
    
    try:
        solverinho.solvesecond()
    except NotImplementedError:
        pass
    
    print(f"This year's first problem solution is: {solverinho.first_sol}")
    print(f"This year's second problem solution is: {solverinho.second_sol}")
    


if __name__ == "__main__":
    main()
    

