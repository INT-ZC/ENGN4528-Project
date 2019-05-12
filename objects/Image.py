class Image(object):
    def __init__(self, image):
        self.image = image
        self.windshield = image[0:490, 0:1200]
        self.left_mirror = image[58:296, 16:193]
        self.right_mirror = image[58:296, 1082:1259]
        self.navigation = image[578:683, 246:424]
        self.assistant = image[268:472, 27:287]
        self.odometer = image[653:662, 626:680]
        self.fuel_gauge = image[612:620, 920:974]
        self.left_turn = image[565:584, 735:756]
        self.right_turn = image[565:584, 863:883]
        self.parking_break = image[565:584, 901:924]
        self.seat_belt = image[565:585, 927:943]
        self.battery_charge = image[578:581, 969:982]
        self.malfunction_indicator = image[679:694, 907:929]
        self.glow_plug = image[680:694, 907:929]
        self.light0 = image[567:575, 1108:1120]
        self.light1 = image[569:577, 1123:1135]
        self.light2 = image[570:578, 1138:1150]
        self.light3 = image[570:578, 1154:1170]
        self.light4 = image[572:578, 1174:1179]
        self.light5 = image[579:583, 1174:1179]
        self.failure0 = image[684:693, 624:641]
        self.failure1 = image[682:694, 647:665]
        self.failure2 = image[682:693, 670:688]
        self.failure3 = image[682:693, 693:712]

    def windshield(self):
        return {'w': self.windshield}