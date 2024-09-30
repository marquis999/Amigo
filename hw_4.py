class Vehicle:
    def move(self, transport):
        pass

class Car(Vehicle):
    def move(self, transport):
        return f"{transport}, едет по дороге"
    
class Bicycle(Vehicle):
    def move(self, transport):
        return f"{transport}, едет по велодорожке"
    
class Boat(Vehicle):
    def move(self, transport):
        return f"{transport}, плывет по воде"
    
movei = [Car(), Bicycle(), Boat()]

for movei in movei:
    print(movei.move(input("Введите вид транспорта: ")))