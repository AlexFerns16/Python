# -------------------------------------------
class planets:
    def set_data(self, d=0, r=0, t=0):
       self.distance = d
       self.radius = r
       self.time = t

    def revolution(self):
        import math
        rev = (2 * math.pi * self.distance) / self.time
        return rev
    
    def rotation(self):
        import math
        rot = (2 * math.pi * self.radius) / self.time
        return rot

earth = planets()
earth.set_data(d=8547893, t=365)
rev_ret_earth = earth.revolution()
print(rev_ret_earth)

jupiter = planets()
jupiter.set_data(d=6575063952, t=568)
rev_ret_jupiter = jupiter.revolution()
print(rev_ret_jupiter)

mars = planets()
mars.set_data(r=445146514, t=627)
rot_ret_mars = mars.rotation()
print(rot_ret_mars)

venus = planets()
venus.set_data(r=541464, t=487)
rot_ret_venus = venus.rotation()
print(rot_ret_venus)

rad = 756625
time = 655
venus.set_data(r=rad, t=time)
rot_ret_venus = venus.rotation()
print(rot_ret_venus)
