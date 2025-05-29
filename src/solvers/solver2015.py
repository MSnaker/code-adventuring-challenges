class Solver2015():
    def __init__(self, input_data:str, args*, kwargs**):
        self.input = input_data
        self.first_sol, self.second_sol = None, None
        
        
        
        
        
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
            
        print(f'Found: {upcount} ), {downcount} (')
            
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
            
