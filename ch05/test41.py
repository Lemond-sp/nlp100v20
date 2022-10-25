class Car():
  def __init__(self,engine,tire):
    self.engine = engine
    self.tire = tire
    self.hoge = []

a = []
engine = 100
tire = "huga"
a.append(Car(engine,tire)) #ここの挙動
for i,car in enumerate(a):
  print(car.tire,car.engine) # huga 100