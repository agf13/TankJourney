import os
from Models import Tank, Camera
from Errors.ERRORS import PlayerError


class TankRepository(object):
    def __init__(self):
        self.tank = Tank(Camera())

    def init_level(self):
        pass
    
    def draw_tank(self):
        pass
    
    
    
    
'''
0 - moving space " "(the tank can stand on those)
1 - wall V1 "-"
2 - vall V2 "|"
3 - wall V3 "/"
4 - wall V4 "\"
5 - tank part 1 "0"
6 - tank part 2 "."
'''
class MapRepository(object):
    def __init__(self):
        self.map = []
        self.map_rows = 0
        self.map_columns = 0
        self.number_of_tanks = 0
        self.tanks = []
        self.levels = {
#             "level1" : "repositories/level1.txt",
#             "level2" : "repositories/level2.txt"
            }
        self.simbols = {
            " ": 0,
            "S": 0,
            "-": 1,
            "|": 2,
            "/": 3,
            "\\": 4,
            "0": 5,
            ".": 6
            }
        self.find_levels()
        
        
    
    def reset_map(self):
        self.__init__()
        
        
        
    '''
        Def: returns the map as a matrix (a list of lists)
    '''
    def get_map(self):
        return self.map
    
    def get_camera_view(self, tank_id):
        position = self.get_tank_position(tank_id)
        line = position[0]
        column = position[1]
        tank = self.tanks[tank_id]
        width = tank.get_camera().get_maximumWidth()
        height = tank.get_camera().get_maximumHeight()
        vertical_start = line
        vertical_stop = line
        horizontal_start = column
        horizontal_stop = column
        while height > 0:
            decrementor = 0
            if vertical_start > 0:
                vertical_start -= 1
                decrementor += 1
            if vertical_stop < self.get_map_rows():
                vertical_stop += 1
                decrementor += 1
            height = height - decrementor
            if decrementor == 0:
                break
            
        while width > 0:
            decrementor = 0
            if horizontal_start > 0:
                horizontal_start -= 1
                decrementor += 1
            if horizontal_stop < self.get_map_columns():
                horizontal_stop += 1
                decrementor += 1
            width = width - decrementor
            if decrementor == 0:
                break
        map = []
        if tank_id != 0 and tank_id != 1:
            for new_lines in range(0,3):
                map.append([0])
        for line in range(vertical_start, vertical_stop):
            one_line = []
            for column in range(horizontal_start, horizontal_stop):
                one_line.append(self.map[line][column])
            map.append(one_line)
        return map
        
    
    
    def count_map_rows(self):
        counter = 0
        for line in self.map:
            counter += 1
        self.map_rows = counter
        
        
    def count_map_columns(self):
        counter = 0
        maximum = 0
        for line in self.map:
            counter = 0
            for column in line:
                counter += 1
            if counter > maximum:
                maximum = counter + 0
        self.map_columns = counter
    '''
        Def: returns the number of lines on the map
    '''
    def get_map_rows(self):
        return self.map_rows
    
      
    '''
        Def: returns the number of columns on the map
    '''
    def get_map_columns(self):
        return self.map_columns


    def add_tank(self):
        tank = Tank(Camera())
        self.tanks.append(tank)

    '''
        Def: sets the tank position
    '''        
    def set_tank_position(self, line, column, index):
        self.tanks[index].set_position([line, column])
        
        
    '''
        Def: returns a list containeg the line on pos 0 and the column on pos 2
    '''
    def get_tank_position(self, index):
        return self.tanks[index].get_position()
    
    
    '''
        Def: returns the number of tank players
    '''
    def get_number_of_tanks(self):
        return self.number_of_tanks
    
    
    def get_tank(self, index):
        return self.tanks[index]
    
     
    '''
        Def: loads the tank on the map
    '''   
    def put_tank_on_map(self, index):
        position = self.tanks[index].get_position()
        line = position[0]
        column = position[1]
        map = self.map
        index = index + 1
        #the 0
        map[line-2][column-2] = 5
        map[line-2][column+2] = 5
        map[line][column] = 5
        map[line+2][column-2] = 5
        map[line+2][column+2] = 5
        
        #the "|"
        map[line-1][column-2] = 2
        map[line-1][column] = 2
        map[line-1][column+2] = 2
        map[line+1][column-2] = 2
        map[line+1][column] = 2
        map[line+1][column+2] = 2
        
        #the "-"
        map[line-2][column-1] = 1
        map[line-2][column+1] = 1
        map[line][column-1] = 1
        map[line][column+1] = 1
        map[line+2][column-1] = 1
        map[line+2][column+1] = 1
        
        #the "."
        map[line-2][column] = 6
        map[line][column-2] = 6
        map[line][column+2] = 6
        map[line+2][column] = 6
        
        #the "/"
        map[line-1][column-1] = 3
        map[line+1][column-1] = 3
        
        #the "\"
        map[line-1][column+1] = 4
        map[line+1][column+1] = 4
        
        self.map = map


    '''
    def: replace the position occupied by the tank with " " (which is represented as a 0 in the map)
    '''
    def removeTank(self, index):
        position_changer = [-2,-1,0,1,2]
        center = self.tanks[index].get_position()
        line = center[0]
        column = center[1]
        for index in range(0, len(position_changer)):
            temporary_line = line + position_changer[index]
            for second_index in range(0, len(position_changer)):
                temporary_column = column + position_changer[second_index]
                self.map[temporary_line][temporary_column] = 0
        
