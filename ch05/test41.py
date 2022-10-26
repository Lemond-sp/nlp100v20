class Car():
  def __init__(self,engine,tire):
    self.engine = engine
    self.tire = tire
    self.hoge = []

a = []
engine = 100
tire = "huga"
a.append(Car(engine,tire)) # huga 100

# リストとして扱う
engine = [120,130]
tire = ["hu","ga"]
# 一つのインスタンス変数として扱われる
a.append(Car(engine,tire))
for i,car in enumerate(a):
  print(car.engine,car.tire) 
  # huga 100 (１つ目)
  # ['hu', 'ga'] [120, 130] (２つ目)