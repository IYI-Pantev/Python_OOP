from dct_mxn import StrDictMixin



class House(StrDictMixin):
    def  __init__(self, floors_count, has_garage, has_electricity, rooms_count, balconies_count, town, has_pool):
        self.floors_count = floors_count
        self.has_garage = has_garage
        self.has_electricity = has_electricity
        self.rooms_count = rooms_count
        self.balconies_count = balconies_count
        self.town = town
        self.has_pool = has_pool
