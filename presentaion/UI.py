import os
import time
from Errors.ERRORS import StupidProgrammerError, ValidationError, PlayerError
from copy import deepcopy


class Console(object):
    def __init__(self, tankService, mapService):
        self.tankService = tankService
        self.mapService = mapService
        self.cameraType = 0 # 0 - see whole map, 1 - camera moves after player
        self.total_players = 0
        self.player = 0
        self.commands={
            "help": self.help,
            "exit": "exit",
            "change": self.change_level,
            "levels": self.show_levels,
            "w": self.up,
            "s":self.down,
            "a":self.left,
            "d":self.right,
            "fire": self.fire
            }
        self.explain_commnads={
            "help" : "Shows the available commands. Type them, then enter.",
            "exit": "It ends the game",
            "change": "Change the level",
            "levels": "Shows the existing levels",
            "w": "Moves the tank up",
            "s": "Moves the tank down",
            "a": "Moves the tank left",
            "d": "Moves the tank right",
            "fire": "Not sure if this will be implemented"
            }

        
    def help(self, parameters):
        output = ""
        for option in self.commands:
            output += "\t"
            output += str(option) + " - "
            output += self.explain_commnads[option]
            output += "\n"
        print(output)
            
    
    def change_level(self, parameters):
        self.mapService.reset_map()
        self.load_level()
        
    
    def show_levels(self, parameters):
        list_of_levels = ""
        for level in self.mapService.get_levels():
            list_of_levels += level + " "
        print(list_of_levels)
    
        
    def start_level1(self):
        self.mapService.start_level1()
        
    def get_number_of_tanks(self):
        return self.mapService.get_number_of_tanks()
        
    def choose_cameraType(self):        
        while True:
            cameraType = input("Camera type: 0 - normal view, 1 - after the character view  > ")
            if cameraType == "0" or cameraType == 0:
                cameraType = 0
                break
            elif cameraType == "1" or cameraType == 1:
                cameraType = 1
                break
                
        self.cameraType = cameraType
        
    def load_level(self):  
        levels = self.mapService.get_levels()
        print("Available levels ids are: " + " ".join(levels))
        while True:
            level_chosen = input("Input the number of the level you want: ")
            if self.mapService.level_exist(level_chosen) == 1:
                break
            else:
                print("\t* - That level does not exists")
            
        while True:
            try:
                number_of_playing_players = int(input("Chose the number of players: "))
                break
            except:
                print("The number of player should be a natural number.")
        self.mapService.load_level(level_chosen, number_of_playing_players)
        
        total_tanks = self.get_number_of_tanks()
        if total_tanks <= 0:
            raise PlayerError()
        self.total_players = total_tanks
        
        self.choose_cameraType()
        self.draw()
    
    
    def up(self, parameters):
        repeat = 1
        if len(parameters) != 0 and parameters[0] != "":
            repeat = int(parameters[0])
        while repeat > 0:
            self.mapService.up(self.player)
            self.draw()
            repeat = repeat - 1
        
    def down(self, parameters):
        repeat = 1
        if len(parameters) != 0 and parameters[0] != "":
            repeat = int(parameters[0])
        while repeat > 0:
            self.mapService.down(self.player)
            self.draw()
            repeat = repeat - 1
        
    def left(self, parameters):
        repeat = 1
        if len(parameters) != 0 and parameters[0] != "":
            repeat = int(parameters[0])
        while repeat > 0:
            self.mapService.left(self.player)
            self.draw()
            repeat = repeat - 1
        
    def right(self, parameters):
        repeat = 1
        if len(parameters) != 0 and parameters[0] != "":
            repeat = int(parameters[0])
        while repeat > 0:
            self.mapService.right(self.player)
            self.draw()
            repeat = repeat - 1
    
    def fire(self,parameters):
        print("It will do sth in the future ... maybe")
        
    def draw(self):
        os.system("cls")
        objects = [" ","-","|","/","\\","0","."]
        output = ""
        if self.cameraType == 0:
            map = self.mapService.get_map()
            map_rows = self.mapService.get_map_rows()
            map_columns = self.mapService.get_map_columns()
            for row in map:
                for column in row:
                    output += objects[column]
                output+="\n"
        else:
            
            tanks = self.get_number_of_tanks()
            maps = []
            for index in range(0, tanks):
                map = self.get_camera_view(index)
                maps.append(map)
                
            map = []
            total_height = 0
            height = 0
            for index in range(0, tanks):
                if index % 2 == 0:
                    for line in maps[index]:
                        map.append(line)
                        height += 1
                        total_height += 1
                elif index % 2 == 1:
                    decrementor = height + 0
                    height = 0
                    for line in maps[index]:
                        for space in range(0,20):
                            if (total_height-decrementor) >= self.mapService.get_camera_maximumHeight_by_player(self.player):
                                map[total_height-decrementor].append(0)
                        for character in line:
                            if (total_height-decrementor) >= self.mapService.get_camera_maximumHeight_by_player(self.player):
                                map[total_height-decrementor].append(character)
                        decrementor -= 1
            for row in map:
                for column in row:
                    output += objects[column]
                output+="\n"
        print(output)
        time.sleep(0.01)
    
    
    def get_camera_view(self, index):
        return self.mapService.get_camera_view(index)
    
        
        
    def next_player(self):
        self.player = (self.player + 1) % self.total_players
        
    def phantom_next_player(self):
        return (self.player + 1) % self.total_players
        
    def init_game(self):
#         self.start_level1()
        while True:
            try:
                self.load_level()
                break
            except PlayerError as pe:
                print("\t* - The map does not suport that many players")
                self.mapService.reset_map()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def run(self):
        self.init_game()
        while True:
            command = input(">")
            paramaters = command.split(" ")
            if paramaters[0] == "exit":
                return
            elif paramaters[0] in self.commands:
                try:
                    self.commands[paramaters[0]](paramaters[1:])
                    self.next_player()
                except StupidProgrammerError as spe:
                    print("StupidProgrammerError. If you are a player... then I'm sorry for you. This means that something is wrong in my code. :< ...")
                except ValidationError as ve:
                    print("\t* - You can't break the walls.")
                    self.next_player()
                except PlayerError as pe:
                    print("\t* - The map does not support that many players")
                except ValueError as ve:
                    print(ve)
            else:
                print("\tUnknown command")