#     '''
#         Def: loads in the map the level1 ( (1IV2019) Now that I can load
#            levels from .txt files, I don't think that I need this anymore
#     '''
#     def level1(self):
#         '''
#         0 - moving space " "(the tank can stand on those)
#         1 - wall V1 "-"
#         2 - vall V2 "|"
#         3 - wall V3 "/"
#         4 - wall V4 "\"
#         5 - tank part 1 "0"
#         6 - tank part 2 "."
#         '''
#         #clear the map
#         self.map = []
#         
#         #set the dimensions
#         self.map_rows = 20
#         self.map_columns = 20
#         
#         #get the dimensions you just set
#         rows = self.get_map_rows()
#         columns = self.get_map_columns()
#         
#         #load the first row
#         one_row = []
#         for index in range(0,columns):
#             one_row.append(1)
#         self.map.append(one_row)
#         
#         #load the rest of the rows until the last one
#         for index in range(1,rows-1):
#             one_row = []
#             one_row.append(2)
#             for column in range(1,columns-1):
#                 one_row.append(0)
#             one_row.append(2)
#             self.map.append(one_row)
#             
#         #load the last row
#         one_row = []
#         for index in range(0,columns):
#             one_row.append(1)
#         self.map.append(one_row)
#         
#         #load the tank
#         self.set_tank_position(5, 3)
#         self.put_tank_on_map()

        
        
# map = MapRepository()
# map.level1()
# map.put_tank_on_map()
# map.draw()
# while(1):



    def load_level_from_file(self, level, number_of_playing_players):
        '''
        0 - moving space " "(the tank can stand on those)
        1 - wall V1 "-"
        2 - vall V2 "|"
        3 - wall V3 "/"
        4 - wall V4 "\"
        5 - tank part 1 "0"
        6 - tank part 2 "."
        '''
        level_chosen = self.levels[level]
        tanks_found = 0
        
        with open(level_chosen,"r") as level:
            temporary_map = []
            line_index = -1
            for line in level:
                line_index = line_index + 1
                column_index = -1
                temporary_line = []
                for simbol in line:
                    column_index = column_index + 1
                    if simbol == "\n":
                        continue
                    if simbol in self.simbols:
                        temporary_line.append(self.simbols[simbol])
                    else:
                        temporary_line.append(0)
                    if simbol == "S": 
                        if number_of_playing_players <= tanks_found:
                            continue
                        tanks_found = tanks_found + 1  
                        self.add_tank()
                        self.set_tank_position(line_index, column_index, tanks_found-1)
#                 temporary_map.append(temporary_line)
                self.map.append(temporary_line)
#             self.map = temporary_map
            if number_of_playing_players > tanks_found:
                raise PlayerError()
            self.number_of_tanks = tanks_found
            for index in range(0,tanks_found):
                self.put_tank_on_map(index)
        self.count_map_rows()
        self.count_map_columns()
                        

    '''
    def: a level looks loke this: "level7.txt" or "levelwow.txt"
    '''
    def seems_to_be_a_level(self, file_name):
#         print(file_name)
        if "level" not in file_name[:6]:
            return 0
#         print("\thas levle in it's name")
        parameters = file_name.split(".")
        if len(parameters) != 2 or parameters[1] != "txt":
            return 0
#         print("\ta single point and a txt extension")
        return 1
            
        
    def get_level_identifier(self, file_name):
        parameters = file_name.split(".")
        parameters = parameters[0].split("level")
        return parameters[1]
        

    def find_levels(self):
        files = os.listdir("repositories") #use this option if you run the entire from main (aka the entire project)
#         files = os.listdir()  #use this option if you run from this file for testing & debugging
        for file in files:
            if self.seems_to_be_a_level(file) == 1:
                identifier = self.get_level_identifier(file)
                file = "repositories/"+str(file)
                self.levels[identifier] = str(file)
#         print(self.levels)
        
    def get_levels(self):
        found_levels = []
        for level in self.levels:
            found_levels.append(level)
        return found_levels
        
    
    
        
    def nothing(self):
        pass    
        
        
# map = MapRepository()
# map.get_levels()
    
    