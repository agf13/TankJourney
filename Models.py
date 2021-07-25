'''
    Here will be the models used by the game / future engine
'''


class Tank(object):
    def __init__(self, camera):
        self.position = [-1,-1]
        self.lives = 3
        self.weapon = 0
        self.skin = 0
        self.camera = camera
        
        
    def set_lives(self, lives):
        self.lives = lives
        
    def set_weapon(self, weapon_id):
        self.weapon = weapon_id
        
    def set_position(self, position):
        self.position = position
        
    def set_camera(self, camera):
        self.camera = camera
    
    def get_lives(self):
        return self.lives
    
    def get_weapon(self):
        return self.weapon
    
    def get_position(self):
        return self.position
    
    def get_camera(self):
        return self.camera


class Camera(object):
    def __init__(self):
        self.position = [-1,-1] #this will be the center of the tank 
        self.maximumHeight = 17
        self.maximumWidth = 50
        self.visibleMap = []
        
    
    def set_position(self, position):
        self.position = position
        
    def set_maximumWidth(self, dimension):
        self.maximumHeight = dimension
        
    def set_maximumHeight(self, dimension):
        self.maximumHeight = dimension
        
    def set_visibleMap(self, visibleMap):
        self.visibleMap = visibleMap
        
    def get_position(self):
        return self.position
    
    def get_maximumHeight(self):
        return self.maximumHeight
    
    def get_maximumWidth(self):
        return self.maximumWidth
    
    def get_visibleMap(self):
        return self.visibleMap
        
        

# # # Will not be used. At least for the time being
# class Map(object):
#     def __init__(self):
#         self.number_of_tank_players = 0
#         self.level_id = 0
#         self.map =[]
#         
#     def set_map(self, map):
#         self.map = map
#     
#     def set_tanl_playera(self, tanks):
#         self.tank_players = tanks
#         
#     def set_level_id(self, level_id):
#         self.level_id = level_id
#         
#     def get_number_of_tank_players(self):
#         return self.number_of_tank_players
#     
#     def get_map(self):
#         return self.map
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


