


class TankService(object):
    def __init__(self, tankRepository, tankValidator):
        self.tankRepository = tankRepository
        self.tankValidator = tankValidator
        
    
        
    
        
        
class MapService(object):
    def __init__(self, mapRepository, tankValidator):
        self.mapRepository = mapRepository
        self.tankValidator = tankValidator

    def up(self, player):
        position = self.mapRepository.get_tank_position(player)
        line = position[0] - 1
        column = position[1]
        center = [line,column]
        map = self.mapRepository.get_map()
        self.tankValidator.validateCenter(center,1, map)
        self.mapRepository.removeTank(player)
        self.mapRepository.set_tank_position(line, column, player)
        self.mapRepository.put_tank_on_map(player)
#         self.mapRepository.level1()
        
    def down(self, player):
        position = self.mapRepository.get_tank_position(player)
        line = position[0] + 1
        column = position[1]
        center = [line,column]
        map = self.mapRepository.get_map()
        self.tankValidator.validateCenter(center,2, map)
        self.mapRepository.removeTank(player)
        self.mapRepository.set_tank_position(line, column, player)
        self.mapRepository.put_tank_on_map(player)
#         self.mapRepository.level1()
        
    def left(self, player):
        position = self.mapRepository.get_tank_position(player)
        line = position[0]
        column = position[1] - 1
        center = [line,column]
        map = self.mapRepository.get_map()
        self.tankValidator.validateCenter(center,3, map)
        self.mapRepository.removeTank(player)
        self.mapRepository.set_tank_position(line, column,player)
        self.mapRepository.put_tank_on_map(player)
#         self.mapRepository.level1()
        
    def right(self, player):
        position = self.mapRepository.get_tank_position(player)
        line = position[0]
        column = position[1] + 1
        center = [line,column]
        map = self.mapRepository.get_map()
        self.tankValidator.validateCenter(center,4, map)
        self.mapRepository.removeTank(player)
        self.mapRepository.set_tank_position(line, column,player)
        self.mapRepository.put_tank_on_map(player)
#         self.mapRepository.level1()

    def start_level1(self):
        self.mapRepository.level1()
        
    def reset_map(self):
        self.mapRepository.reset_map()
        
    def get_map(self):
        return self.mapRepository.get_map()
        
    def get_map_rows(self):
        return self.mapRepository.get_map_rows()
        
    def get_map_columns(self):
        return self.mapRepository.get_map_columns()
    
    def get_number_of_tanks(self):
        return self.mapRepository.get_number_of_tanks()
        
    def draw(self):
        pass

    def load_level(self, level_chosen, number_of_playing_players):
        self.mapRepository.load_level_from_file(level_chosen, number_of_playing_players)
        
    def level_exist(self, level_chosen):
        list_of_levels = self.mapRepository.get_levels()
        if level_chosen not in list_of_levels:
            return 0
        return 1
    
    def get_levels(self):
        return self.mapRepository.get_levels()
    
    def get_tank_position(self, player):
        return self.mapRepository.get_tank_position(player)
    
    def get_camera_view(self, tank):
        return self.mapRepository.get_camera_view(tank)
    
    def get_camera_maximumHeight_by_player(self, player):
        return self.get_camera_maximumHeight(self.mapRepository.get_tank(player).get_camera())
    
    def get_camera_maximumWidth_by_player(self, player):
        return self.get_camera_maximumWidth(self.mapRepository.get_tank(player).get_camera())
    
    def get_camera_maximumHeight(self, camera):
        return camera.get_maximumHeight()
    
    def get_camera_maximumWidth(self, camera):
        return camera.get_maximumWidth()












