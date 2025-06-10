class Solver():
    def __init__(self, *args, **kwargs):
        self.first_sol, self.second_sol = None, None
        self.input = ""
        
    def d1_p1(self)->None:
        self.first_sol = 0
        upcount, downcount = 0, 0
        for pos, char in enumerate(self.input):
            if '(' == char: 
                self.first_sol += 1
                upcount += 1
            elif ')' == char: 
                self.first_sol -= 1
                downcount += 1
            else: raise TypeError(f'Unexpected character found in input file: {char}. Position: {pos}.')
            
            
    def d1_p2(self)->None:
        current_pos = 0
        for step, char in enumerate(self.input):
            if '(' == char: 
                current_pos += 1
            elif ')' == char: 
                current_pos -= 1
            else: raise TypeError(f'Unexpected character found in input file: {char}. Position: {step}.')
            if current_pos < 0: 
                self.second_sol = step + 1
                return
    def d2_p1(self) -> None:
        self.first_sol = 0
        for element in self.input.split("\n"):
            element = [int(number) for number in element.split("x")]
            sides_area = [element[0] * element[1], element[1] * element[2], element[2] * element[0]]
            self.first_sol += 2 * sum(sides_area) + min(sides_area)

    def d2_p2(self) -> None:
        self.second_sol = 0
        for sides in self.input.split("\n"):
            sides = [int(number) for number in sides.split("x")]
            ribbon_length = 1
            for side in sides:
                ribbon_length = ribbon_length * side
            smallest_perimeter = sides.remove(max(sides))
            ribbon_length += 2*sum(sides)
            self.second_sol += ribbon_length
        