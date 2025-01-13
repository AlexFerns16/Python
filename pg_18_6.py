# -------------------------------------------
class planets:
    def __init__(self, d=0, r=0, t=0):
       self.distance = d
       self.radius = r
       self.time = t

    def revolution(self):
        import math
        try:
            rev = (2 * math.pi * self.distance) / self.time
            print(id(self))
            return rev
        except:
            print('ZeroDivisionError')
    
    def rotation(self):
        import math
        rot = (2 * math.pi * self.radius) / self.time
        return rot
    
earth_one = planets(d=78559879, t=128)
rev_ret_earth_one = earth_one.revolution()
print(id(earth_one))
print(rev_ret_earth_one)

print()

earth_two = planets(d=565559879, t=478)
rev_ret_earth_two = earth_two.revolution()
print(id(earth_two))
print(rev_ret_earth_two)

var = earth_one.distance + earth_two.distance
print(var)
