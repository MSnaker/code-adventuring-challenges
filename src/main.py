"""
    Author: Marco Bissaro
    E-mail: marco.bissaro@dorbit.space
    Create date: 2025-05-29 17:17:32
    Last edit date: 2025-05-29 17:17:32

The purpose of this code is to solve Advent of code problems.
"""

import argparse
import os
import solvers

parser = argparse.ArgumentParser(description=__doc__, 
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("--year", "-y",
                    dest="year",
                    help="Year to solve for.")
parser.add_argument("--day", "-d",
                    dest="day",
                    help="Day to solve for.")
args = parser.parse_args()

match args.year:
    case '2015':
        import solvers.solver2015 as solver
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

def main():
    print("Hello Hello Hello!")
    print(f'Solving Advent of Code for year {args.year}!')

    with open(os.path.join(os.getcwd(), "input", args.year + "-" + args.day), 'r', encoding='utf-8') as input_file:
        input_content = input_file.read()
    
    this_year_solver = solver.Solver2015(input_content)
    
    try:
        this_year_solver.solvefirst()
    except NotImplementedError:
        pass
    
    try:
        this_year_solver.solvesecond()
    except NotImplementedError:
        pass
    
    print(f"This year's first problem solution is: {this_year_solver.first_sol}")
    print(f"This year's second problem solution is: {this_year_solver.second_sol}")
    


if __name__ == "__main__":
    main()
    

