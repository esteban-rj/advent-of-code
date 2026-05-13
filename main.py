from typing import Tuple
from typing import Literal

def get_dial_number(current_position:int, movements: int, direction: Literal['L', 'R']) -> Tuple[int, int]:
    dial_size = 100
    times_0 = movements // dial_size
    movements = movements % dial_size
    
    if movements == 0:
        return current_position, times_0

    if direction == 'L':
        movements = -movements
    later_position_no_abs = (current_position + movements)
    later_position = (current_position + movements) % dial_size
    if (later_position_no_abs <= 0 and current_position != 0) or later_position_no_abs >= dial_size:
        times_0 += 1
    
    return later_position, times_0

if __name__ == "__main__":
    current_position = 50
    zero_count = 0
    #current_position_list = []
    while True:
        linea = input()

        if linea == '':
            break

        direction = linea[0]
        movements = int(linea[1:])
        current_position, times_0 = get_dial_number(current_position, movements, direction)

        #current_position_list.append((current_position, times_0))
        zero_count += times_0
    #print(current_position_list)
    print(zero_count)
            
    
    