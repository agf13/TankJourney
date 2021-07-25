'''
Created on Feb 25, 2019

@author: Sebi
'''
# import os


from repositories.Repository import TankRepository, MapRepository
from validators.Validator import TankValidator
from services.Service import TankService, MapService
from presentaion.UI import Console


tankRepository = TankRepository()
tankValidator = TankValidator()
tankService = TankService(tankRepository, tankValidator)

mapRepository = MapRepository()
mapService = MapService(mapRepository,tankValidator)


console = Console(tankService, mapService)


console.run()





