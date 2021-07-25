from Errors.ERRORS import ValidationError, StupidProgrammerError

class TankValidator(object):
    
    def __init__(self):
        pass
    
    def validateCenter(self, coord, direction, map):
        '''
        coord: the coord of the center of the tank( [0] - line; [1] - column)
        direction: 
            1 -> up
            2 -> down
            3 -> a left
            4 -> right
        map: the map on which the tank moves
        '''
        line = coord[0]
        column = coord[1]
        line_coords = []
        column_coords = []
        
        if direction != 1 and direction != 2 and direction != 3 and direction !=4:
            raise StupidProgrammerError()
        
        if direction == 1:
            line_coords = [-2,-2,-2,-2,-2]
            column_coords = [-2,-1,0,1,2]
        elif direction == 2:
            line_coords = [2,2,2,2,2]
            column_coords = [-2,-1,0,1,2]
        elif direction == 3:
            line_coords = [-2,-1,0,1,2]
            column_coords = [-2,-2,-2,-2,-2]
        elif direction == 4:
            line_coords = [-2,-1,0,1,2]
            column_coords = [2,2,2,2,2]
            
        for index in range(0, len(line_coords)):
            if (line + line_coords[index]) >= len(map) or (column + column_coords[index]) >= len(map[line]):
                print("first")
                raise ValidationError()            
            if map[line + line_coords[index]][column + column_coords[index]] != 0:
                print("second")
                raise ValidationError()
            










